from django.urls import path
from . import views

app_name = 'Africa'

urlpatterns = [
    
    path('Continente/',views.v_contAfr, name='contAfr'),
    
    
]
