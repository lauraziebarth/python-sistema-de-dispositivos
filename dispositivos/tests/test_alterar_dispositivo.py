from django.test import TestCase

from dispositivos.gateway import alterar_dispositivo, busca_um_dispositivo
from dispositivos.tests.core_test_case import criar_dispositivo_android


class AlteraDispostivoTests(TestCase):

    def test_altera_um_dispositivo(self):
        dispositivo = criar_dispositivo_android()
        alteracoes = {
            'os': 'android',
            'nome': 'Mercos',
            'descricao': 'A70',
            'numeromodelo': 'MERCOS001',
            'versao': '9.0'
        }

        alterar_dispositivo(dispositivo.id, alteracoes['os'], alteracoes['nome'], alteracoes['descricao'], alteracoes['numeromodelo'], alteracoes['versao'])

        dispositivo_alterado = busca_um_dispositivo(dispositivo.id)
        self.assertEqual(alteracoes['os'], dispositivo_alterado.os)
        self.assertEqual(alteracoes['nome'], dispositivo_alterado.nome)
        self.assertEqual(alteracoes['descricao'], dispositivo_alterado.descricao)
        self.assertEqual(alteracoes['numeromodelo'], dispositivo_alterado.numeromodelo)
        self.assertEqual(alteracoes['versao'], dispositivo_alterado.versao)

    def test_altera_o_dispositivo_correto(self):
        dispositivo = criar_dispositivo_android()
        criar_dispositivo_android()
        alteracoes = {
            'os': 'android',
            'nome': 'Mercos',
            'descricao': 'A70',
            'numeromodelo': 'MERCOS001',
            'versao': '9.0'
        }

        alterar_dispositivo(dispositivo.id, alteracoes['os'], alteracoes['nome'], alteracoes['descricao'],
                            alteracoes['numeromodelo'], alteracoes['versao'])

        dispositivo_alterado = busca_um_dispositivo(dispositivo.id)
        self.assertEqual(dispositivo.id, dispositivo_alterado.id)
        self.assertEqual(alteracoes['nome'], dispositivo_alterado.nome)
