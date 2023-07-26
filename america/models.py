from django.db import models
from django.contrib.auth.models import User

class model_america(models.Model):

    Continente = models.CharField(max_length=100)
    País = models.CharField(max_length=100)
    Descricao = models.CharField(max_length=3000)
    OndeFicar = models.CharField(max_length=1800)
    OndeComer = models.CharField(max_length=1800)
    OndeVisitar = models.CharField(max_length=1800)
    carr = models.ImageField(upload_to='img/%Y/%m/%d/')
    foto = models.ImageField(upload_to='img/%Y/%m/%d/')
    ta_publicado = models.BooleanField(default=False)
    link = models.CharField(max_length=60)


    def __str__(self):
        return self.País
    

    

class Comentario(models.Model):
    coment = models.CharField(max_length=100, null=False, blank=False)
    eh_publicada = models.BooleanField(default=True)
    link_url = models.CharField(max_length=100, null=False, blank=False)
    usuario = models.ForeignKey(
        to=User, 
        on_delete=models.SET_NULL, 
        null=True, blank=False, 
        related_name='user'
    )

    def __str__(self):
        return self.coment