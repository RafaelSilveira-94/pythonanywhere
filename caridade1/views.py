from django.shortcuts import render, get_object_or_404
from .models import Evento, Item
from django.utils import timezone
from django.http import Http404


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
