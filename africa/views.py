from django.shortcuts import render

def view_home(request):
    return render(request, 'africa/paginas/index.html')
