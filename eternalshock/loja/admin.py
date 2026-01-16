from django.contrib import admin
from .models import Produto, ItemCarrinho, Pedido, ItemPedido


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'categoria', 'preco', 'estoque', 'ativo')
    list_filter = ('categoria', 'ativo', 'criado_em')
    search_fields = ('nome', 'descricao')
    list_editable = ('ativo', 'estoque')


@admin.register(ItemCarrinho)
class ItemCarrinhoAdmin(admin.ModelAdmin):
    list_display = ('produto', 'quantidade', 'session_key', 'criado_em')
    list_filter = ('criado_em',)


class ItemPedidoInline(admin.TabularInline):
    model = ItemPedido
    extra = 0


@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome_cliente', 'total', 'status', 'criado_em')
    list_filter = ('status', 'criado_em')
    search_fields = ('nome_cliente', 'email')
    inlines = [ItemPedidoInline]
    readonly_fields = ('criado_em', 'atualizado_em')
