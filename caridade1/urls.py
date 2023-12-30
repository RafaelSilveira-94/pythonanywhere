from django.urls import path
from . import views

app_name= 'caridade1'
urlpatterns=[
    path('', views.index, name='index'),
    path('evento/<int:evento_id>/', views.detail, name='detail'),
    path('logar/', views.logar, name='logar'),
    path('cadastrar_perfil/', views.cadastrar_perfil, name='cadastrar_perfil'),
]