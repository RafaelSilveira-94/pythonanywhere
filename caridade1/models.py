from django.db import models

# Create your models here.
class Evento(models.Model):
    duracao = models.DurationField(null = True, blank = True)
    ativo = models.BooleanField(default = False)
    nome = models.CharField(max_length = 30)

class Item(models.Model):
    descricao = models.CharField(max_length = 100)
    foto = models.ImageField(upload_to = 'caridade')
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)

