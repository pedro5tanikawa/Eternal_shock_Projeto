from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from decimal import Decimal
from .models import Produto, ItemCarrinho, Pedido, ItemPedido


def obter_session_key(request):
    """Obtém ou cria uma session key para o usuário"""
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key


def loja(request):
    """Página principal da loja com listagem de produtos"""
    produtos = Produto.objects.filter(ativo=True)
    categoria = request.GET.get('categoria')
    
    if categoria:
        produtos = produtos.filter(categoria=categoria)
    
    categorias = dict(Produto._meta.get_field('categoria').choices)
    
    context = {
        'title': 'Loja G-Shock',
        'produtos': produtos,
        'categorias': categorias,
        'categoria_selecionada': categoria,
    }
    return render(request, 'loja/loja.html', context)


def detalhes_produto(request, produto_id):
    """Página de detalhes do produto"""
    produto = get_object_or_404(Produto, id=produto_id, ativo=True)
    produtos_relacionados = Produto.objects.filter(
        categoria=produto.categoria,
        ativo=True
    ).exclude(id=produto_id)[:4]
    
    context = {
        'title': f'{produto.nome} - G-Shock',
        'produto': produto,
        'produtos_relacionados': produtos_relacionados,
    }
    return render(request, 'loja/detalhes.html', context)


def adicionar_ao_carrinho(request, produto_id):
    """Adiciona um produto ao carrinho"""
    produto = get_object_or_404(Produto, id=produto_id)
    session_key = obter_session_key(request)
    quantidade = int(request.POST.get('quantidade', 1))
    
    item, criado = ItemCarrinho.objects.get_or_create(
        produto=produto,
        session_key=session_key,
        defaults={'quantidade': quantidade}
    )
    
    if not criado:
        item.quantidade += quantidade
        item.save()
    
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        carrinho = obter_carrinho_context(session_key)
        return JsonResponse({
            'sucesso': True,
            'mensagem': f'{produto.nome} adicionado ao carrinho!',
            'total_items': carrinho['total_items'],
            'total_preco': str(carrinho['total_preco']),
        })
    
    return redirect('carrinho')


def carrinho(request):
    """Página do carrinho de compras"""
    session_key = obter_session_key(request)
    itens = ItemCarrinho.objects.filter(session_key=session_key)
    
    total_preco = sum(item.total_item() for item in itens)
    
    context = {
        'title': 'Carrinho - G-Shock',
        'itens': itens,
        'total_preco': total_preco,
    }
    return render(request, 'loja/carrinho.html', context)


def atualizar_carrinho(request, item_id):
    """Atualiza a quantidade de um item no carrinho"""
    session_key = obter_session_key(request)
    item = get_object_or_404(ItemCarrinho, id=item_id, session_key=session_key)
    quantidade = int(request.POST.get('quantidade', 1))
    
    if quantidade > 0:
        item.quantidade = quantidade
        item.save()
    else:
        item.delete()
    
    return redirect('carrinho')


def remover_do_carrinho(request, item_id):
    """Remove um item do carrinho"""
    session_key = obter_session_key(request)
    item = get_object_or_404(ItemCarrinho, id=item_id, session_key=session_key)
    item.delete()
    
    return redirect('carrinho')


def checkout(request):
    """Página de checkout/finalização da compra"""
    session_key = obter_session_key(request)
    itens = ItemCarrinho.objects.filter(session_key=session_key)
    
    if not itens.exists():
        return redirect('carrinho')
    
    if request.method == 'POST':
        total = sum(item.total_item() for item in itens)
        
        pedido = Pedido.objects.create(
            nome_cliente=request.POST.get('nome_cliente'),
            email=request.POST.get('email'),
            telefone=request.POST.get('telefone'),
            endereco=request.POST.get('endereco'),
            numero=request.POST.get('numero'),
            complemento=request.POST.get('complemento', ''),
            cidade=request.POST.get('cidade'),
            estado=request.POST.get('estado'),
            cep=request.POST.get('cep'),
            total=total,
        )
        
        for item in itens:
            ItemPedido.objects.create(
                pedido=pedido,
                produto=item.produto,
                quantidade=item.quantidade,
                preco_unitario=item.produto.preco,
            )
        
        itens.delete()
        
        return redirect('pedido_confirmacao', pedido_id=pedido.id)
    
    total_preco = sum(item.total_item() for item in itens)
    
    context = {
        'title': 'Checkout - G-Shock',
        'itens': itens,
        'total_preco': total_preco,
    }
    return render(request, 'loja/checkout.html', context)


def pedido_confirmacao(request, pedido_id):
    """Página de confirmação do pedido"""
    pedido = get_object_or_404(Pedido, id=pedido_id)
    
    context = {
        'title': 'Pedido Confirmado - G-Shock',
        'pedido': pedido,
    }
    return render(request, 'loja/confirmacao.html', context)


def obter_carrinho_context(session_key):
    """Função auxiliar para obter dados do carrinho"""
    itens = ItemCarrinho.objects.filter(session_key=session_key)
    total_items = sum(item.quantidade for item in itens)
    total_preco = sum(item.total_item() for item in itens)
    
    return {
        'itens': itens,
        'total_items': total_items,
        'total_preco': total_preco,
    }


def contexto_global(request):
    """Context processor para adicionar dados do carrinho em todas as páginas"""
    if request.session.session_key:
        carrinho = obter_carrinho_context(request.session.session_key)
        return {
            'carrinho_total_items': carrinho['total_items'],
        }
    return {'carrinho_total_items': 0}
