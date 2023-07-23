from django.db import models

class Pesquisa(models.Model):

    CATEGORIAS = [
        ('País','PAÍS'),
        ('Continente','CONTINENTE'),
    ]

    nome = models.CharField(max_length=100,null=False,blank=False)
    categoria = models.CharField(max_length=100,choices=CATEGORIAS,default='')
    eh_publicada = models.BooleanField(default=False)


    def __str__(self):
        return self.nome

