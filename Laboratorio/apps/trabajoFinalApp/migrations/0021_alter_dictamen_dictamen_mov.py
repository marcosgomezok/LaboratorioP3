# Generated by Django 4.2.5 on 2023-10-28 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('trabajoFinalApp', '0020_alter_dictamen_dictamen_mov'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dictamen',
            name='dictamen_mov',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dictamen_mov', to='trabajoFinalApp.movimiento'),
        ),
    ]
