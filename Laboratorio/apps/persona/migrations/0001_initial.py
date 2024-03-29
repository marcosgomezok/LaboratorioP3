# Generated by Django 4.2.5 on 2023-10-18 08:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('dni', models.CharField(max_length=8, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona')),
                ('mu', models.CharField(max_length=200, unique=True)),
                ('email', models.CharField(max_length=200)),
            ],
            bases=('persona.persona',),
        ),
        migrations.CreateModel(
            name='Asesor',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona')),
                ('cv_asesor', models.FileField(upload_to='')),
            ],
            bases=('persona.persona',),
        ),
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('persona_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='persona.persona')),
                ('cuil', models.CharField(max_length=200, unique=True)),
            ],
            bases=('persona.persona',),
        ),
    ]
