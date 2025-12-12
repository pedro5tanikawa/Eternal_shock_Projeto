from django.urls import path
from . import views
urlpatterns = [
    path('primeiros_modelos/', views.primeiros_modelos),
]