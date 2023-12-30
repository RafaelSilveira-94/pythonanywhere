from django.shortcuts import render, get_object_or_404
from .models import Evento, Item
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from .services import CadastrarPerfilService, LogarService
from django import forms
from .forms import LoginForm, UsuarioForm
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
def index(request):
    evento_list = Evento.objects.all
    contexto = {'evento_list': evento_list}
    return render(request, 'index.html', contexto)

def detail(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    item = Item.objects.filter(evento_id=evento_id)
    
    context={
        'evento':evento,
        'item': item,
        }
    if evento.ativo is False:
        raise Http404('Nenhum evento satisfaz o critério informado')
    return render(
        request, 'detalhes.html', context
    )
### View Login
####################

def logar(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request, 'login.html', { 'form': form})
    elif request.method == 'POST':
        ls = LogarService()
        if ls.Logar(request):
            return redirect(reverse('index'))
        else: 
            form = LoginForm()
            return render(request,'login.html',{'form': form})
            
### View Cadastrar Perfil
###################        
    
def cadastrar_perfil(request):
    if request.method == 'GET':
        form = UsuarioForm()
        return render(request, 'cadastro_perfil.html', { 'form': form})
    if request.method == 'POST':
        cps = CadastrarPerfilService()
        if cps.cadastrar_perfil(request):
            return redirect(reverse('index'))
        else:
            form = UsuarioForm(request.POST)
            return render(request, 'cadastro_perfil.html', {'form': form}) 
