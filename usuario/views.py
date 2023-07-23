from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from usuario.forms import LoginForms,CadastroForms
from django.contrib import auth
 

def view_login(request):
    formulario = LoginForms()

    if request.method == 'POST':
        formulario = LoginForms(request.POST)


        if formulario.is_valid():
            nome = formulario['nome_login'].value()
            senha = formulario['senha'].value()

            usuario = auth.authenticate(
                request,
                username = nome,
                password = senha
            )

            if usuario is not None:
                auth.login(request, usuario)
                messages.success(request,f'Bem vindo(a) {nome}!')
                return redirect('inicio:home')
            
            else:
                messages.error(request,'Nome ou senha incorretos!')
                return redirect('user:login')
            
    return render(request, 'usuario/paginas/login.html',context={'formulario': formulario})





def view_cadastro(request):
    formulario = CadastroForms()

    if request.method =='POST':
        formulario = CadastroForms(request.POST)

        if formulario.is_valid():
            if formulario['senha_1'].value() != formulario['senha_2'].value():
                messages.error(request,'As senhas não condizem!')
                return redirect('user:cadastro')
            
            nome = formulario['nome_cadastro'].value()
            email = formulario['email_cadastro'].value()
            senha = formulario['senha_1'].value()

            if User.objects.filter(username=nome).exists():
                messages.error(request,'Usuário já cadastrado!')
                return redirect('user:cadastro')
            

            novo_user = User.objects.create_user(
                username = nome,
                email = email,
                password = senha
            )

            novo_user.save()
            messages.success(request,'Cadastro realizado!')
    
            return redirect('user:login')
    
    return render(request, 'usuario/paginas/cadastro.html',context={'formulario': formulario})

def logout(request):
    auth.logout(request)
    messages.sucess(request,'Logout realizado com sucesso!')
    return redirect('user:login')