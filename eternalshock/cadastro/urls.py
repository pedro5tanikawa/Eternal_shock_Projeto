from django.urls import path
from . import views
app_name = 'cadastro'
urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('gravar/', views.gravar, name="gravar"),
    path('perfil/', views.perfil, name='perfil'),
    path('perfil/editar/', views.editar_perfil, name='editar_perfil'),
    path('perfil/favorito/<int:produto_id>/', views.adicionar_favorito, name='adicionar_favorito'),
    path('perfil/favorito/remover/<int:produto_id>/', views.remover_favorito, name='remover_favorito'),
    path('mostrar/', views.exibe, name="mostrar"),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
]
