# Generated by Django 5.0 on 2024-04-16 00:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0011_reporter_article'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
