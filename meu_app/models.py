from django.db import models


class Vaga(models.Model):
    MODALIDADES = [
        ('presencial', 'Presencial'),
        ('hibrido', 'Híbrido'),
        ('remoto', 'Remoto'),
    ]

    empresa = models.CharField('empresa', max_length=120)
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
