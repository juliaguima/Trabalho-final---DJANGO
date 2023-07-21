from django.urls import path
from usuario.views import view_login,view_cadastro

app_name = 'user'

urlpatterns = [
    
    path('Login/',view_login, name='login'),
    path('Cadastro/',view_cadastro, name='cadastro'),
    
    
]
