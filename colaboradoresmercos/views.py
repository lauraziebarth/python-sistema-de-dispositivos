from django.http import HttpResponse
from django.views import View
from colaboradoresmercos.forms import FormColaborador, FormLogin
from colaboradoresmercos.models import Colaborador
from django.shortcuts import render, redirect
from django.urls import reverse



class CadastrarColaborador(View):
    def get(self, request):
        form = FormColaborador()
        return render(request, 'cadastrar_colaborador.html', {'form': form})

    def post(self, request):
        form = FormColaborador(request.POST)

        if not form.is_valid():
            return render(request, 'cadastrar_colaborador.html', {'form': form})

        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        area = form.cleaned_data['area']

        colaborador = Colaborador()
        colaborador.nome = nome
        colaborador.email = email
        colaborador.area = area
        colaborador.save()


class Login(View):
   def get(self, request):
        form = FormLogin()
        return render(request, 'login.html', {'form': form})

   def post(self, request):
       form = FormColaborador(request.POST)

       if not form.is_valid():
            return render(request, 'login.html', {'form': form})