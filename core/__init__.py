from colaboradoresmercos.models import Colaborador


def cria_novo_colaborador(user, nome, email, area):
    colaborador = Colaborador()
    colaborador.user = user
    colaborador.nome = nome
    colaborador.email = email
    colaborador.area = area
    colaborador.save()



