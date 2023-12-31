# Generated by Django 4.2.7 on 2023-11-18 16:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("alunos", "0002_alter_aluno_data_nascimento"),
    ]

    operations = [
        migrations.CreateModel(
            name="Matricula",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "periodo",
                    models.CharField(
                        choices=[
                            ("M", "Matutino"),
                            ("V", "Vespertino"),
                            ("N", "Noturno"),
                        ],
                        default="M",
                        max_length=1,
                    ),
                ),
                (
                    "aluno",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="alunos.aluno"
                    ),
                ),
                (
                    "curso",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="alunos.curso"
                    ),
                ),
            ],
        ),
    ]
