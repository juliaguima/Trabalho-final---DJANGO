from django.shortcuts import render

def view_home(request):
    return render(request, 'europa/paginas/index.html')
