from rest_framework import serializers
from .models import Produto, ItemCarrinho, Pedido, ItemPedido


class ProdutoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Produto"""
    categoria_display = serializers.CharField(source='get_categoria_display', read_only=True)
    
    class Meta:
        model = Produto
        fields = [
            'id',
            'nome',
            'descricao',
            'categoria',
            'categoria_display',
            'preco',
            'imagem',
            'estoque',
            'ativo',
            'criado_em',
            'atualizado_em',
        ]
        read_only_fields = ['id', 'criado_em', 'atualizado_em']


class ProdutoListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem de produtos"""
    categoria_display = serializers.CharField(source='get_categoria_display', read_only=True)
    
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'preco', 'imagem', 'categoria', 'categoria_display', 'estoque']


class ItemCarrinhoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo ItemCarrinho"""
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(),
        write_only=True,
        source='produto'
    )
    total_item = serializers.SerializerMethodField()
    
    class Meta:
        model = ItemCarrinho
        fields = [
            'id',
            'produto',
            'produto_id',
            'quantidade',
            'session_key',
            'total_item',
            'criado_em',
        ]
        read_only_fields = ['id', 'session_key', 'criado_em']
    
    def get_total_item(self, obj):
        """Calcula o total do item (preço x quantidade)"""
        return str(obj.total_item())


class ItemPedidoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo ItemPedido"""
    produto = ProdutoSerializer(read_only=True)
    produto_id = serializers.PrimaryKeyRelatedField(
        queryset=Produto.objects.all(),
        write_only=True,
        source='produto'
    )
    total_item = serializers.SerializerMethodField()
    
    class Meta:
        model = ItemPedido
        fields = [
            'id',
            'produto',
            'produto_id',
            'quantidade',
            'preco_unitario',
            'total_item',
        ]
        read_only_fields = ['id']
    
    def get_total_item(self, obj):
        """Calcula o total do item (preço unitário x quantidade)"""
        return str(obj.total_item())


class PedidoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Pedido"""
    itens = ItemPedidoSerializer(many=True, read_only=True)
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Pedido
        fields = [
            'id',
            'nome_cliente',
            'email',
            'telefone',
            'endereco',
            'numero',
            'complemento',
            'cidade',
            'estado',
            'cep',
            'total',
            'status',
            'status_display',
            'itens',
            'criado_em',
            'atualizado_em',
        ]
        read_only_fields = ['id', 'criado_em', 'atualizado_em']


class PedidoListSerializer(serializers.ModelSerializer):
    """Serializer simplificado para listagem de pedidos"""
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    
    class Meta:
        model = Pedido
        fields = [
            'id',
            'nome_cliente',
            'email',
            'total',
            'status',
            'status_display',
            'criado_em',
        ]
        read_only_fields = ['id', 'criado_em']


class CarrinhoResumoSerializer(serializers.Serializer):
    """Serializer para resumo do carrinho"""
    itens_count = serializers.IntegerField()
    total = serializers.DecimalField(max_digits=10, decimal_places=2)
    itens = ItemCarrinhoSerializer(many=True)
