from django.shortcuts import render

# Create your views here.

def home(request):
    contexto = {
        'title' : 'Eternal Shock | Cadastro'
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