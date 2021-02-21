from django.test import TestCase

from dispositivos.gateway import busca_dispositivos_nao_excluidos
from dispositivos.tests.core_test_case import criar_dispositivo_android, criar_dispositivo_android_excluido


class BuscaDispositivosNaoExcluidosTests(TestCase):
    def setUp(self):
        self.dispositivo_excluido = criar_dispositivo_android_excluido()


    def test_retorna_dispositivo_nao_excluido_corretamente(self):
        dispositivo_ativo = criar_dispositivo_android()

        dispositivos_nao_excluidos = busca_dispositivos_nao_excluidos()

        self.assertEqual(1, len(dispositivos_nao_excluidos))
        self.assertEqual(dispositivo_ativo.id, dispositivos_nao_excluidos[0].id)

    def test_nao_retorna_dispositivos_quando_nenhum_esta_excluido(self):
        retorno = busca_dispositivos_nao_excluidos()

        self.assertEqual(0, len(retorno))
