from colaboradoresmercos.models import Colaborador


def cria_novo_colaborador(user_id, nome, email, area):
    colaborador = Colaborador()
    colaborador.user_id = user_id
    colaborador.nome = nome
    colaborador.email = email
    colaborador.area = area
    colaborador.save()

def salva_imagem_colaborador():
    pass
