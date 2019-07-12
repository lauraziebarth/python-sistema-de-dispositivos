# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from django import forms


class FormDispositivo(forms.Form):
    nome = forms.CharField(max_length=30)
    descricao = forms.CharField(max_length=30)
    numeromodelo = forms.CharField(max_length=30)
    versao = forms.CharField(max_length=10)