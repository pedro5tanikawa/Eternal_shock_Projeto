from django.shortcuts import render

# Create your views here.
def testes(request):
    return render(
        request,
        'testes/index.html'
    )