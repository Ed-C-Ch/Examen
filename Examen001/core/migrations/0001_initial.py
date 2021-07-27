# Generated by Django 3.2.5 on 2021-07-21 17:35

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
                ('idCliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombreCliente', models.CharField(max_length=50)),
                ('apellidoCliente', models.CharField(max_length=50)),
                ('correoCliente', models.EmailField(max_length=50)),
                ('claveCliente', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Ingresar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('correoCliente', models.EmailField(max_length=50)),
                ('claveCliente', models.CharField(max_length=25)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.cliente')),
            ],
        ),
    ]
