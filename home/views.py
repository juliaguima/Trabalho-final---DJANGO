from django.shortcuts import render,redirect
from home.models import Pesquisa
from africa.models import model_africa
from asia.models import model_asia
from america.models import model_america
from oceania.models import model_oceania
from europa.models import model_europa

def view_home(request):
    cont = []
    cont.extend(model_africa.objects.all())
    cont.extend(model_oceania.objects.all())
    cont.extend(model_asia.objects.all())
    cont.extend(model_europa.objects.all())
    cont.extend(model_america.objects.all())
    dicionario = {'cont': cont}
    return render(request, 'home/paginas/index.html', context=dicionario)



def view_busca(request):
    pesquisa = Pesquisa.objects.all()

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            pesquisa = pesquisa.filter(nome__icontains=nome)
    itens_filtro = []
    itens_filtro.extend(model_africa.objects.filter(País__icontains=nome))
    itens_filtro.extend(model_america.objects.filter(País__istartswith=nome))
    itens_filtro.extend(model_asia.objects.filter(País__icontains=nome))
    itens_filtro.extend(model_oceania.objects.filter(País__icontains=nome))
    itens_filtro.extend(model_europa.objects.filter(País__icontains=nome))

    return render(request, 'home/paginas/busca.html', context={
        'pesquisa': pesquisa,
        'itens_filtro': itens_filtro,
        
    })