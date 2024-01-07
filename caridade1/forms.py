from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Evento, Item, Reservado

class LoginForm(forms.Form):
    username = forms.CharField(max_length=65)
    password = forms.CharField(max_length=65, widget=forms.PasswordInput)
    

class UsuarioForm(UserCreationForm):
    class Meta:
        model=User
        fields = ['username','email','password1','password2']

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nome', 'ativo',]

class cadastrar_itemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['descricao', 'foto', 'preco', 'evento']        

class reservar_itemForm(forms.ModelForm):
    class Meta:
        model = Reservado
        fields = ['reservado']