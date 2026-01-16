from django.urls import path
from . import views

urlpatterns = [
    path('', views.loja, name='loja'),
    path('produto/<int:produto_id>/', views.detalhes_produto, name='detalhes_produto'),
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_ao_carrinho'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('atualizar/<int:item_id>/', views.atualizar_carrinho, name='atualizar_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_do_carrinho'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmacao/<int:pedido_id>/', views.pedido_confirmacao, name='pedido_confirmacao'),
]
