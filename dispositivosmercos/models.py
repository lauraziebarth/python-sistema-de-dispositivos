from django.db import models


class Dispositivos(models.Model):
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)
    numeromodelo = models.CharField(max_length=30, default='NULL')
    versao = models.CharField(max_length=10)
    disponivel = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    ultima_alteracao = models.DateTimeField(null=True)




