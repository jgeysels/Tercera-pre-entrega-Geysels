# Generated by Django 4.1.6 on 2023-02-28 23:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('MiProyecto', '0002_cliente_apellido_cliente_correo_electronico'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagen',
        ),
    ]