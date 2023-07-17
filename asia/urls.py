from django.urls import path
from . import views

app_name = 'asia'

urlpatterns = [
    path('', views.view_home, name='home'),
]