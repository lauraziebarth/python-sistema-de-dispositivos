from django.db import models


class Colaborador(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.DO_NOTHING)
    nome = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    area = models.CharField(max_length=20)
    excluido = models.BooleanField(default=False)
    ultima_alteracao = models.DateTimeField(null=True)


class ColaboradorImagem(models.Model):
    colaborador_id = models.ForeignKey(Colaborador, on_delete=models.DO_NOTHING)
    imagem = models.ImageField(default='NULL')
    ultima_alteracao = models.DateTimeField(null=True)

