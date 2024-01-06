from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Item
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from .services import CadastrarPerfilService, LogarService, CadastrarEventoService
from django import forms
from .forms import LoginForm, UsuarioForm, EventoForm, cadastrar_itemForm
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
            return redirect(reverse('caridade1:index'))
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
            return redirect(reverse('caridade1:index'))
        else:
            form = UsuarioForm(request.POST)
            return render(request, 'cadastro_perfil.html', {'form': form}) 

def cadastrar_evento(request):
    if request.method == 'GET':
        form = EventoForm()
        return render(request, 'cadastrar_evento.html', {'form' : form})
    if request.method == 'POST':
        service = CadastrarEventoService()
        deu_certo = service.Cadastrar(request)
        if deu_certo:
            return redirect('caridade1:index')
        else:
            form = EventoForm(request.POST)
            return render(request, 'cadastrar_evento.html', {'form': form}) 

def cadastrar_item(request):
    if request.method == 'GET':
        form = cadastrar_itemForm()
        return render(request, 'cadastrar_item.html', {'form': form})
    elif request.method == 'POST':
        form = cadastrar_itemForm(request.POST, request.FILES)
        if form.is_valid():
            novo_item = form.save(commit=False)
            novo_item.save()
            return redirect('index')
        else:
            return render(request, 'cadastrar_item.html', {'form': form})