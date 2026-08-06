from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0003_moto_concessionaria'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaga',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=120, verbose_name='empresa')),
                ('titulo', models.CharField(max_length=140, verbose_name='título da vaga')),
                ('area', models.CharField(max_length=100, verbose_name='área de atuação')),
                ('descricao', models.TextField(verbose_name='descrição')),
                ('requisitos', models.TextField(blank=True, verbose_name='requisitos')),
                ('localizacao', models.CharField(default='Guanambi - BA', max_length=120, verbose_name='localização')),
                ('modalidade', models.CharField(choices=[('presencial', 'Presencial'), ('hibrido', 'Híbrido'), ('remoto', 'Remoto')], default='presencial', max_length=12, verbose_name='modalidade')),
                ('carga_horaria', models.CharField(blank=True, max_length=80, verbose_name='carga horária')),
                ('bolsa', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='bolsa-auxílio')),
                ('prazo_candidatura', models.DateField(verbose_name='prazo para candidatura')),
                ('criado_em', models.DateTimeField(auto_now_add=True, verbose_name='publicada em')),
                ('ativa', models.BooleanField(default=True, verbose_name='vaga ativa')),
            ],
            options={'verbose_name': 'vaga', 'verbose_name_plural': 'vagas', 'ordering': ['-criado_em']},
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=140, verbose_name='nome completo')),
                ('email', models.EmailField(max_length=254, verbose_name='e-mail')),
                ('telefone', models.CharField(max_length=25, verbose_name='telefone')),
                ('curso', models.CharField(max_length=140, verbose_name='curso ou área de formação')),
                ('curriculo', models.FileField(upload_to='curriculos/', verbose_name='currículo')),
                ('apresentacao', models.TextField(blank=True, verbose_name='mensagem de apresentação')),
                ('criada_em', models.DateTimeField(auto_now_add=True, verbose_name='candidatura enviada em')),
                ('vaga', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidaturas', to='meu_app.vaga')),
            ],
            options={'verbose_name': 'candidatura', 'verbose_name_plural': 'candidaturas', 'ordering': ['-criada_em']},
        ),
    ]
