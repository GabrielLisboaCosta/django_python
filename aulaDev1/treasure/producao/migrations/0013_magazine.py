# Generated by Django 5.0 on 2024-04-16 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('producao', '0012_delete_article_delete_reporter'),
    ]

    operations = [
        migrations.CreateModel(
            name='Magazine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]