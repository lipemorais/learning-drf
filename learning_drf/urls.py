
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from apps.alunos import views

router = routers.DefaultRouter()
router.register(r"alunos", views.AlunosViewSet, basename="Alunos")
router.register(r"cursos", views.CursosViewSet, basename="Cursos")
router.register(r"matriculas", views.MatriculasViewSet, basename="Matriculas")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("aluno/<int:pk>/matriculas/", views.MatriculasAluno.as_view(), name="matriculas-aluno"),
]
