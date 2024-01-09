from django.shortcuts import render, get_object_or_404, redirect
from .models import Evento, Item, Reservado
from django.utils import timezone
from django.http import Http404
from django.urls import reverse
from .services import CadastrarPerfilService, LogarService, CadastrarEventoService
from django import forms
from .forms import LoginForm, UsuarioForm, EventoForm, cadastrar_itemForm, reservar_itemForm, pesquisa_itemForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import messages

# Create your views here.
def index(request):
    evento_list = Evento.objects.filter(ativo=True) 
    contexto = {'evento_list': evento_list}
    return render(request, 'index.html', contexto)

def detail(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    item = Item.objects.filter(evento_id=evento_id)
    if request.method == 'GET':    
        context={
            'evento':evento,
            'item': item,
            'form': reservar_itemForm()
            }
        if evento.ativo is False:
            raise Http404('Nenhum evento satisfaz o critério informado')
        return render(
            request, 'detalhes.html', context
        )

    if request.method == 'POST':
        if request.user.is_authenticated:
            form = reservar_itemForm(request.POST)  # Instantiate the form
            if form.is_valid():
                item_id = request.POST.get('item_id')  # Retrieve the item ID from POST data
                r_item = get_object_or_404(Item, pk=item_id)
                reservado = Reservado.objects.create(
                    item=r_item,  # Directly associate with the item
                    reservado=True,
                    User=request.user
                )
                reservado.save()
                messages.success(request, 'Item reservado com sucesso.')
                return redirect('caridade1:index')
        else:
            return redirect('caridade1:logar')
            


    
### View Login
####################

def logar(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('caridade1:index')
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
            novo_item.User = request.user
            novo_item.Reservado = False 
            novo_item.save()
            return redirect('caridade1:index')
        else:
            return render(request, 'cadastrar_item.html', {'form': form})
        
def logoff(request):
    logout(request)
    messages.success(request,'You have been logged out.')
    return redirect('caridade1:index')    

class Pesquisa_itemForm(forms.Form):
    termo_pesquisa = forms.CharField(label='Pesquisar item', max_length=100)

### View PESQUISAR items
#############
def pesquisar_item(request):
    items = Item.objects.all()
    form = Pesquisa_itemForm()
    
    if request.method == 'POST':
        form = Pesquisa_itemForm(request.POST)
        if form.is_valid():
            termo_pesquisa = form.cleaned_data.get('termo_pesquisa', '')
            items = Item.objects.filter(descricao__contains=termo_pesquisa)
    
    return render(request, 'resultado_pesquisa.html', {'form': form, 'items': items})