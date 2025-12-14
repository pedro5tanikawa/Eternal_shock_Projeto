from django.shortcuts import render

# Create your views here.
def primeiros_modelos(request):
    contexto = {
        'title' : 'Eternal Shock | Primeiros Modelos'
    }
    return render(
        request,
        'primeiros_modelos/index.html',
        contexto,
    )