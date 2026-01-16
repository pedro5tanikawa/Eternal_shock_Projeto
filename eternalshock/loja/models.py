from django.db import models

class Produto(models.Model):
    CATEGORIAS = [
        ('relogios', 'Relógios'),
        ('acessorios', 'Acessórios'),
        ('edicoes-limitadas', 'Edições Limitadas'),
        ('colaboracoes', 'Colaborações'),
    ]
    
    nome = models.CharField(max_length=200)
    descricao = models.TextField()
    categoria = models.CharField(max_length=50, choices=CATEGORIAS)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', default='placeholder.jpg')
    estoque = models.IntegerField(default=0)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'
    
    def __str__(self):
        return self.nome


class ItemCarrinho(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.IntegerField(default=1, min_value=1)
    session_key = models.CharField(max_length=40, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name = 'Item do Carrinho'
        verbose_name_plural = 'Itens do Carrinho'
    
    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
    
    def total_item(self):
        return self.produto.preco * self.quantidade


class Pedido(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('processando', 'Processando'),
        ('enviado', 'Enviado'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]
    
    nome_cliente = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField()
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=200, blank=True)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    
    total = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pendente')
    
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
    
    def __str__(self):
        return f"Pedido #{self.id} - {self.nome_cliente}"


class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    quantidade = models.IntegerField()
    preco_unitario = models.DecimalField(max_digits=10, decimal_places=2)
    
    class Meta:
        verbose_name = 'Item do Pedido'
        verbose_name_plural = 'Itens do Pedido'
    
    def __str__(self):
        return f"{self.quantidade}x {self.produto.nome}"
    
    def total_item(self):
        return self.preco_unitario * self.quantidade
