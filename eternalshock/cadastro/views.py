from django.shortcuts import render

from cadastro.models import Pessoa

# Create your views here.
def cadastro(request):
    contexto = {
        'title' : 'Jornada Viagem | Cadastro'
    }
    return render(
        request,
        'cadastro/index.html',
        contexto,
    )

def gravar(request): #funçao para salvar os dados para a tabela
    nova_pessoa = Pessoa()
    nova_pessoa.nome = request.POST.get('nome')
    nova_pessoa.idade = request.POST.get('idade')
    nova_pessoa.email = request.POST.get('email')
    nova_pessoa.save()
    
    return cadastro(request)

def exibe(request):
    exibe_pessoas = {
        "pessoas": Pessoa.objects.all()
    }
    return render(
        request,
        'cadastro/mostrar.html',
        exibe_pessoas,
    )

def atualizar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.nome = request.POST.get('nome')
    pessoa.idade = request.POST.get('idade')
    pessoa.email = request.POST.get('email')
    pessoa.save()

    return exibe(request)

def editar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    return render(
        request,
        'cadastro/editar.html',
        {'pessoa': pessoa}
    )

def apagar(request, id):
    pessoa = Pessoa.objects.get(id_pessoa=id)
    pessoa.delete()

    return exibe(request)