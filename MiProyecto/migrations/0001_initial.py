# Generated by Django 4.1.6 on 2023-02-21 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=200)),
                ('telefono', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DetalleOrden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.PositiveIntegerField(default=1)),
                ('precio_unitario', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=6)),
                ('imagen', models.ImageField(upload_to='productos/')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now_add=True)),
                ('total', models.DecimalField(decimal_places=2, max_digits=6)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiProyecto.cliente')),
                ('productos', models.ManyToManyField(through='MiProyecto.DetalleOrden', to='MiProyecto.producto')),
            ],
        ),
        migrations.AddField(
            model_name='detalleorden',
            name='orden',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiProyecto.orden'),
        ),
        migrations.AddField(
            model_name='detalleorden',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MiProyecto.producto'),
        ),
    ]
