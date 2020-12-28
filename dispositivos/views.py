from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.views import View
from dispositivos.forms import FormDispositivo
from dispositivos.models import Dispositivos
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate
from dispositivos.gateway import busca_dispositivos_nao_excluidos, busca_um_dispositivo, alterar_dispositivo, \
    excluir_dispositivo, cria_novo_dispositivo, emprestar_dispositivo, devolver_dispositivo, \
    criar_vinculo_colaboradordispositivo_emprestimo, atualizar_vinculo_colaboradordispositivo_datadedevolucao, \
    busca_dispositivos_emprestados, busca_dispostivos_emprestados
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from colaboradores.models import Colaborador


class ListarDispositivos(LoginRequiredMixin, View):
    def get(self, request):
        usuario_logado_id = request.user.id
        colaborador_logado = Colaborador.objects.get(user_id=usuario_logado_id)

        dispositivos = busca_dispositivos_nao_excluidos()
        return render(request, 'listar_todos_dispositivos.html', {'dispositivos': dispositivos, 'colaborador_logado': colaborador_logado})


class ListarDispositivosEmprestados(LoginRequiredMixin, View):
    def get(self, request):
        usuario_logado_id = request.user.id
        colaborador_logado = Colaborador.objects.get(user_id=usuario_logado_id)

        vinculos = busca_dispostivos_emprestados()
        return render(request, 'listar_dispositivos_emprestados.html', {'vinculos': vinculos, 'colaborador_logado': colaborador_logado})


class ListarDispositivosEmprestadosColaboradorLogado(LoginRequiredMixin, View):
    def get(self, request):
        usuario_logado_id = request.user.id
        colaborador_logado = Colaborador.objects.get(user_id=usuario_logado_id)

        vinculos = busca_dispositivos_emprestados(colaborador_logado.id)
        return render(request, 'listar_dispositivos_emprestados_por_colaborador.html', {
            'vinculos': vinculos,
            'colaborador_logado': colaborador_logado
        })


class CadastrarDispositivo(LoginRequiredMixin, View):
    def get(self, request):
        form = FormDispositivo()
        usuario_logado_id = request.user.id
        colaborador_logado = Colaborador.objects.get(user_id=usuario_logado_id)
        return render(request, 'cadastrar_dispositivo.html', {'form': form, 'colaborador_logado': colaborador_logado})

    def post(self, request):
        form = FormDispositivo(request.POST)

        if not form.is_valid():
            return render(request, 'cadastrar_dispositivo.html', {'form': form})

        sistema_operacional = form.cleaned_data['sistema_operacional']
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        numeromodelo = form.cleaned_data['numeromodelo']
        versao = form.cleaned_data['versao']

        cria_novo_dispositivo(sistema_operacional, nome, descricao, numeromodelo, versao)

        return redirect(reverse('listar_dispositivos'))


class AlterarDispositivo(LoginRequiredMixin, View):
    def get(self, request, dispositivo_id=None):
        dispositivo = busca_um_dispositivo(dispositivo_id)
        form = FormDispositivo(initial={'id': dispositivo.id, 'nome': dispositivo.nome, 'descricao': dispositivo.descricao, 'numeromodelo': dispositivo.numeromodelo, 'versao': dispositivo.versao})
        return render(request, 'alterar_dispositivo.html', {'form': form, 'dispositivo_id': dispositivo_id})

    def post(self, request, dispositivo_id=None):
        form = FormDispositivo(request.POST)

        if not form.is_valid():
            return render(request, 'alterar_dispositivo.html', {'form': form, 'dispositivo_id': dispositivo_id})

        sistema_operacional = form.cleaned_data['sistema_operacional']
        nome = form.cleaned_data['nome']
        descricao = form.cleaned_data['descricao']
        numeromodelo = form.cleaned_data['numeromodelo']
        versao = form.cleaned_data['versao']

        alterar_dispositivo(dispositivo_id, sistema_operacional, nome, descricao, numeromodelo, versao)

        return redirect(reverse('listar_dispositivos'))


class ExcluirDispositivo(LoginRequiredMixin, View):
    def get(self, dispositivo_id=None):
        excluir_dispositivo(dispositivo_id)
        return redirect(reverse('listar_dispositivos'))


class EmprestarDispositivo(LoginRequiredMixin, View):
    def get(self, request, dispositivo_id=None):
        usuario_logado_id = request.user.id
        colaborador_logado = Colaborador.objects.get(user_id=usuario_logado_id)

        criar_vinculo_colaboradordispositivo_emprestimo(dispositivo_id, colaborador_logado.id)
        emprestar_dispositivo(dispositivo_id)

        return redirect(reverse('listar_dispositivos'))


class DevolverDispositivo(LoginRequiredMixin, View):
    def get(self, vinculo_id=None):
        vinculo = atualizar_vinculo_colaboradordispositivo_datadedevolucao(vinculo_id)
        devolver_dispositivo(vinculo.dispositivo_id)

        return redirect(reverse('listar_dispositivos'))
