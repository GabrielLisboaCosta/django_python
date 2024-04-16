# Generated by Django 5.0 on 2024-04-16 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exemplo', '0007_article_magazines'),
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
        migrations.AlterField(
            model_name='article',
            name='magazines',
            field=models.ManyToManyField(to='exemplo.magazine'),
        ),
    ]
