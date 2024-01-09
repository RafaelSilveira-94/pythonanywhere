from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Evento(models.Model):
    duracao = models.DurationField(null = True, blank = True)
    ativo = models.BooleanField(default = False)
    nome = models.CharField(max_length = 30)
    User = models.ForeignKey(User, on_delete=models.CASCADE,null=False)

class Reservado(models.Model):
    User = models.ForeignKey(User, on_delete = models.CASCADE, )    
    reservado = models.BooleanField(default = False)

class Item(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE,null=False, blank = True)
    descricao = models.CharField(max_length = 100)
    foto = models.ImageField(upload_to = 'caridade')
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    evento = models.ForeignKey(Evento, on_delete=models.PROTECT)
    reservado = models.ForeignKey(Reservado, on_delete=models.PROTECT, null = True, blank = True)


