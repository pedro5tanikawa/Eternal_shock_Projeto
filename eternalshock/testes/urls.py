from django.urls import path
from . import views
urlpatterns = [
    path('', views.testes, name='testes' ),
]