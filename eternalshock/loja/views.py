

# Create your views here.
from django.shortcuts import render
from rest_framework import viewsets
from blog.serializers import TopicoSerializer
from blog.models import Topico

# Create your views here.
class TopicoViewSet(viewsets.ModelViewSet):
    queryset = Topico.objects.all()
    serializer_class = TopicoSerializer


# Create your views here.
def blog(request):
    # contexto = {
    #     'title' : 'ETERNAL SHOCK | Loja'
    # }
    exibe_artigos = {
        'artigos' : Topico.objects.all()
    }
    return render(
        request,
        'loja/index.html',
        #contexto,
        exibe_artigos,
    )