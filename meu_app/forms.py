from django import forms

from .models import Candidatura, Vaga


class EstiloFormularioMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'campo-formulario'


class VagaForm(EstiloFormularioMixin, forms.ModelForm):
    class Meta:
        model = Vaga
        fields = [
            'empresa', 'titulo', 'area', 'descricao', 'requisitos', 'localizacao',
            'modalidade', 'carga_horaria', 'bolsa', 'prazo_candidatura',
        ]
        widgets = {
            'descricao': forms.Textarea(attrs={'rows': 5}),
            'requisitos': forms.Textarea(attrs={'rows': 4}),
            'prazo_candidatura': forms.DateInput(attrs={'type': 'date'}),
            'bolsa': forms.NumberInput(attrs={'step': '0.01', 'min': '0'}),
        }


class CandidaturaForm(EstiloFormularioMixin, forms.ModelForm):
    class Meta:
        model = Candidatura
        fields = ['nome', 'email', 'telefone', 'curso', 'curriculo', 'apresentacao']
        widgets = {'apresentacao': forms.Textarea(attrs={'rows': 5})}
