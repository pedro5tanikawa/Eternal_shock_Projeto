from django.shortcuts import render

# Create your views here.
def primeiros_modelos(request):
    contexto = {
        'title' : 'eternal shock | primeiros modelos'
    }
    return render(
        request,
        'primeiros_modelos/index.html',
        contexto,
    )