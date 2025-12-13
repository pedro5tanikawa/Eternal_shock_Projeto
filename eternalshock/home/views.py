from django.shortcuts import render

# Create your views here.
def home(request):
    contexto = {
        'title' : 'eternal shock | home'
    }
    return render(
        request,
        'home/index.html',
        contexto,
    )