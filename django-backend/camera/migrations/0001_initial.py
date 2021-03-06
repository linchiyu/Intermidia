# Generated by Django 3.0.5 on 2020-04-02 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(blank=True, max_length=200, null=True)),
                ('datacriacao', models.DateTimeField(auto_now_add=True)),
                ('dataatualizacao', models.DateTimeField(blank=True, null=True)),
                ('ultimoregistro', models.IntegerField(default=0)),
                ('m_jovem', models.IntegerField(default=0)),
                ('m_adulto', models.IntegerField(default=0)),
                ('m_idoso', models.IntegerField(default=0)),
                ('f_jovem', models.IntegerField(default=0)),
                ('f_adulto', models.IntegerField(default=0)),
                ('f_idoso', models.IntegerField(default=0)),
            ],
            options={
                'db_table': 'local',
            },
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('razaosocial', models.CharField(max_length=40)),
                ('cnpj', models.CharField(blank=True, max_length=20, null=True)),
                ('endereco', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('telefone', models.CharField(blank=True, max_length=20, null=True)),
                ('dataatualizacao', models.DateTimeField(auto_now=True)),
                ('usuarios', models.ManyToManyField(to=settings.AUTH_USER_MODEL, verbose_name='lista de usuarios')),
            ],
            options={
                'db_table': 'empresa',
            },
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=40)),
                ('descricao', models.CharField(blank=True, max_length=200, null=True)),
                ('ativo', models.BooleanField(default=False)),
                ('permissao', models.BooleanField(null=True)),
                ('status', models.BooleanField(default=False)),
                ('path', models.FilePathField(blank=True, default='', null=True, recursive=True)),
                ('datacadastro', models.DateTimeField(auto_now_add=True)),
                ('dataativacao', models.DateTimeField(blank=True, null=True)),
                ('datadesativacao', models.DateTimeField(blank=True, null=True)),
                ('chave', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
                ('fkempresa', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='camera.Empresa')),
                ('local', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='camera.Local')),
            ],
            options={
                'db_table': 'camera',
            },
        ),
        migrations.CreateModel(
            name='Analise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField()),
                ('tempoatt', models.FloatField()),
                ('idade', models.SmallIntegerField()),
                ('sexo', models.CharField(max_length=1)),
                ('datarecepcao', models.DateTimeField(auto_now_add=True)),
                ('fkcamera', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='camera.Camera')),
            ],
            options={
                'db_table': 'analise',
            },
        ),
    ]
