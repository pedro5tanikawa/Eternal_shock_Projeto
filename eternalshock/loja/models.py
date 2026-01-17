from django.db import models

# Create your models here.
from django.db import models


# Create your models here.
class Topico(models.Model):
    id   = models.AutoField(primary_key=True)
    tema = models.CharField(max_length=30)
    foto = models.ImageField()
    conteudo = models.TextField(blank=True, null=True)
    preco = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Preço'
    )

    def __str__(self):
        return self.tema
