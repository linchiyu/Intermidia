from rest_framework import serializers
from .models import Empresa
from .models import Analise
from .models import Camera

class EmpresaSerializer(serializers.ModelSerializer):

    class Meta:

        model = Empresa
        fields = '__all__'
        #fields = ('cnpj', 'razaosocial')
        #read_only_fields = ( 'cnpj' ,)


class AnaliseSerializer(serializers.ModelSerializer):

    class Meta:

        model = Analise
        fields = '__all__'
        #fields = ('cnpj', 'razaosocial')
        #read_only_fields = ( 'cnpj' ,)


class CameraSerializer(serializers.ModelSerializer):

    class Meta:

        model = Camera
        fields = '__all__'


class CameraViewSerializer(serializers.ModelSerializer):
    class Meta:

        model = Camera
        fields = ['id', 'nome', 'descricao', 'ativo', 'status', 'datacadastro',
            'dataativacao', 'datadesativacao', 'local', 'fkempresa']