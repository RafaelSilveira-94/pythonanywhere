from django.contrib import admin
from .models import Evento, Item, Reservado

# Register your models here.
admin.site.register(Evento)
admin.site.register(Item)
admin.site.register(Reservado)