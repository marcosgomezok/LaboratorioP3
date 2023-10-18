# Generated by Django 4.2.5 on 2023-10-18 21:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0002_alter_asesor_cv_asesor'),
        ('trabajoFinalApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proyecto',
            name='asesor',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='asesor', to='persona.asesor'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='co_director',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='co_director', to='persona.docente'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='director',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='director', to='persona.docente'),
        ),
        migrations.AlterField(
            model_name='tribunal',
            name='presidente',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='persona.docente'),
        ),
        migrations.CreateModel(
            name='RegistroDirector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alta_proyecto', models.DateField(blank=True, null=True)),
                ('baja_proyecto', models.DateField(blank=True, null=True)),
                ('director', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_registro', to='persona.docente')),
                ('proyecto', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director_proyecto', to='trabajoFinalApp.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Integrante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alta_proyecto', models.DateField(blank=True, null=True)),
                ('baja_proyecto', models.DateField(blank=True, null=True)),
                ('analitico', models.FileField(blank=True, null=True, upload_to='')),
                ('alumno', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='integrante_alumno', to='persona.alumno')),
                ('proyecto', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='integrante_proyecto', to='trabajoFinalApp.proyecto')),
            ],
        ),
    ]
