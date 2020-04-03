from django.shortcuts import render
from rest_framework import generics
from .models import Empresa, Camera, Analise
from .serializers import EmpresaSerializer
from .serializers import AnaliseSerializer
from .serializers import CameraSerializer, CameraViewSerializer
from .usecase import cadastraUsuarioSenhaCamera
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.authentication import TokenAuthentication
from rest_framework import status
from rest_framework import viewsets, permissions
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from django.contrib.auth.models import Group, Permission
from rest_framework.authtoken.views import obtain_auth_token
from datetime import datetime
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import viewsets


#rodar uma única vez ao inicializar o banco de dados para cadastrar dados iniciais
def cadastroInicial(request):

    try:
        validacao = Group.objects.get(name='ADMINS')
        return HttpResponse("Cadastro inicial já foi realizado anteriormente! Reinicie o banco de dados caso desejar realizar novo cadastro!")
    except:
        None


    #cadastrar empresa
    new_empresa, created = Empresa.objects.get_or_create(razaosocial='empresa teste', email='teste@teste.com')

    new_empresa.save()
    #cadastrar superuser

    #cadastrar grupo admin com todas as permissões
    new_group, created = Group.objects.get_or_create(name='ADMINS')
    proj_add_perm = Permission.objects.all()

    for i in proj_add_perm:
        new_group.permissions.add(i)
    new_group.save()

    new_group, created = Group.objects.get_or_create(name='CAMERAS_API')
    proj_add_perm = Permission.objects.get(codename='add_analise')
    new_group.permissions.add(proj_add_perm)
    '''proj_add_perm = Permission.objects.get(codename='add_token')
    new_group.permissions.add(proj_add_perm)
    proj_add_perm = Permission.objects.get(codename='view_token')
    new_group.permissions.add(proj_add_perm)'''
    new_group.save()

    return HttpResponse("Cadastro inicial realizado com sucesso!")



# Create your views here.
def index(request):
    print(request.headers)
    return HttpResponse("Welcome to API.")


#==============================================
# API do ADMINISTRADOR
#==============================================
class EmpresaList(generics.ListCreateAPIView):
    queryset = Empresa.objects.all().order_by('-id')
    serializer_class = EmpresaSerializer
    permission_classes = [IsAdminUser]

class EmpresaAlter(generics.RetrieveUpdateDestroyAPIView):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer
    permission_classes = [IsAdminUser]

class CameraList(generics.ListAPIView):
    queryset = Camera.objects.exclude(permissao=None).order_by('-id')
    serializer_class = CameraSerializer
    permission_classes = [IsAdminUser]

class CameraAlter(generics.RetrieveUpdateAPIView):
    queryset = Camera.objects.all()
    serializer_class = CameraSerializer
    permission_classes = [IsAdminUser]

class PermissaoCamerasList(generics.ListAPIView):
    queryset = Camera.objects.filter(permissao=None).order_by('-id')
    serializer_class = CameraViewSerializer
    permission_classes = [IsAdminUser]

class AnaliseList(generics.ListAPIView):
    queryset = Analise.objects.all().order_by('-id')
    serializer_class = AnaliseSerializer
    permission_classes = [IsAdminUser]


#==============================================
# API da CAMERA
#==============================================
class AnaliseApi(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]

    #salvar lista de analises
    def post(self, request, format=None):
        print(request.data)
        user = User.objects.get(username=request.user)

        if not user.has_perm('camera.add_analise'):
            return Response(status=status.HTTP_401_UNAUTHORIZED)

        camera = Camera.objects.get(chave=user)
        camera.status = True
        camera.save()

        serializer = AnaliseSerializer(data=request.data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#api para identificar nova camera
class CadCam(APIView):

    def post(self, request, format=None):
        serializer = CameraSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = cadastraUsuarioSenhaCamera(request.data['nome'])
            serializer.save(chave=user)
            return Response({"username": user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


#camera irá aguardar para conseguir token de autenticação
class ValidarCam(ObtainAuthToken):

    def post(self, request, *args, **kwargs):

        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        camera = Camera.objects.get(chave=user)
        if (camera.permissao == None):
            return Response({'err': 'Aguarde aprovação de um administrador.'}, 
                status=status.HTTP_401_UNAUTHORIZED)
        elif (camera.permissao == False):
            return Response({'err': 'Camera recusada, solicite novo acesso ao administrador.'}, 
                status=status.HTTP_401_UNAUTHORIZED)
        token, created = Token.objects.get_or_create(user=user)

        if created:
            camera.dataativacao = str(datetime.now())
            camera.ativo = True
            camera.save()
        return Response({'token': token.key})


#===========================================
# API do USUÁRIO
#===========================================