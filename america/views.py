from django.shortcuts import render
from . import models



def v_americano(request):
    cont = models.model_america.objects.all()
    dicionario = {'cont': cont}
    return render(request,'America/paginas/index.html',context=dicionario)


def v_detalhe(request, link_url):

    detalhe = models.model_america.objects.filter(link=link_url)
    dicionario = {'detalhe':detalhe[0]}

    return render(request, 'America/paginas/detalhe.html', context=dicionario)