from django.test import TestCase
from dispositivos.gateway import busca_um_dispositivo
from dispositivos.tests.core_test_case import criar_dispositivo_android, criar_dispositivo_ios


class BuscaUmUnicoDispositivoTests(TestCase):
    def setUp(self):
        self.dispositivo_android = criar_dispositivo_android()
        self.dispositivo_ios = criar_dispositivo_ios()

    def test_retorna_um_unico_dispositivo(self):
        resultado = (busca_um_dispositivo(self.dispositivo_android.id))

        self.assertEqual(1, resultado.id)