from django.shortcuts import render, redirect
from django.contrib import messages

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
