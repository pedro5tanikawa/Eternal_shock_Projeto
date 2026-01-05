from django.urls import path
from . import views

app_name = 'cadastro'

urlpatterns = [
    path('', views.home, name='cadastro'),
    path('gravar/', views.gravar, name='gravar'),
    path('mostrar/', views.exibe, name='mostrar'),
]
