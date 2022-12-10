# Generated by Django 4.1.4 on 2022-12-10 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_candidato', models.CharField(max_length=100, verbose_name='Nome:')),
                ('cpf_candidato', models.CharField(max_length=11, verbose_name='CPF:')),
                ('nasc_candidato', models.DateField(verbose_name='Data de nascimento: ')),
                ('email_candidato', models.EmailField(max_length=254, verbose_name='Email:')),
                ('endereco_candidato', models.CharField(max_length=255, verbose_name='Endereço:')),
                ('genero_candidato', models.CharField(blank=True, max_length=50, verbose_name='Sexo:')),
                ('curso_candidato', models.CharField(choices=[('Curso técnico', 'Curso técnico'), ('ADS', 'ADS')], max_length=50, verbose_name='Curso:')),
                ('mini_cursos', models.CharField(blank=True, max_length=100, verbose_name='Mini cursos')),
            ],
        ),
    ]
