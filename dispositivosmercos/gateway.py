from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
from dispositivosmercos.models import Dispositivos


def busca_dispositivos_nao_excluidos():
    return Dispositivos.objects.filter(excluido=False)


def busca_um_dispositivo(dispositivo_id):
    return Dispositivos.objects.get(id=dispositivo_id)


def alterar_dispositivo(dispositivo_id, nome, descricao, numeromodelo, versao):
    dispositivo = busca_um_dispositivo(dispositivo_id)
    dispositivo.nome = nome
    dispositivo.descricao = descricao
    dispositivo.numeromodelo = numeromodelo
    dispositivo.versao = versao
    dispositivo.ultima_alteracao = datetime.now()
    dispositivo.save()


def excluir_dispositivo(dispositivo_id):
    dispositivo = busca_um_dispositivo(dispositivo_id)
    dispositivo.excluido = True
    dispositivo.ultima_alteracao = datetime.now()
    dispositivo.save()
