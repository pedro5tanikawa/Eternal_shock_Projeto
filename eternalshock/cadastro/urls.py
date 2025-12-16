from django.urls import path
from . import views
urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('gravar/', views.gravar, name="gravar"),
    path('mostrar/', views.exibe, name="mostrar"),
    
]