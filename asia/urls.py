from django.urls import path
from . import views

app_name = 'Asia'

urlpatterns = [
    
    path('Continente/',views.v_asiatico, name='continente'),
    path('Continente/detalhe/<str:link_url>/',views.v_detalhe, name='detalhe'),
    
    
]
