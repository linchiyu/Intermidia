from django.urls import include, path
from . import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('cadini', views.cadastroInicial, name='cadini'),
    path('api/', include([
        path('', views.index, name='index'),

        #API CAMERA
        path('cam/cad', views.CadCam.as_view(), name='cadastrar-camera'),
        path('cam/logon', views.ValidarCam.as_view(), name='gerar-token-camera'),

        path('cam/analise', views.AnaliseApi.as_view(), name='analise-facial'),

        #API ADMIN
        path('emp', views.EmpresaList.as_view(), name='empresas'),
        path('emp/<int:pk>', views.EmpresaAlter.as_view(), name='empresa-alter'),

        path('cam', views.CameraList.as_view(), name='cameras'),
        path('cam/<int:pk>', views.CameraAlter.as_view(), name='camera-alter'),
        path('cam/perm', views.PermissaoCamerasList.as_view(), name='cameras-novas'),

        path('dados', views.AnaliseList.as_view(), name='analises'),
    ])),
]