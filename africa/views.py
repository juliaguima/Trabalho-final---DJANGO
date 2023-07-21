from django.shortcuts import render
from . import models



def v_contAfr(request):
    contact = models.model_africa.objects.all()
    dicionario = {'conta': contact}
    return render(request,'Africa/paginas/index.html',context=dicionario)
