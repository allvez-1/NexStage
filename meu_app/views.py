from django.contrib import messages
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import CandidaturaForm, VagaForm
from .models import Vaga


def home(request):
    vagas = Vaga.objects.filter(ativa=True)[:3]
    return render(request, 'index.html', {'vagas': vagas})


def lista_vagas(request):
    termo = request.GET.get('q', '').strip()
    vagas = Vaga.objects.filter(ativa=True)
    if termo:
        vagas = vagas.filter(
            Q(titulo__icontains=termo)
            | Q(empresa__icontains=termo)
            | Q(area__icontains=termo)
        )
    return render(request, 'vagas.html', {'vagas': vagas, 'termo': termo})


def detalhe_vaga(request, id):
    vaga = get_object_or_404(Vaga, id=id, ativa=True)
    return render(request, 'detalhe_vaga.html', {'vaga': vaga})


def publicar_vaga(request):
    form = VagaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Vaga publicada com sucesso. Ela já está disponível para candidatos.')
        return redirect('lista_vagas')
    return render(request, 'publicar_vaga.html', {'form': form})


def candidatar(request, id):
    vaga = get_object_or_404(Vaga, id=id, ativa=True)
    form = CandidaturaForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        candidatura = form.save(commit=False)
        candidatura.vaga = vaga
        candidatura.save()
        messages.success(request, 'Candidatura enviada. A empresa poderá entrar em contato pelo e-mail informado.')
        return redirect('detalhe_vaga', id=vaga.id)
    return render(request, 'candidatar.html', {'form': form, 'vaga': vaga})


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')
