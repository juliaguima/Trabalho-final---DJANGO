from django.shortcuts import render,redirect,get_object_or_404
from . import models
from america.models import Comentario,model_america
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from america.forms import ComentarioForms


def v_americano(request):
    cont = models.model_america.objects.all()
    dicionario = {'cont': cont}
    return render(request,'America/paginas/index.html',context=dicionario)



def v_detalhe(request, link_url):
    detalhe = get_object_or_404(model_america, link=link_url)
    comentarios = Comentario.objects.filter(eh_publicada=True, link_url=link_url)
    formulario = ComentarioForms(initial={'link_url': link_url})

    if request.method == 'POST':
        formulario = ComentarioForms(request.POST)

        if formulario.is_valid():
            comentario = formulario.cleaned_data['Coment']
            link_url = formulario.cleaned_data['link_url']

            novo_comment = Comentario(coment=comentario, eh_publicada=False, link_url=link_url)
            novo_comment.save()

            messages.success(request, 'Comentário enviado para revisão.')
            return redirect('America:detalhe', link_url=link_url)

    return render(request, 'America/paginas/detalhe.html', context={'detalhe': detalhe, 'comentarios': comentarios, 'formulario': formulario})



def view_comentario(request):
    if request.method == 'POST':
        formulario = ComentarioForms(request.POST)

        if formulario.is_valid():
            comentario = formulario.cleaned_data['Coment']
            link_url = formulario.cleaned_data['link_url']
            usuario = request.user
            
            
            novo_comment = Comentario(coment=comentario, eh_publicada=True, link_url=link_url, usuario=usuario)
            novo_comment.save()
            return redirect('America:detalhe', link_url=link_url)

    else:
        formulario = ComentarioForms()

    return render(request, 'America/paginas/detalhe.html', context={'formulario': formulario})





def editar_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    
    if request.method == 'POST':
        formulario = ComentarioForms(request.POST, initial={'Coment': comentario.coment, 'link_url': comentario.link_url, 'usuario': request.user})
        
        if formulario.is_valid():
            comentario.coment = formulario.cleaned_data['Coment']
            comentario.link_url = formulario.cleaned_data['link_url']
            comentario.usuario = request.user 
            comentario.save()
            return redirect('America:detalhe', link_url=comentario.link_url)
        else:
            formulario = ComentarioForms(initial={'Coment': comentario.coment, 'link_url': comentario.link_url, 'usuario': request.user})
    
    return render(request, 'America/paginas/detalhe.html', {'formulario': formulario, 'comentarios': Comentario.objects.all()})


def excluir_comentario(request, id):
    comentario = get_object_or_404(Comentario, id=id)
    
    if request.method == 'POST':
        comentario.delete()
        return redirect('America:detalhe', link_url=comentario.link_url)

    return render(request, 'America/paginas/detalhe.html', {'formulario': ComentarioForms(),})

                        