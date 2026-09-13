from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('meu_app', '0004_vaga_candidatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_fantasia', models.CharField(max_length=140, verbose_name='nome fantasia')),
                ('cnpj', models.CharField(blank=True, max_length=18, verbose_name='CNPJ')),
                ('descricao', models.TextField(blank=True, verbose_name='sobre a empresa')),
                ('telefone', models.CharField(blank=True, max_length=25, verbose_name='telefone')),
                ('endereco', models.CharField(blank=True, max_length=180, verbose_name='endereço')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='empresa', to=settings.AUTH_USER_MODEL)),
            ],
            options={'verbose_name': 'empresa', 'verbose_name_plural': 'empresas'},
        ),
        migrations.CreateModel(
            name='PerfilCandidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefone', models.CharField(blank=True, max_length=25, verbose_name='telefone')),
                ('curso', models.CharField(max_length=140, verbose_name='curso ou área de formação')),
                ('curriculo', models.FileField(blank=True, upload_to='curriculos/', verbose_name='currículo')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil_candidato', to=settings.AUTH_USER_MODEL)),
            ],
            options={'verbose_name': 'perfil de candidato', 'verbose_name_plural': 'perfis de candidatos'},
        ),
        migrations.RenameField(model_name='vaga', old_name='empresa', new_name='empresa_nome'),
        migrations.AddField(
            model_name='vaga',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vagas', to='meu_app.empresa'),
        ),
        migrations.AddField(
            model_name='candidatura',
            name='candidato',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='candidaturas', to='meu_app.perfilcandidato'),
        ),
    ]
