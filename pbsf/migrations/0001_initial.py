# Generated by Django 4.2.3 on 2023-08-10 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vacina',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('publico_alvo', models.CharField(choices=[('NE', 'Não Especificado'), ('A', 'Adulto'), ('C', 'Criança')], default='NE', max_length=2)),
            ],
        ),
    ]