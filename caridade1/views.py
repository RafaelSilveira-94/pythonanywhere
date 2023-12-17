from django.shortcuts import render, get_object_or_404
from .models import Evento, Item
from django.utils import timezone
from django.http import Http404


# Create your views here.
def index(request):
    lista_evento = Evento.objects.filter(
        data_pub__lte = timezone.now()
    ).order_by('-data_pub')
    contexto = {'evento_list': lista_evento}
    return render(request, 'caridade/index.html', contexto)

def detail(request, evento_id):
    evento = get_object_or_404(Evento, pk=evento_id)
    item = Item.objects.filter(evento_id=evento_id)
    context={
        'evento':evento,
        'item': item,
        }
    if evento.ativo:
        raise Http404('Nenhum evento satisfaz o critério informado')
    return render(
        request, 'caridade/detalhes.html', context
    )
