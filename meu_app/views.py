from functools import wraps

from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render

from .forms import (
    CadastroCandidatoForm, CadastroEmpresaForm, CandidaturaForm, EmpresaForm,
    LoginForm, PerfilCandidatoForm, VagaForm,
)
from .models import Candidatura, Vaga


def candidato_required(view):
    @wraps(view)
    @login_required(login_url='login_candidato')
    def wrapped(request, *args, **kwargs):
        if not hasattr(request.user, 'perfil_candidato'):
            messages.error(request, 'Esta área é exclusiva para candidatos.')
            return redirect('login_candidato')
        return view(request, *args, **kwargs)
    return wrapped


def empresa_required(view):
    @wraps(view)
    @login_required(login_url='login_empresa')
    def wrapped(request, *args, **kwargs):
        if not hasattr(request.user, 'empresa'):
            messages.error(request, 'Esta área é exclusiva para empresas.')
            return redirect('login_empresa')
        return view(request, *args, **kwargs)
    return wrapped


def home(request):
    if request.user.is_authenticated and hasattr(request.user, 'empresa'):
        return redirect('painel_empresa')
    return render(request, 'index.html', {'vagas': Vaga.objects.filter(ativa=True).select_related('empresa')[:3]})


def lista_vagas(request):
    termo = request.GET.get('q', '').strip()
    vagas = Vaga.objects.filter(ativa=True).select_related('empresa')
    if termo:
        vagas = vagas.filter(Q(titulo__icontains=termo) | Q(empresa__nome_fantasia__icontains=termo) | Q(area__icontains=termo))
    return render(request, 'vagas.html', {'vagas': vagas, 'termo': termo})


def detalhe_vaga(request, id):
    return render(request, 'detalhe_vaga.html', {'vaga': get_object_or_404(Vaga.objects.select_related('empresa'), id=id, ativa=True)})


def login_por_perfil(request, perfil):
    if request.user.is_authenticated:
        return redirecionar_painel(request)
    form = LoginForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        usuario = form.get_user()
        perfil_do_usuario = 'empresa' if hasattr(usuario, 'empresa') else 'candidato' if hasattr(usuario, 'perfil_candidato') else 'administrador'
        if perfil_do_usuario != perfil:
            form.add_error(None, f'Esta conta é de {perfil_do_usuario}. Use a página de login correspondente.')
        else:
            login(request, usuario)
            return redirecionar_painel(request)
    titulo = 'Entrar como empresa' if perfil == 'empresa' else 'Entrar como candidato'
    return render(request, 'login.html', {'form': form, 'titulo': titulo, 'perfil': perfil})


def login_candidato(request):
    return login_por_perfil(request, 'candidato')


def login_empresa(request):
    return login_por_perfil(request, 'empresa')


def cadastro_candidato(request):
    form = CadastroCandidatoForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.save())
        messages.success(request, 'Cadastro realizado. Complete seu perfil e encontre oportunidades.')
        return redirect('painel_candidato')
    return render(request, 'cadastro.html', {'form': form, 'titulo': 'Crie sua conta de candidato', 'perfil': 'candidato'})


def cadastro_empresa(request):
    if request.user.is_authenticated:
        return redirecionar_painel(request)
    form = CadastroEmpresaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        login(request, form.save())
        messages.success(request, 'Empresa cadastrada. Agora você já pode publicar vagas.')
        return redirect('painel_empresa')
    return render(request, 'cadastro.html', {'form': form, 'titulo': 'Cadastre sua empresa', 'perfil': 'empresa'})


def sair(request):
    logout(request)
    messages.success(request, 'Você saiu da sua conta.')
    return redirect('home')


def redirecionar_painel(request):
    if request.user.is_staff:
        return redirect('admin:index')
    if hasattr(request.user, 'empresa'):
        return redirect('painel_empresa')
    if hasattr(request.user, 'perfil_candidato'):
        return redirect('painel_candidato')
    raise Http404('Perfil de usuário não configurado.')


@candidato_required
def painel_candidato(request):
    candidaturas = Candidatura.objects.filter(candidato=request.user.perfil_candidato).select_related('vaga', 'vaga__empresa')
    return render(request, 'painel_candidato.html', {'candidaturas': candidaturas})


@candidato_required
def detalhe_candidatura(request, id):
    candidatura = get_object_or_404(
        Candidatura.objects.select_related('vaga', 'vaga__empresa'),
        id=id,
        candidato=request.user.perfil_candidato,
    )
    return render(request, 'detalhe_candidatura.html', {'candidatura': candidatura})


@candidato_required
def editar_perfil_candidato(request):
    form = PerfilCandidatoForm(request.POST or None, request.FILES or None, instance=request.user.perfil_candidato)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Perfil atualizado com sucesso.')
        return redirect('painel_candidato')
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar perfil de candidato', 'botao': 'Salvar perfil'})


@candidato_required
def candidatar(request, id):
    vaga = get_object_or_404(Vaga, id=id, ativa=True)
    if not request.user.perfil_candidato.curriculo:
        messages.info(request, 'Envie seu currículo no perfil antes de se candidatar.')
        return redirect('editar_perfil_candidato')
    if Candidatura.objects.filter(vaga=vaga, candidato=request.user.perfil_candidato).exists():
        messages.info(request, 'Você já enviou uma candidatura para esta vaga.')
        return redirect('detalhe_vaga', id=vaga.id)
    form = CandidaturaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        candidatura = form.save(commit=False)
        candidatura.vaga = vaga
        candidatura.candidato = request.user.perfil_candidato
        candidatura.nome = request.user.get_full_name() or request.user.username
        candidatura.email = request.user.email
        candidatura.telefone = request.user.perfil_candidato.telefone
        candidatura.curso = request.user.perfil_candidato.curso
        candidatura.curriculo = request.user.perfil_candidato.curriculo
        candidatura.save()
        messages.success(request, 'Candidatura enviada. A empresa poderá entrar em contato pelo e-mail informado.')
        return redirect('painel_candidato')
    return render(request, 'candidatar.html', {'form': form, 'vaga': vaga})


@empresa_required
def painel_empresa(request):
    vagas = Vaga.objects.filter(empresa=request.user.empresa).prefetch_related('candidaturas')
    return render(request, 'painel_empresa.html', {'vagas': vagas})


@empresa_required
def editar_empresa(request):
    form = EmpresaForm(request.POST or None, instance=request.user.empresa)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Dados da empresa atualizados.')
        return redirect('painel_empresa')
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar perfil da empresa', 'botao': 'Salvar dados'})


@empresa_required
def publicar_vaga(request):
    form = VagaForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        vaga = form.save(commit=False)
        vaga.empresa = request.user.empresa
        vaga.empresa_nome = request.user.empresa.nome_fantasia
        vaga.save()
        messages.success(request, 'Vaga publicada com sucesso.')
        return redirect('painel_empresa')
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Publicar vaga de estágio', 'botao': 'Publicar vaga'})


def vaga_da_empresa(request, id):
    return get_object_or_404(Vaga, id=id, empresa=request.user.empresa)


@empresa_required
def editar_vaga(request, id):
    vaga = vaga_da_empresa(request, id)
    form = VagaForm(request.POST or None, instance=vaga)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, 'Vaga atualizada com sucesso.')
        return redirect('painel_empresa')
    return render(request, 'formulario.html', {'form': form, 'titulo': 'Editar vaga', 'botao': 'Salvar alterações'})


@empresa_required
def excluir_vaga(request, id):
    vaga = vaga_da_empresa(request, id)

    if request.method == 'POST':
        vaga.ativa = False
        vaga.save(update_fields=['ativa'])

        messages.success(request, 'Vaga desativada com sucesso.')
        return redirect('painel_empresa')

    return render(request, 'confirmar_exclusao.html', {'vaga': vaga})


@empresa_required
def candidatos_vaga(request, id):
    vaga = vaga_da_empresa(request, id)
    candidaturas = vaga.candidaturas.select_related('candidato', 'candidato__usuario')
    return render(request, 'candidatos_vaga.html', {'vaga': vaga, 'candidaturas': candidaturas})


@empresa_required
def atualizar_status_candidatura(request, id, status):
    if request.method != 'POST':
        raise Http404

    if status not in dict(Candidatura.STATUS_CHOICES):
        raise Http404

    candidatura = get_object_or_404(
        Candidatura.objects.select_related('vaga'),
        id=id,
        vaga__empresa=request.user.empresa,
    )
    candidatura.status = status
    candidatura.save(update_fields=['status'])
    messages.success(request, f'O status de {candidatura.nome} foi atualizado para {candidatura.get_status_display()}.')
    return redirect('candidatos_vaga', id=candidatura.vaga_id)


def sobre(request):
    return render(request, 'sobre.html')


def contato(request):
    return render(request, 'contato.html')
