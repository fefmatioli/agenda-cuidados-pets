from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pets/', views.listar_pets, name='listar_pets'),
    path('pets/adicionar/', views.adicionar_pet, name='adicionar_pet'),
    path('pets/editar/<int:id>/', views.editar_pet, name='editar_pet'),
    path('pets/remover/<int:id>/', views.remover_pet, name='remover_pet'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/adicionar/', views.adicionar_evento, name='adicionar_evento'),
    path('buscar/', views.buscar, name='buscar'),
]
