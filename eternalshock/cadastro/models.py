from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Pessoa(models.Model):
    id_pessoa = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    email = models.EmailField(max_length=255)
    foto_perfil = models.ImageField(upload_to='perfis/', null=True, blank=True)
    favoritos = models.ManyToManyField('loja.Produto', blank=True, related_name='favoritos_usuarios')
    
    def __str__(self):
        return self.nome