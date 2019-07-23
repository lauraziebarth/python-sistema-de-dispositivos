# coding: utf-8
from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals
from django import forms
from dispositivosmercos.enums import DISPOSITIVOS_OS


class FormDispositivo(forms.Form):
    sistema_operacional = forms.ChoiceField(choices=DISPOSITIVOS_OS, required=True)
    nome = forms.CharField(max_length=30, required=True)
    descricao = forms.CharField(max_length=30, required=True)
    numeromodelo = forms.CharField(max_length=30, required=True)
    versao = forms.CharField(max_length=10, required=True)
