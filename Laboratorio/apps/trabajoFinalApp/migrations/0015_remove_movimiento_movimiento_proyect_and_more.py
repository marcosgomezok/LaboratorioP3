# Generated by Django 4.2.5 on 2023-10-22 15:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabajoFinalApp', '0014_remove_cstf_cstf_proyecto_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movimiento',
            name='movimiento_proyect',
        ),
        migrations.AddField(
            model_name='movimiento',
            name='movimiento_proyecto',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movimiento_proyecto', to='trabajoFinalApp.proyecto'),
        ),
    ]
