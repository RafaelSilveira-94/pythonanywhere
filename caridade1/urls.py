from django.urls import path
from . import views

app_name= 'caridade1'
urlpatterns=[
    path('', views.index, name='index'),
    path('evento/<int:evento_id>/', views.detail, name='detail'),
    path('logar/', views.logar, name='logar'),
    path('cadastrar_perfil/', views.cadastrar_perfil, name='cadastrar_perfil'),
    path('cadastrar_evento/', views.cadastrar_evento, name='cadastrar_evento'),
    path('cadastrar_item/', views.cadastrar_item, name='cadastrar_item'),
    path('logout/', views.logoff, name='logoff'),
    path('pesquisar_item/', views.pesquisar_item, name='pesquisar_item'),
]