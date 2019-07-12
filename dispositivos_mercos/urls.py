"""dispositivos_mercos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from dispositivosmercos.views import ListarDispositivos, CadastrarDispositivo, ExcluirDispositivo, AlterarDispositivo
from colaboradoresmercos.views import CadastrarColaborador, Login

urlpatterns = [
    path('', Login.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('cadastrar_colaborador/', CadastrarColaborador.as_view(), name='cadastrar_colaborador'),

    path('listar_dispositivos/', ListarDispositivos.as_view(), name='listar_dispositivos'),
    path('cadastrar_dispositivo/', CadastrarDispositivo.as_view(), name='cadastrar_dispositivo'),
    path('alterar_dispositivo/<int:dispositivo_id>/', AlterarDispositivo.as_view(), name='alterar_dispositivo'),
    path('excluir_dispositivo/<int:dispositivo_id>/', ExcluirDispositivo.as_view(), name='excluir_dispositivo'),
]