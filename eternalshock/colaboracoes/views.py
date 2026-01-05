

from django.shortcuts import render

# Create your views here.
def colaboracoes(request):
    contexto = {
        'title' : 'Eternal Shock | Colaborações'
    }
    return render(
        request,
        'colaboracoes/index.html',
        contexto,
    )