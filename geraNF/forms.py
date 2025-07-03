from django import forms
from .models import Tomador

class TomadorForm(forms.ModelForm):
    class Meta:
        model = Tomador
        fields = [
            'nome', 'cpf_cnpj', 'inscricao_estadual', 'inscricao_municipal',
            'email', 'telefone', 'endereco', 'numero', 'complemento', 'bairro',
            'cidade', 'uf', 'cep'
        ]
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome completo'}),
            'cpf_cnpj': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apenas números'}),
            'inscricao_estadual': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inscrição Estadual'}),
            'inscricao_municipal': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Inscrição Municipal'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'email@exemplo.com'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apenas números'}),
            'endereco': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Rua, Avenida, etc.'}),
            'numero': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Número'}),
            'complemento': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apartamento, sala, etc.'}),
            'bairro': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Bairro'}),
            'cidade': forms.Select(attrs={'class': 'form-select'}),
            'uf': forms.Select(attrs={'class': 'form-select'}),
            'cep': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apenas números'}),
        } 