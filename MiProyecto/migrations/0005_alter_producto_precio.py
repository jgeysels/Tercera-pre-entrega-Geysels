# Generated by Django 4.1.6 on 2023-02-28 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MiProyecto', '0004_alter_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
