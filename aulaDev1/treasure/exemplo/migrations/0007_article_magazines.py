# Generated by Django 5.0 on 2024-04-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplo', '0006_reporter_article'),
        ('producao', '0013_magazine'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='magazines',
            field=models.ManyToManyField(to='producao.magazine'),
        ),
    ]
