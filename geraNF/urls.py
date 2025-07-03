from django.urls import path
from . import views

app_name = 'geraNF'

urlpatterns = [
    path('tomadores/', views.lista_tomadores, name='lista_tomadores'),
    path('tomadores/cadastrar/', views.cadastrar_tomador, name='cadastrar_tomador'),
    path('tomadores/<int:tomador_id>/', views.visualizar_tomador, name='visualizar_tomador'),
    path('tomadores/<int:tomador_id>/editar/', views.editar_tomador, name='editar_tomador'),
    path('tomadores/<int:tomador_id>/remover/', views.remover_tomador, name='remover_tomador'),
    path('gerar-nf/', views.gerar_nf, name='gerar_nf'),
] 