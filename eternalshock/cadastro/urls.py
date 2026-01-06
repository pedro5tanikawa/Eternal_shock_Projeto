from django.urls import path
from . import views
app_name = 'cadastro'
urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('gravar/', views.gravar, name="gravar"),
    path('mostrar/', views.exibe, name="mostrar"),
    path('editar/<int:id>', views.editar, name='editar'),
    path('atualizar/<int:id>', views.atualizar, name='atualizar'),
    path('apagar/<int:id>', views.apagar, name='apagar'),
    
]