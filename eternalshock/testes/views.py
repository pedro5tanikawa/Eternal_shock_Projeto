from django.shortcuts import render

# Create your views here.
def testes(request):
    contexto = {
        'title' : 'Eternal Shock | Testes'
    }
    return render(
        request,
        'testes/index.html',
        contexto,
    )