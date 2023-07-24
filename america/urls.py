from django.urls import path
from . import views

app_name = 'America'

urlpatterns = [
    
    path('Continente/',views.v_americano, name='continente'),
    path('Continente/detalhe/<str:link_url>/',views.v_detalhe, name='detalhe'),
    
    
]
