# Generated by Django 5.0 on 2024-04-15 23:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exemplo', '0004_person_alter_passaport_ower'),
        ('producao', '0004_delete_passaport'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]
