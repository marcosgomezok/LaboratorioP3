# Generated by Django 4.2.5 on 2023-10-30 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0007_alumno_analitico'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='analitico',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
