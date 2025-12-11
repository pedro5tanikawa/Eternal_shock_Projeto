from django.shortcuts import render

# Create your views here.
def primeiros_modelos(request):
    return render(
        request,
        'primeiros_modelos/index.html'
    )