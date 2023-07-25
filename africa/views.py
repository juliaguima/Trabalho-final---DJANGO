from django.shortcuts import render,redirect,get_object_or_404
from . import models
from africa.models import ComentarioAF,model_africa
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth
from africa.forms import ComentarioFormsAF



def v_contAfr(request):
    cont = models.model_africa.objects.all()
    dicionario = {'cont': cont}
    return render(request,'Africa/paginas/index.html',context=dicionario)



def v_detalhe(request, link_url):
    detalhe = get_object_or_404(model_africa, link=link_url)
    comentarios = ComentarioAF.objects.filter(eh_publicada=True, link_url=link_url)
    formulario = ComentarioFormsAF(initial={'link_url': link_url})

    if request.method == 'POST':
        formulario = ComentarioFormsAF(request.POST)

        if formulario.is_valid():
            comentario = formulario.cleaned_data['Coment']
            link_url = formulario.cleaned_data['link_url']

            novo_comment = ComentarioAF(coment=comentario, eh_publicada=False, link_url=link_url)
            novo_comment.save()

            messages.success(request, 'Comentário enviado para revisão.')
            return redirect('Africa:detalhe', link_url=link_url)

    return render(request, 'Africa/paginas/detalhe.html', context={'detalhe': detalhe, 'comentarios': comentarios, 'formulario': formulario})


def view_comentario(request):
    if request.method == 'POST':
        formulario = ComentarioFormsAF(request.POST)

        if formulario.is_valid():
            comentario = formulario.cleaned_data['Coment']
            link_url = formulario.cleaned_data['link_url']
            usuario = request.user
            
            
            novo_comment = ComentarioAF(coment=comentario, eh_publicada=True, link_url=link_url, usuario=usuario)
            novo_comment.save()
            return redirect('Africa:detalhe', link_url=link_url)

    else:
        formulario = ComentarioFormsAF()

    return render(request, 'Africa/paginas/detalhe.html', context={'formulario': formulario})