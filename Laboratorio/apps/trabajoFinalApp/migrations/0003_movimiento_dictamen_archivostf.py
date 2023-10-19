# Generated by Django 4.2.5 on 2023-10-19 00:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabajoFinalApp', '0002_alter_proyecto_asesor_alter_proyecto_co_director_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_mov', models.DateField(blank=True, null=True)),
                ('fin_mov', models.DateField(blank=True, null=True)),
                ('tipo_mov', models.CharField(blank=True, max_length=200, null=True)),
                ('movimiento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='movimiento', to='trabajoFinalApp.proyecto')),
            ],
        ),
        migrations.CreateModel(
            name='Dictamen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resultado_dictamen', models.CharField(blank=True, max_length=200, null=True)),
                ('observacion', models.CharField(blank=True, max_length=2000, null=True)),
                ('dictamen_mov', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dictamen_mov', to='trabajoFinalApp.movimiento')),
            ],
        ),
        migrations.CreateModel(
            name='ArchivosTF',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivos_tf', models.FileField(blank=True, null=True, upload_to='')),
                ('archivo_mov', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='archivo_mov', to='trabajoFinalApp.movimiento')),
            ],
        ),
    ]
