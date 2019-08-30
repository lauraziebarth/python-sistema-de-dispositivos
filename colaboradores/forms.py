# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from django import forms
from colaboradores.enums import AREAS


class FormColaborador(forms.Form):
    nome = forms.CharField(max_length=100, required=True)
    email = forms.CharField(max_length=100, required=True)
    area = forms.ChoiceField(choices=AREAS, required=True)
    senha = forms.CharField(widget=forms.PasswordInput, required=True)


class FormLogin(forms.Form):
    email = forms.CharField(max_length=100)
    senha = forms.CharField(widget=forms.PasswordInput)

