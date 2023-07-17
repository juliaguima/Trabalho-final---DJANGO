from django.shortcuts import render
from . import views

def view_home(request):
    return render(request, 'home/paginas/index.html')