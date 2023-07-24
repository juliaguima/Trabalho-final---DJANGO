from django.shortcuts import render
from . import models



def v_contAfr(request):
    cont = models.model_africa.objects.all()
    dicionario = {'cont': cont}
    return render(request,'Africa/paginas/index.html',context=dicionario)


def v_detalhe(request, link_url):

    detalhe = models.model_africa.objects.filter(link=link_url)
    dicionario = {'detalhe':detalhe[0]}

    return render(request, 'Africa/paginas/detalhe.html', context=dicionario)