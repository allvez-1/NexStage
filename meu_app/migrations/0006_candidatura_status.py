from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0005_auth_profiles_and_empresa'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidatura',
            name='status',
            field=models.CharField(
                choices=[('analise', 'Em análise'), ('aprovada', 'Aprovada'), ('rejeitada', 'Rejeitada')],
                default='analise',
                max_length=20,
                verbose_name='status',
            ),
        ),
    ]
