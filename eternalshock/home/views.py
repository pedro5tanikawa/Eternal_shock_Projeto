from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'title' : 'Eternal Shock | Home'
    }
    return render(
        request,
        'home/index.html',
        contexto,
    )