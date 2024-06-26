# Generated by Django 5.0 on 2024-04-15 22:33

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='production',
            old_name='specs',
            new_name='especificacoes',
        ),
        migrations.RenameField(
            model_name='production',
            old_name='realease_date',
            new_name='lancamento',
        ),
        migrations.RemoveField(
            model_name='production',
            name='reviews',
        ),
        migrations.RemoveField(
            model_name='production',
            name='tredimenter',
        ),
        migrations.AddField(
            model_name='production',
            name='genero',
            field=models.CharField(choices=[('ACT', 'Ação'), ('ADV', 'Aventura'), ('HOR', 'Horor'), ('FIC', 'Ficção'), ('THR', 'Suspense'), ('WAR', 'Guerra')], default='ACT', max_length=3),
        ),
        migrations.AddField(
            model_name='production',
            name='nota',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
        migrations.AddField(
            model_name='production',
            name='populadidade',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(0)]),
        ),
        migrations.AddField(
            model_name='production',
            name='quantidade_avaliacoes',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinLengthValidator(1)]),
        ),
    ]
