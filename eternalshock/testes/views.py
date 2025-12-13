from django.shortcuts import render

# Create your views here.
def testes(request):
    contexto = {
        'title' : 'eternal shock | testes'
    }
    return render(
        request,
        'testes/index.html',
        contexto,
    )