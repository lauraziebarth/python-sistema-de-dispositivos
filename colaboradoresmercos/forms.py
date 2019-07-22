# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from django import forms
from colaboradoresmercos.enums import AREAS


class FormColaborador(forms.Form):
    nome = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    area = forms.ChoiceField(choices=AREAS)
    senha = forms.CharField(widget=forms.PasswordInput)


class FormLogin(forms.Form):
    email = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput)

