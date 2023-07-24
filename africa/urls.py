from django.urls import path
from . import views

app_name = 'Africa'

urlpatterns = [
    
    path('Continente/',views.v_contAfr, name='continente'),
    path('Continente/detalhe/<str:link_url>/',views.v_detalhe, name='detalhe'),
    
    
]
