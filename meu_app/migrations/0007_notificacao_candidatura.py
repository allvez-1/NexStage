from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0006_candidatura_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacaoCandidatura',
            fields=[
                ('id', models.BigAutoField(
                    auto_created=True,
                    primary_key=True,
                    serialize=False,
                    verbose_name='ID',
                )),
                ('status', models.CharField(
                    choices=[
                        ('analise', 'Em análise'),
                        ('aprovada', 'Aprovada'),
                        ('rejeitada', 'Rejeitada'),
                    ],
                    max_length=20,
                    verbose_name='status comunicado',
                )),
                ('criada_em', models.DateTimeField(
                    auto_now_add=True,
                    verbose_name='criada em',
                )),
                ('lida', models.BooleanField(default=False, verbose_name='lida')),
                ('candidatura', models.ForeignKey(
                    on_delete=django.db.models.deletion.CASCADE,
                    related_name='notificacoes',
                    to='meu_app.candidatura',
                )),
            ],
            options={
                'verbose_name': 'notificação de candidatura',
                'verbose_name_plural': 'notificações de candidaturas',
                'ordering': ['-criada_em'],
            },
        ),
    ]
