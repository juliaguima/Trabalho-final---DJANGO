from django.shortcuts import render
from home.models import Pesquisa

def view_home(request):
    return render(request, 'home/paginas/index.html')

def view_busca(request):
    pesquisa = Pesquisa.objects.all()

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            pesquisa = pesquisa.filter(nome__icontains=nome)
    return render(request, 'home/paginas/busca.html',context={'pesquisa':pesquisa})

