
from rest_framework import viewsets, generics,filters
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculaAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    search_fields = ['id', 'nome','data_nascimento']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['nivel']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class MatriculasViewSet(viewsets.ModelViewSet):
    """Listando todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['periodo']
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculaAlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

class ListaAlunoMatriculado(generics.ListAPIView):
    """Listando os alunos matriculados"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


