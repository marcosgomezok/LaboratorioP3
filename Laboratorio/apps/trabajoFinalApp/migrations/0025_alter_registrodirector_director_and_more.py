# Generated by Django 4.2.5 on 2023-10-31 06:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0008_alter_alumno_analitico'),
        ('trabajoFinalApp', '0024_remove_integrante_analitico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registrodirector',
            name='director',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_registro', to='persona.docente'),
        ),
        migrations.AlterField(
            model_name='registrodirector',
            name='proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_proyecto', to='trabajoFinalApp.proyecto'),
        ),
    ]