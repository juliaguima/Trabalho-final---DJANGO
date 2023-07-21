from django.shortcuts import render
from usuario.forms import LoginForms
 

def view_login(request):
    formulario = LoginForms()
    return render(request, 'usuario/paginas/login.html',context={'formulario': formulario})


def view_cadastro(request):
    return render(request, 'usuario/paginas/cadastro.html')