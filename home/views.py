from django.shortcuts import render,redirect
from home.models import Pesquisa
from africa.models import model_africa

def view_home(request):
    return render(request, 'home/paginas/index.html')



def view_busca(request):
    pesquisa = Pesquisa.objects.all()

    if 'buscando' in request.GET:
        nome = request.GET['buscando']
        if nome:
            pesquisa = pesquisa.filter(nome__icontains=nome)

        if pesquisa == 'Africa':
            return redirect('Africa:continente')
            
    return render(request, 'home/paginas/busca.html',context={'pesquisa':pesquisa})

