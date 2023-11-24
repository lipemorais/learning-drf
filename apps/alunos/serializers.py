from rest_framework import serializers

from apps.alunos.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.ReadOnlyField(source='get_periodo_display')
    class Meta:
        model = Matricula
        fields = ["aluno_nome", "curso", "periodo"]


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['aluno', 'curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    periodo = serializers.ReadOnlyField(source='get_periodo_display')

    class Meta:
        model = Matricula
        fields = ['aluno', "aluno_nome", "periodo"]
