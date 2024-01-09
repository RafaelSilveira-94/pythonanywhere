from .forms import UsuarioForm, LoginForm, EventoForm
from django.contrib import messages
from django.contrib.auth import authenticate, login 

class CadastrarPerfilService:
    def cadastrar_perfil(self, request):
        form = UsuarioForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()            
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return True
        else:
            return False
        
class LogarService:
    def Logar(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user is not None:
                login(request, user)
                messages.success(request,f'Hi {user.get_username()}, welcome back!')
                return True
            else:
                messages.error(request,f'Invalid username or password') 
                return False
            
class CadastrarEventoService:
    def Cadastrar(self, request):
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            evento = form.save(commit=False)
            evento.User = request.user 
            evento.save()
            form.save_m2m()
            messages.success(request, 'Evento cadastrado com sucesso.')
            return True
        else:
            messages.error(request, 'Erro ao cadastrar evento. Verifique os campos.')
            return False
