#business logic
#idea extracted from https://medium.com/@jairvercosa/business-logic-in-django-projects-7fe700db9b0a
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from .models import Camera
import secrets
import hashlib


def cadastraUsuarioSenhaCamera(nome):
    grupo = Group.objects.get(name='CAMERAS_API')

    usuario = secrets.token_hex(3)
    #passw = username + his reverse
    senha = hashlib.md5((usuario+nome).encode()).hexdigest()

    user = User(username=usuario)
    user.set_password(senha)
    user.is_active = False
    user.save()
    user.groups.add(grupo)
    user.save()

    return user

def liberarPermissaoCamera(idCamera):
    camera = Camera.objects.get(id=idCamera)
    user = User.objects.get(username=camera.chave)
    camera.permissao = True
    user.is_active = True

    return True

def bloquearPermissaoCamera():
    camera = Camera.objects.get(id=idCamera)
    user = User.objects.get(username=camera.chave)
    camera.permissao = False
    user.is_active = False

    return True
