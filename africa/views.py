from django.shortcuts import render
from . import models



def v_africaCont(request):

    objetos = models.mod_africa.objects.all()
    dicionario = {'obj': objetos }
    return render(request,'africa/paginas/index.html',context=dicionario)
