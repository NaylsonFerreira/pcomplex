# Generated by Django 3.1.4 on 2021-02-07 20:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import storages.backends.ftp


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True,
                                        primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, null=True, unique=True)),
                ('nome', models.CharField(blank=True, max_length=50,
                                          null=True, verbose_name='Nome completo')),
                ('cpf', models.CharField(blank=True, max_length=50, null=True)),
                ('apelido', models.CharField(blank=True, max_length=50,
                                             null=True, verbose_name='Como gostaria de ser chamado?')),
                ('foto',
                 models.ImageField(blank=True,
                                   null=True,
                                   storage=storages.backends.ftp.FTPStorage(),
                                   upload_to='profiles/',
                                   verbose_name='Foto do perfil')),
                ('sobre', models.TextField(blank=True, null=True,
                                           verbose_name='Escreva algo sobre você')),
                ('whatsapp', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(
                    blank=True, max_length=100, null=True)),
                ('idade', models.IntegerField(blank=True,
                                              default=18, null=True, verbose_name='Idade')),
                ('genero',
                 models.CharField(blank=True,
                                  choices=[('M',
                                            'Masculino'),
                                           ('F',
                                            'Feminino')],
                                  default='M',
                                  max_length=10,
                                  null=True,
                                  verbose_name='Gênero')),
                ('user', models.OneToOneField(
                    on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
