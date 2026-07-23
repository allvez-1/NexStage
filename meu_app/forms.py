from django import forms
from .models import Moto

class MotoForm(forms.ModelForm):
    class Meta:
        model = Moto
        fields = ['marca', 'modelo', 'ano', 'cor', 'preco']
        labels = {
            'marca': 'Marca',
            'modelo': 'Modelo',
            'ano': 'Ano',
            'cor': 'Cor',
            'preco': 'Preço',
        }
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 ease block w-full rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none'}),
            'modelo': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 ease block w-full rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none'}),
            'ano': forms.NumberInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 ease block w-full rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none', 'min': 1900}),
            'cor': forms.TextInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 ease block w-full rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none'}),
            'preco': forms.NumberInput(attrs={'class': 'focus:shadow-primary-outline text-sm leading-5.6 ease block w-full rounded-lg border border-solid border-gray-300 bg-white bg-clip-padding px-3 py-2 font-normal text-gray-700 transition-all placeholder:text-gray-500 focus:border-blue-500 focus:outline-none', 'step': '0.01'}),
        }
