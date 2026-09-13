from django.conf import settings
from django.db import models


class PerfilCandidato(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='perfil_candidato')
    telefone = models.CharField('telefone', max_length=25, blank=True)
    curso = models.CharField('curso ou área de formação', max_length=140)
    curriculo = models.FileField('currículo', upload_to='curriculos/', blank=True)

    class Meta:
        verbose_name = 'perfil de candidato'
        verbose_name_plural = 'perfis de candidatos'

    def __str__(self):
        return self.usuario.get_full_name() or self.usuario.username


class Empresa(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='empresa')
    nome_fantasia = models.CharField('nome fantasia', max_length=140)
    cnpj = models.CharField('CNPJ', max_length=18, blank=True)
    descricao = models.TextField('sobre a empresa', blank=True)
    telefone = models.CharField('telefone', max_length=25, blank=True)
    endereco = models.CharField('endereço', max_length=180, blank=True)

    class Meta:
        verbose_name = 'empresa'
        verbose_name_plural = 'empresas'

    def __str__(self):
        return self.nome_fantasia


class Vaga(models.Model):
    MODALIDADES = [
        ('presencial', 'Presencial'),
        ('hibrido', 'Híbrido'),
        ('remoto', 'Remoto'),
    ]

    empresa_nome = models.CharField('empresa', max_length=120, blank=True)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name='vagas', null=True, blank=True)
    titulo = models.CharField('título da vaga', max_length=140)
    area = models.CharField('área de atuação', max_length=100)
    descricao = models.TextField('descrição')
    requisitos = models.TextField('requisitos', blank=True)
    localizacao = models.CharField('localização', max_length=120, default='Guanambi - BA')
    modalidade = models.CharField('modalidade', max_length=12, choices=MODALIDADES, default='presencial')
    carga_horaria = models.CharField('carga horária', max_length=80, blank=True)
    bolsa = models.DecimalField('bolsa-auxílio', max_digits=8, decimal_places=2, null=True, blank=True)
    prazo_candidatura = models.DateField('prazo para candidatura')
    criado_em = models.DateTimeField('publicada em', auto_now_add=True)
    ativa = models.BooleanField('vaga ativa', default=True)

    class Meta:
        ordering = ['-criado_em']
        verbose_name = 'vaga'
        verbose_name_plural = 'vagas'

    def __str__(self):
        return f'{self.titulo} - {self.empresa}'


class Candidatura(models.Model):
    vaga = models.ForeignKey(Vaga, on_delete=models.CASCADE, related_name='candidaturas')
    candidato = models.ForeignKey(PerfilCandidato, on_delete=models.CASCADE, related_name='candidaturas', null=True, blank=True)
    nome = models.CharField('nome completo', max_length=140)
    email = models.EmailField('e-mail')
    telefone = models.CharField('telefone', max_length=25)
    curso = models.CharField('curso ou área de formação', max_length=140)
    curriculo = models.FileField('currículo', upload_to='curriculos/')
    apresentacao = models.TextField('mensagem de apresentação', blank=True)
    criada_em = models.DateTimeField('candidatura enviada em', auto_now_add=True)

    class Meta:
        ordering = ['-criada_em']
        verbose_name = 'candidatura'
        verbose_name_plural = 'candidaturas'

    def __str__(self):
        return f'{self.nome} - {self.vaga}'
