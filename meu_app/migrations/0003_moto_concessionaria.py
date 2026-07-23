# Generated for the motorcycle dealership CRUD.

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meu_app', '0002_produto_delete_post'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Produto',
            new_name='Moto',
        ),
        migrations.RenameField(
            model_name='moto',
            old_name='nome',
            new_name='modelo',
        ),
        migrations.AddField(
            model_name='moto',
            name='marca',
            field=models.CharField(default='Nao informada', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moto',
            name='ano',
            field=models.PositiveIntegerField(default=2026),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='moto',
            name='cor',
            field=models.CharField(default='Nao informada', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='moto',
            name='preco',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
