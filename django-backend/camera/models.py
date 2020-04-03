from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
# Create your models here.
#https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html

def images_path():
    return os.path.join(settings.LOCAL_FILE_DIR, 'images')

class Empresa(models.Model):
    class Meta:
        db_table = 'empresa'

    razaosocial = models.CharField(max_length=40)
    cnpj = models.CharField(max_length=20, blank=True, null=True)
    endereco = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField()
    telefone = models.CharField(max_length=20, blank=True, null=True)
    dataatualizacao = models.DateTimeField(auto_now=True)
    usuarios = models.ManyToManyField(User, verbose_name="lista de usuarios")

    def __str__(self):
        return self.razaosocial

class Local(models.Model):
    class Meta:
        db_table = 'local'

    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    datacriacao = models.DateTimeField(auto_now_add=True)
    dataatualizacao = models.DateTimeField(blank=True, null=True)
    ultimoregistro = models.IntegerField(default=0)
    m_jovem = models.IntegerField(default=0)
    m_adulto = models.IntegerField(default=0)
    m_idoso = models.IntegerField(default=0)
    f_jovem = models.IntegerField(default=0)
    f_adulto = models.IntegerField(default=0)
    f_idoso = models.IntegerField(default=0)

    def __str__(self):
        return self.nome

class Camera(models.Model):
    class Meta:
        db_table = 'camera'

    nome = models.CharField(max_length=40)
    descricao = models.CharField(max_length=200, blank=True, null=True)
    #chave = models.CharField(max_length=100, blank=True, null=True)
    ativo = models.BooleanField(default=False)
    permissao = models.BooleanField(null=True)
    status = models.BooleanField(default=False)
    #path = models.FilePathField(path=images_path,
    #                            recursive=True, blank=True, null=True)
    datacadastro = models.DateTimeField(auto_now_add=True)
    dataativacao = models.DateTimeField(blank=True, null=True)
    datadesativacao = models.DateTimeField(blank=True, null=True)
    chave = models.ForeignKey(User, on_delete=models.PROTECT, null=True)
    local = models.ForeignKey(Local, on_delete=models.PROTECT, null=True)
    fkempresa = models.ForeignKey(Empresa, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.nome



class Analise(models.Model):
    class Meta:
        db_table = 'analise'

    data = models.DateTimeField()
    tempoatt = models.FloatField()
    idade = models.SmallIntegerField()
    sexo = models.CharField(max_length=1)
    datarecepcao = models.DateTimeField(auto_now_add=True)
    fkcamera = models.ForeignKey(Camera, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.sexo, self.idade
