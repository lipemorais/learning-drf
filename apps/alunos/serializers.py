from rest_framework import serializers

from apps.alunos.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = '__all__'


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):

    serializer_curso = serializers.ReadOnlyField(source='curso.descricao')
    class Meta:
        model = Matricula
        fields = ['aluno', 'curso', 'periodo']
