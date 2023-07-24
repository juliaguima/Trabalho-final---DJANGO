from django.db import models

class model_africa(models.Model):

    Continente = models.CharField(max_length=100)
    País = models.CharField(max_length=100)
    Descricao = models.CharField(max_length=3000)
    OndeFicar = models.CharField(max_length=1800)
    OndeComer = models.CharField(max_length=1800)
    OndeVisitar = models.CharField(max_length=1800)
    foto = models.ImageField(upload_to='img/%Y/%m/%d/')
    ta_publicado = models.BooleanField(default=False)
    link = models.CharField(max_length=60)




    def __str__(self):
        return self.País


