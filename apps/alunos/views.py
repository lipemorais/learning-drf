from rest_framework import viewsets, generics

from apps.alunos.models import Aluno, Curso, Matricula
from apps.alunos.serializers import AlunoSerializer, CursoSerializer, MatriculaSerializer, \
    ListaMatriculasAlunoSerializer


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer


class MatriculasViewSet(viewsets.ModelViewSet):
    """Exibindo todas as matrículas"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer


class MatriculasAluno(generics.ListAPIView):
    """Listando as matrículas de um aluno ou aluna"""
    serializer_class = ListaMatriculasAlunoSerializer

    def get_queryset(self):
        return Matricula.objects.filter(aluno_id=self.kwargs['pk'])
