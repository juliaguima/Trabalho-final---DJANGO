from django.urls import path
from . import views

app_name = 'Europa'

urlpatterns = [
    
    path('Continente/',views.v_continente, name='continente'),
    path('Continente/detalhe/<str:link_url>/',views.v_detalhe, name='detalhe'),
    path('comentario/', views.view_comentario, name='comentario'),
    path('editar-comentario/<int:id>/', views.editar_comentario, name='editar_comentario'),
    path('excluir-comentario/<int:id>/', views.excluir_comentario, name='excluir_comentario'),

    
]
