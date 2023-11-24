from rest_framework import viewsets, generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from apps.alunos.models import Aluno, Curso, Matricula
from apps.alunos.serializers import (
    AlunoSerializer,
    CursoSerializer,
    MatriculaSerializer,
    ListaMatriculasAlunoSerializer,
    ListaMatriculasCursoSerializer
)


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    serializer_class = ListaMatriculasAlunoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['curso_id'])

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class MatriculasCurso(generics.ListAPIView):
    serializer_class = ListaMatriculasCursoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(curso_id=self.kwargs['curso_id'])

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
