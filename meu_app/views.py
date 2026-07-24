from django.shortcuts import get_object_or_404, redirect, render
from .models import Moto
from .forms import MotoForm

def home(request):
    return render(request, 'home.html')



def lista_motos(request):
    motos = Moto.objects.all()

    return render(request, 'lista.html', {
        'motos': motos
    })


def detalhe_moto(request, id):
    moto = get_object_or_404(Moto, id=id)

    return render(request, 'detalhe.html', {
        'moto': moto
    })


def criar_moto(request):
    form = MotoForm(request.POST or None)

    if form.is_valid():
        form.save()

        return redirect('lista_motos')

    return render(request, 'form.html', {
        'form': form
    })


def editar_moto(request, id):
    moto = get_object_or_404(Moto, id=id)

    form = MotoForm(request.POST or None, instance=moto)

    if form.is_valid():
        form.save()

        return redirect('lista_motos')

    return render(request, 'form.html', {
        'form': form
    })


def deletar_moto(request, id):
    moto = get_object_or_404(Moto, id=id)

    if request.method == 'POST':
        moto.delete()

        return redirect('lista_motos')

    return render(request, 'confirmar_delete.html', {
        'moto': moto
    })
