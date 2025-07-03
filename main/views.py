from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .models import empresa, unidade, lancamento
from links.models import Link

# Create your views here.

def home(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')
        
        messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')
        return redirect('home')
    
    return render(request, 'home.html')

def contato(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        mensagem = request.POST.get('mensagem')

        messages.success(request, 'Mensagem enviada com sucesso! Entraremos em contato em breve.')

    
    return render(request, 'home.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('main:dashboard')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bem-vindo, {user.username}!')
                return redirect('main:dashboard')
            else:
                messages.error(request, 'Usuário ou senha inválidos.')
        else:
            messages.error(request, 'Por favor, corrija os erros abaixo.')
    else:
        form = AuthenticationForm()
    
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Você foi desconectado com sucesso.')
    return redirect('main:home')

@login_required
def dashboard(request):
    # Estatísticas básicas
    context = {
        'empresas_count': empresa.objects.count(),
        'unidades_count': unidade.objects.count(),
        'lancamentos_count': lancamento.objects.count(),
        'links_count': Link.objects.count(),
        'recent_links': Link.objects.select_related('empresa').order_by('-id')[:5],
    }
    return render(request, 'main/dashboard.html', context)
