from django.shortcuts import render, redirect
from .models import Pessoa


# Página inicial do cadastro
def home(request):
    contexto = {
        'title': 'Eternal Shock | Cadastro'
    }
    return render(
        request,
        'cadastro/index.html',
        contexto
    )


# Função para salvar os dados no banco
def gravar(request):
    if request.method == 'POST':
        nova_pessoa = Pessoa()
        nova_pessoa.nome = request.POST.get('nome')
        nova_pessoa.idade = request.POST.get('idade')
        nova_pessoa.email = request.POST.get('email')
        nova_pessoa.save()

    # depois de salvar, volta para a página de cadastro
    return redirect('cadastro:cadastro')



# Página para exibir as pessoas cadastradas
def exibe(request):
    exibe_pessoas = {
        'pessoas': Pessoa.objects.all()
    }
    return render(
        request,
        'cadastro/mostrar.html',
        exibe_pessoas
    )
