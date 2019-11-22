from django.views import View
from colaboradores.forms import FormColaborador, FormLogin
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout


class CadastrarColaborador(View):
    def get(self, request):
        form = FormColaborador()
        return render(request, 'cadastrar_colaborador.html', {'form': form})

    def post(self, request):
        from core.colaborador import cria_novo_colaborador

        form = FormColaborador(request.POST)

        if not form.is_valid():
            return render(request, 'cadastrar_colaborador.html', {'form': form})

        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        area = form.cleaned_data['area']
        senha = form.cleaned_data['senha']

        user = User.objects.create(first_name=nome, username=email, email=email)
        user.set_password(senha)
        user.save()

        cria_novo_colaborador(user.id, nome, email, area)

        return redirect(reverse('login'))


class Login(View):
    def get(self, request):
        form = FormLogin()
        return render(request, 'login.html', {'form': form})

    def post(self, request):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(reverse('listar_dispositivos'))
        else:
            return redirect(reverse('login'))


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect(reverse('login'))


class PerfilColaborador(View):
    def get(self, request):
        return render(request, 'perfil_colaborador.html')


class ImagemColaborador(View):
    def get(self, request):
        salva_imagem_colaborador()
        return render(request, 'cadastrar_colaborador.html', {'form': form})


