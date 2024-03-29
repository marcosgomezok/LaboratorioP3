# Generated by Django 4.2.5 on 2023-10-19 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trabajoFinalApp', '0004_alter_dictamen_resultado_dictamen_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictamen',
            name='resultado_dictamen',
            field=models.CharField(blank=True, choices=[('aceptado', 'Aceptado'), ('rechazado', 'Rechazado'), ('observado', 'Observado')], max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='movimiento',
            name='tipo_mov',
            field=models.CharField(blank=True, choices=[('proyecto_presentado', 'Proyecto Presentado'), ('evaluacion_cstf', 'Proyecto en Evaluación por CSTF'), ('evaluacion_tribunal', 'Proyecto en Evaluación por Tribunal'), ('evaluacion_borrador', 'Borrador en Evaluación por el Tribunal'), ('evaluacion_final', 'Defensa del Trabajo Final')], max_length=200, null=True),
        ),
    ]
