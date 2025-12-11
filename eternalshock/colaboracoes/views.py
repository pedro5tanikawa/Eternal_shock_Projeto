

from django.shortcuts import render

# Create your views here.
def colaboracoes(request):
    return render(
        request,
        'colaboracoes/index.html'
    )