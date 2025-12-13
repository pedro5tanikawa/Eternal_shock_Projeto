from django.urls import path
from . import views
urlpatterns = [
    path('', views.primeiros_modelos, name='primeiros_modelos'),
]