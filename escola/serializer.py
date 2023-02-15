from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

#É UM FILTRO DOS DADOS QUE A GENTE QUER DISPONIBILIZAR NA NOSSA API
# CONVERTE OS DADOS DA NOSSA API NO FORMATO JSON

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = '__all__'



class ListaMatriculaAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    def get_periodo(self, obj):
        return obj.get_periodo_display()

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    curso = serializers.ReadOnlyField(source='curso.descricao')
    class Meta:
        model = Matricula
        fields = ['aluno_nome', 'curso']


