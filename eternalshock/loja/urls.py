from django.urls import path
from . import views

app_name = 'loja'

urlpatterns = [
    # Loja
    path('', views.loja, name='index'),
    path('produto/<int:produto_id>/', views.detalhes_produto, name='detalhes'),
    
    # Gerenciamento de produtos (admin)
    path('criar/', views.CriarProdutoView.as_view(), name='criar_produto'),
    path('editar/<int:produto_id>/', views.EditarProdutoView.as_view(), name='editar_produto'),
    path('deletar/<int:produto_id>/', views.DeletarProdutoView.as_view(), name='deletar_produto'),
    
    # Carrinho
    path('adicionar/<int:produto_id>/', views.adicionar_ao_carrinho, name='adicionar_carrinho'),
    path('carrinho/', views.carrinho, name='carrinho'),
    path('atualizar/<int:item_id>/', views.atualizar_carrinho, name='atualizar_carrinho'),
    path('remover/<int:item_id>/', views.remover_do_carrinho, name='remover_carrinho'),
    
    # Checkout
    path('checkout/', views.checkout, name='checkout'),
    path('confirmacao/<int:pedido_id>/', views.pedido_confirmacao, name='confirmacao'),
]

