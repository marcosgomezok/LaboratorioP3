# Generated by Django 4.2.5 on 2023-10-31 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0008_alter_alumno_analitico'),
        ('trabajoFinalApp', '0027_alter_tribunal_presidente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tribunal',
            name='presidente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='presidente', to='persona.docente'),
        ),
    ]