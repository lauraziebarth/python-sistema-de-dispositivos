from dispositivos.models import Dispositivos
from datetime import datetime


DISPOSITVIO_ANDROID_DEFAULT = {
    'os': 'android',
    'nome': 'android default',
    'descricao': 'A30',
    'versao': '9.0',
    'disponivel': True,
    'excluido': False,
    'ultima_alteracao': datetime.now()
}

DISPOSITVIO_IOS_DEFAULT = {
    'os': 'ios',
    'nome': 'ios default',
    'descricao': 'XS',
    'versao': '13.0',
    'disponivel': True,
    'excluido': False,
    'ultima_alteracao': datetime.now()
}


DISPOSITVIO_ANDROID_EXCLUIDO_DEFAULT = {
    'os': 'android',
    'nome': 'android default',
    'descricao': 'A30',
    'versao': '9.0',
    'disponivel': True,
    'excluido': True,
    'ultima_alteracao': datetime.now()
}

DISPOSITVIO_IOS_EXCLUIDO_DEFAULT = {
    'os': 'ios',
    'nome': 'ios default',
    'descricao': 'XS',
    'versao': '13.0',
    'disponivel': True,
    'excluido': True,
    'ultima_alteracao': datetime.now()
}


def merge_dicts(base, other):
    return dict(base, **other) if other is not None else base


def criar(model, default, **kwargs):
    return model.objects.create(**merge_dicts(default, kwargs))


def criar_dispositivo_android(**kwargs):
    return criar(Dispositivos, DISPOSITVIO_ANDROID_DEFAULT, **kwargs)


def criar_dispositivo_ios(**kwargs):
    return criar(Dispositivos, DISPOSITVIO_IOS_DEFAULT, **kwargs)


def criar_dispositivo_android_excluido(**kwargs):
    return criar(Dispositivos, DISPOSITVIO_ANDROID_EXCLUIDO_DEFAULT, **kwargs)


