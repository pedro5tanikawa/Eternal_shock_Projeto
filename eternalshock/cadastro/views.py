from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cadastro.models import Pessoa
from loja.models import Produto

# Create your views here.
def cadastro(request):
    contexto = {
        'title' : 'Eternal Shock | Cadastro'
    }
    return render(
        request,
        'cadastro/index.html',
        contexto,
    )

def gravar(request): #funçao para salvar os dados para a tabela
    # Se for GET, mostra o formulário
    if request.method == 'GET':
        return cadastro(request)
    
    # Se for POST, processa os dados
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        idade = request.POST.get('idade', '').strip()
        email = request.POST.get('email', '').strip()
        username = request.POST.get('username', '').strip()
        senha = request.POST.get('senha', '').strip()
        confirmacao_senha = request.POST.get('confirmacao_senha', '').strip()
        
        # Validação básica
        if not nome or not email or not username or not senha:
            contexto = {
                'title': 'Cadastro',
                'erro': 'Nome, Email, Usuário e Senha são obrigatórios!'
            }
            return render(request, 'cadastro/index.html', contexto)
        
        # Validar comprimento da senha
        if len(senha) < 6:
            contexto = {
                'title': 'Cadastro',
                'erro': 'A senha deve ter no mínimo 6 caracteres!'
            }
            return render(request, 'cadastro/index.html', contexto)
        
        # Validar se as senhas são iguais
        if senha != confirmacao_senha:
            contexto = {
                'title': 'Cadastro',
                'erro': 'As senhas não correspondem!'
            }
            return render(request, 'cadastro/index.html', contexto)
        
        # Validar se o username já existe
        if User.objects.filter(username=username).exists():
            contexto = {
                'title': 'Cadastro',
                'erro': 'Este usuário já existe!'
            }
            return render(request, 'cadastro/index.html', contexto)
        
        # Validar se o email já existe
        if User.objects.filter(email=email).exists():
            contexto = {
                'title': 'Cadastro',
                'erro': 'Este email já está cadastrado!'
            }
            return render(request, 'cadastro/index.html', contexto)
        
        try:
            # Criar User
            novo_user = User.objects.create_user(
                username=username,
                email=email,
                password=senha,
                first_name=nome
            )
            
            # Criar Pessoa vinculada ao User
            nova_pessoa = Pessoa()
            nova_pessoa.user = novo_user
            nova_pessoa.nome = nome
            nova_pessoa.idade = int(idade) if idade else 0
            nova_pessoa.email = email
            nova_pessoa.save()
            
            contexto = {
                'title': 'Cadastro',
                'sucesso': 'Cadastro realizado com sucesso! Agora você pode fazer login.'
            }
            return render(request, 'cadastro/index.html', contexto)
        except Exception as e:
            contexto = {
                'title': 'Cadastro',
                'erro': f'Erro ao salvar: {str(e)}'
            }
            return render(request, 'cadastro/index.html', contexto)

@login_required(login_url='/accounts/login/')
def perfil(request):
    """Exibe o perfil do usuário logado"""
    try:
        pessoa = Pessoa.objects.get(user=request.user)
    except Pessoa.DoesNotExist:
        # Se não houver Pessoa, redireciona para cadastro
        return redirect('cadastro:gravar')
    
    contexto = {
        'title': 'Meu Perfil',
        'pessoa': pessoa,
        'favoritos': pessoa.favoritos.all()
    }
    return render(request, 'cadastro/perfil.html', contexto)

@login_required(login_url='/accounts/login/')
def editar_perfil(request):
    """Permite editar foto de perfil"""
    try:
        pessoa = Pessoa.objects.get(user=request.user)
    except Pessoa.DoesNotExist:
        return redirect('cadastro:gravar')
    
    if request.method == 'POST':
        nome = request.POST.get('nome', '').strip()
        idade = request.POST.get('idade', '').strip()
        
        if nome:
            pessoa.nome = nome
            request.user.first_name = nome
            request.user.save()
        
        if idade:
            try:
                pessoa.idade = int(idade)
            except ValueError:
                pass
        
        if 'foto_perfil' in request.FILES:
            pessoa.foto_perfil = request.FILES['foto_perfil']
        
        pessoa.save()
        
        return redirect('cadastro:perfil')
    
    contexto = {
        'title': 'Editar Perfil',
        'pessoa': pessoa
    }
    return render(request, 'cadastro/editar_perfil.html', contexto)

@login_required(login_url='/accounts/login/')
def adicionar_favorito(request, produto_id):
    """Adiciona um produto aos favoritos"""
    try:
        pessoa = Pessoa.objects.get(user=request.user)
        produto = Produto.objects.get(id=produto_id)
        
        if pessoa.favoritos.filter(id=produto_id).exists():
            pessoa.favoritos.remove(produto)
        else:
            pessoa.favoritos.add(produto)
    except (Pessoa.DoesNotExist, Produto.DoesNotExist):
        pass
    
    return redirect('cadastro:perfil')

@login_required(login_url='/accounts/login/')
def remover_favorito(request, produto_id):
    """Remove um produto dos favoritos"""
    try:
        pessoa = Pessoa.objects.get(user=request.user)
        produto = Produto.objects.get(id=produto_id)
        pessoa.favoritos.remove(produto)
    except (Pessoa.DoesNotExist, Produto.DoesNotExist):
        pass
    
    return redirect('cadastro:perfil')

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