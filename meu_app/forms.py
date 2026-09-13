from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import Candidatura, Empresa, PerfilCandidato, Vaga


class EstiloFormularioMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'campo-formulario'


class LoginForm(EstiloFormularioMixin, AuthenticationForm):
    pass


class CadastroCandidatoForm(EstiloFormularioMixin, UserCreationForm):
    first_name = forms.CharField(label='Nome', max_length=150)
    last_name = forms.CharField(label='Sobrenome', max_length=150)
    email = forms.EmailField(label='E-mail')
    telefone = forms.CharField(label='Telefone', max_length=25)
    curso = forms.CharField(label='Curso ou área de formação', max_length=140)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'telefone', 'curso', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            PerfilCandidato.objects.create(usuario=user, telefone=self.cleaned_data['telefone'], curso=self.cleaned_data['curso'])
        return user


class CadastroEmpresaForm(EstiloFormularioMixin, UserCreationForm):
    email = forms.EmailField(label='E-mail corporativo')
    nome_fantasia = forms.CharField(label='Nome da empresa', max_length=140)
    cnpj = forms.CharField(label='CNPJ (opcional)', max_length=18, required=False)
    telefone = forms.CharField(label='Telefone', max_length=25, required=False)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('username', 'email', 'nome_fantasia', 'cnpj', 'telefone', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            Empresa.objects.create(usuario=user, nome_fantasia=self.cleaned_data['nome_fantasia'], cnpj=self.cleaned_data['cnpj'], telefone=self.cleaned_data['telefone'])
        return user


class PerfilCandidatoForm(EstiloFormularioMixin, forms.ModelForm):
    class Meta:
        model = PerfilCandidato
        fields = ['telefone', 'curso', 'curriculo']


class EmpresaForm(EstiloFormularioMixin, forms.ModelForm):
    class Meta:
        model = Empresa
        fields = ['nome_fantasia', 'cnpj', 'descricao', 'telefone', 'endereco']
        widgets = {'descricao': forms.Textarea(attrs={'rows': 4})}


class VagaForm(EstiloFormularioMixin, forms.ModelForm):
    class Meta:
        model = Vaga
        fields = ['titulo', 'area', 'descricao', 'requisitos', 'localizacao', 'modalidade', 'carga_horaria', 'bolsa', 'prazo_candidatura']
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5}),
            'requisitos': forms.Textarea(attrs={'rows': 4}),
            'prazo_candidatura': forms.DateInput(attrs={'type': 'date'}),
            'bolsa': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }


class CandidaturaForm(EstiloFormularioMixin, forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = ['apresentacao']
        widgets = {'apresentacao': forms.Textarea(attrs={'rows': 5})}
