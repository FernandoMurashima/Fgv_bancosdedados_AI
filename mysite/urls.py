"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from lojasvarejistasapp.views import lojasvarejistasadmin
from lojasvarejistasapp.views import listar_loja
from lojasvarejistasapp.views import listar_produto
from lojasvarejistasapp.views import listar_vendeproduto

from lojasvarejistasapp.views import listar_loja, nova_loja, create_loja, visualizar_loja, editar_loja, atualizar_loja, excluir_loja
from lojasvarejistasapp.views import listar_produto, novo_produto, create_produto, visualizar_produto, editar_produto, atualizar_produto, excluir_produto
from lojasvarejistasapp.views import listar_vendeproduto, novo_vendeproduto, create_vendeproduto, visualizar_vendeproduto, editar_vendeproduto, atualizar_vendeproduto, excluir_vendeproduto

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', lojasvarejistasadmin, name='lojasvarejistasadmin' ),

    path('admin_loja/', listar_loja, name='listar_loja' ),
    path('admin_produto/', listar_produto, name='listar_produto'),
    path('admin_vendeproduto/', listar_vendeproduto, name='listar_vendeproduto'),

    path('listar_loja/', listar_loja, name='listar_loja'),
    path('nova_loja/', nova_loja, name='nova_loja'),
    path('create_loja/', create_loja, name='create_loja'),
    path('visualizar_loja/<str:pk>/', visualizar_loja, name='visualizar_loja'),
    path('editar_loja/<str:pk>/', editar_loja, name='editar_loja'),
    path('atualizar_loja/<str:pk>/', atualizar_loja, name='atualizar_loja'),
    path('excluir_loja/<str:pk>/', excluir_loja, name='excluir_loja'),

    path('produto/', listar_produto, name='listar_produto'),
    path('novo_produto/', novo_produto, name='novo_produto'),
    path('create_produto/', create_produto, name='create_produto'),
    path('visualizar_produto/<str:pk>/', visualizar_produto, name='visualizar_produto'),
    path('editar_produto/<str:pk>/', editar_produto, name='editar_produto'),
    path('atualizar_produto/<str:pk>/', atualizar_produto, name='atualizar_produto'),
    path('excluir_produto/<str:pk>/', excluir_produto, name='excluir_produto'),

    path('vendeproduto/', listar_vendeproduto, name='listar_vendeproduto'),
    path('novo_vendeproduto/', novo_vendeproduto, name='novo_vendeproduto'),
    path('create_vendeproduto/', create_vendeproduto, name='create_vendeproduto'),
    path('visualizar_vendeproduto/<int:pk>/', visualizar_vendeproduto, name='visualizar_vendeproduto'),
    path('editar_vendeproduto/<int:pk>/', editar_vendeproduto, name='editar_vendeproduto'),
    path('atualizar_vendeproduto/<int:pk>/', atualizar_vendeproduto, name='atualizar_vendeproduto'),
    path('excluir_vendeproduto/<int:pk>/', excluir_vendeproduto, name='excluir_vendeproduto'),

]