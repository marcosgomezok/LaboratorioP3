# Generated by Django 4.2.5 on 2023-10-31 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0008_alter_alumno_analitico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='mu',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='asesor',
            name='cuil',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='docente',
            name='cuil',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
