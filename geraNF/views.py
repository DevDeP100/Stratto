from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from .models import Tomador
from .forms import TomadorForm
from main.models import AcessoEmpresa

# Create your views here.

@login_required
def lista_tomadores(request):
    # Versão temporária para teste
    try:
        # Tentar pegar a empresa do usuário
        acesso_empresa = AcessoEmpresa.objects.filter(usuario=request.user).first()
        
        if acesso_empresa and acesso_empresa.unidade and acesso_empresa.unidade.empresa:
            # Usuário tem acesso a uma empresa
            empresa_usuario = acesso_empresa.unidade.empresa
            tomadores = Tomador.objects.filter(empresa=empresa_usuario).order_by('-created_at')
        else:
            # Usuário não tem acesso a empresa, mostrar todos os tomadores (apenas para teste)
            tomadores = Tomador.objects.all().order_by('-created_at')
            messages.warning(request, 'Você não tem acesso a uma empresa específica. Mostrando todos os tomadores.')
        
        return render(request, 'geraNF/lista_tomadores.html', {'tomadores': tomadores})
        
    except Exception as e:
        print(f"Erro na view lista_tomadores: {str(e)}")
        messages.error(request, f'Erro ao carregar tomadores: {str(e)}')
        return redirect('main:dashboard')

@login_required
def cadastrar_tomador(request):
    # Pegar a empresa do usuário logado através da unidade
    try:
        acesso_empresa = AcessoEmpresa.objects.filter(usuario=request.user).first()
        if not acesso_empresa or not acesso_empresa.unidade:
            messages.error(request, 'Você não tem acesso a nenhuma empresa.')
            return redirect('geraNF:lista_tomadores')
        
        empresa_usuario = acesso_empresa.unidade.empresa
        if not empresa_usuario:
            messages.error(request, 'A unidade não está associada a uma empresa.')
            return redirect('geraNF:lista_tomadores')
    except Exception as e:
        messages.error(request, 'Erro ao acessar informações da empresa.')
        return redirect('geraNF:lista_tomadores')

    if request.method == 'POST':
        form = TomadorForm(request.POST)
        if form.is_valid():
            tomador = form.save(commit=False)
            tomador.empresa = empresa_usuario  # Definir empresa automaticamente
            tomador.created_by = request.user
            tomador.updated_by = request.user
            tomador.save()
            messages.success(request, 'Tomador cadastrado com sucesso!')
            return redirect('geraNF:lista_tomadores')
    else:
        form = TomadorForm()
    
    return render(request, 'geraNF/cadastrar_tomador.html', {
        'form': form, 
        'empresa_usuario': empresa_usuario
    })

@login_required
def visualizar_tomador(request, tomador_id):
    # Verificar se o usuário tem acesso ao tomador através da empresa
    try:
        acesso_empresa = AcessoEmpresa.objects.filter(usuario=request.user).first()
        if not acesso_empresa or not acesso_empresa.unidade or not acesso_empresa.unidade.empresa:
            messages.error(request, 'Você não tem acesso a nenhuma empresa.')
            return redirect('geraNF:lista_tomadores')
        
        empresa_usuario = acesso_empresa.unidade.empresa
        tomador = get_object_or_404(Tomador, id=tomador_id, empresa=empresa_usuario)
    except Exception as e:
        messages.error(request, 'Erro ao acessar informações da empresa.')
        return redirect('geraNF:lista_tomadores')
    
    return render(request, 'geraNF/visualizar_tomador.html', {'tomador': tomador})

@login_required
def editar_tomador(request, tomador_id):
    # Verificar se o usuário tem acesso ao tomador através da empresa
    try:
        acesso_empresa = AcessoEmpresa.objects.filter(usuario=request.user).first()
        if not acesso_empresa or not acesso_empresa.unidade or not acesso_empresa.unidade.empresa:
            messages.error(request, 'Você não tem acesso a nenhuma empresa.')
            return redirect('geraNF:lista_tomadores')
        
        empresa_usuario = acesso_empresa.unidade.empresa
        tomador = get_object_or_404(Tomador, id=tomador_id, empresa=empresa_usuario)
    except Exception as e:
        messages.error(request, 'Erro ao acessar informações da empresa.')
        return redirect('geraNF:lista_tomadores')
    
    if request.method == 'POST':
        form = TomadorForm(request.POST, instance=tomador)
        if form.is_valid():
            tomador = form.save(commit=False)
            tomador.updated_by = request.user
            tomador.save()
            messages.success(request, 'Tomador atualizado com sucesso!')
            return redirect('geraNF:lista_tomadores')
    else:
        form = TomadorForm(instance=tomador)
    return render(request, 'geraNF/editar_tomador.html', {'form': form, 'tomador': tomador})

@login_required
def remover_tomador(request, tomador_id):
    # Verificar se o usuário tem acesso ao tomador através da empresa
    try:
        acesso_empresa = AcessoEmpresa.objects.filter(usuario=request.user).first()
        if not acesso_empresa or not acesso_empresa.unidade or not acesso_empresa.unidade.empresa:
            messages.error(request, 'Você não tem acesso a nenhuma empresa.')
            return redirect('geraNF:lista_tomadores')
        
        empresa_usuario = acesso_empresa.unidade.empresa
        tomador = get_object_or_404(Tomador, id=tomador_id, empresa=empresa_usuario)
    except Exception as e:
        messages.error(request, 'Erro ao acessar informações da empresa.')
        return redirect('geraNF:lista_tomadores')
    
    if request.method == 'POST':
        nome_tomador = tomador.nome
        tomador.delete()
        messages.success(request, f'Tomador "{nome_tomador}" removido com sucesso!')
        return redirect('geraNF:lista_tomadores')
    return render(request, 'geraNF/remover_tomador.html', {'tomador': tomador})

@login_required
def gerar_nf(request):
    """View para gerar notas fiscais"""
    try:
        # Pegar a empresa do usuário
        acesso_empresa = AcessoEmpresa.objects.filter(usuario=request.user).first()
        
        if acesso_empresa and acesso_empresa.unidade and acesso_empresa.unidade.empresa:
            empresa_usuario = acesso_empresa.unidade.empresa
            tomadores = Tomador.objects.filter(empresa=empresa_usuario).order_by('nome')
        else:
            tomadores = Tomador.objects.all().order_by('nome')
            messages.warning(request, 'Você não tem acesso a uma empresa específica.')
        
        context = {
            'tomadores': tomadores,
            'empresa_usuario': empresa_usuario if acesso_empresa and acesso_empresa.unidade and acesso_empresa.unidade.empresa else None
        }
        
        return render(request, 'geraNF/gerar_nf.html', context)
        
    except Exception as e:
        messages.error(request, f'Erro ao carregar dados para geração de NF: {str(e)}')
        return redirect('main:dashboard')
