from django.shortcuts import render

# Create your views here.
def historia(request):
    contexto = {
        'title' : 'Eternal Shock | Historia'
    }
    return render(
        request,
        'historia/index.html',
        contexto,
    )