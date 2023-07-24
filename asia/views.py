from django.shortcuts import render
from . import models

def v_asiatico(request):
    cont = models.model_asia.objects.all()
    dicionario = {'cont': cont}
    return render(request,'Asia/paginas/index.html',context=dicionario)


def v_detalhe(request, link_url):

    detalhe = models.model_asia.objects.filter(link=link_url)
    dicionario = {'detalhe':detalhe[0]}
    return render(request, 'Asia/paginas/detalhe.html', context=dicionario)