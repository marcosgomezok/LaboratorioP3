# Generated by Django 4.2.5 on 2023-10-25 03:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_persona_user'),
        ('trabajoFinalApp', '0015_remove_movimiento_movimiento_proyect_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miembro_titular',
            name='vocal_titular',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vocal_titular', to='persona.docente'),
        ),
    ]
