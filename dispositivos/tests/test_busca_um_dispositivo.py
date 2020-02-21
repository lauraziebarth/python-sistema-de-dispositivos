from django.test import TestCase

from dispositivos.gateway import busca_um_dispositivo
from dispositivos.tests.core_test_case import criar_dispositivo_android


class BuscaUmUnicoDispositivo(TestCase):

    def test_busca_um_unico_dispositivo(self):
        dispositivo = criar_dispositivo_android()
        criar_dispositivo_android()

        resultado = busca_um_dispositivo(dispositivo.id)

        self.assertEqual(dispositivo.id, resultado.id)
