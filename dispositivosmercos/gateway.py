from __future__ import absolute_import
from __future__ import print_function
from __future__ import unicode_literals

from datetime import datetime
from dispositivosmercos.models import Dispositivos


def busca_dispositivos_nao_excluidos():
    return Dispositivos.objects.filter(excluido=False)


def busca_um_dispositivo(dispositivo_id):
    return Dispositivos.objects.get(id=dispositivo_id)


def alterar_dispositivo(dispositivo_id, sistema_operacional, nome, descricao, numeromodelo, versao):
    dispositivo = busca_um_dispositivo(dispositivo_id)
    dispositivo.os = sistema_operacional
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


def cria_novo_dispositivo(sistema_operacional, nome, descricao, numeromodelo, versao):
    dispositivo = Dispositivos()
    dispositivo.os = sistema_operacional
    dispositivo.nome = nome
    dispositivo.descricao = descricao
    dispositivo.numeromodelo = numeromodelo
    dispositivo.versao = versao
    dispositivo.save()


def busca_dispostivos_emprestados():
    return Dispositivos.objects.filter(disponivel=False)


def busca_dispositivos_emprestados_por_colaborador(colaborador_id):
    return DispositivosColaborador.objects.get(colaborador_id=colaborador_id)


def busca_vinculo_colaboradordispositivo(dispositivo_id, colaborador_id):
    return DispositivosColaborador.objects.get(dispositivo_id=dispositivo_id, colaborador_id=colaborador_id)


def criar_vinculo_colaboradordispositivo_emprestimo(dispositivo_id, colaborador_id):
    dispositivoscolaborador = DispositivosColaborador()
    dispositivoscolaborador.colaborador_id = colaborador_id
    dispositivoscolaborador.dispositivo_id = dispositivo_id
    dispositivoscolaborador.data_de_emprestimo = datetime.now()
    dispositivoscolaborador.save()


def emprestar_dispositivo(dispositivo_id):
    dispositivo = busca_um_dispositivo(dispositivo_id)
    dispositivo.disponivel = False
    dispositivo.ultima_alteracao = datetime.now()
    dispositivo.save()


def atualizar_vinculo_colaboradordispositivo_datadedevolucao(dispositivo_id, colaborador_id):
    dispositivoscolaborador = busca_vinculo_colaboradordispositivo(dispositivo_id=dispositivo_id, colaborador_id=colaborador_id)
    dispositivoscolaborador.data_de_devolucao = datetime.now()
    dispositivoscolaborador.ultima_alteracao = datetime.now()
    dispositivoscolaborador.save()


def devolver_dispositivo(dispositivo_id):
    dispositivo = busca_um_dispositivo(dispositivo_id)
    dispositivo.disponivel = True
    dispositivo.ultima_alteracao = datetime.now()
    dispositivo.save()
    

