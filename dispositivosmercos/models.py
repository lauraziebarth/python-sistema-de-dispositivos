from django.db import models


class Dispositivos(models.Model):
    os = models.IntegerField(default=False, null=False)
    nome = models.CharField(max_length=30)
    descricao = models.CharField(max_length=30)
    numeromodelo = models.CharField(max_length=30, default='NULL')
    versao = models.CharField(max_length=10)
    disponivel = models.BooleanField(default=True)
    excluido = models.BooleanField(default=False)
    ultima_alteracao = models.DateTimeField(null=True)


class DispositivosColaborador(models.Model):
    dispositivo = models.ForeignKey(Dispositivos, on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey('colaboradoresmercos.Colaborador', on_delete=models.DO_NOTHING)
    data_de_emprestimo = models.DateField()
    emprestimo_ativo = models.BooleanField(default=True)
    ultima_alteracao = models.DateTimeField(null=True)


