from django.test import TestCase

from dispositivos.gateway import busca_dispositivos_nao_excluidos
from dispositivos.tests.core_test_case import criar_dispositivo_android, criar_dispositivo_android_excluido


class BuscaDispositivosNaoExcluidosTests(TestCase):
    def setUp(self):
        self.dispositivo_ativo = criar_dispositivo_android()
        self.dispositivo_excluido = criar_dispositivo_android_excluido()


    def test_retorna_um_unico_dispositivo_nao_excluido(self):
        resultado = len(busca_dispositivos_nao_excluidos())

        self.assertEqual(1, resultado)
