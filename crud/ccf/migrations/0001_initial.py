# Generated by Django 4.1.1 on 2022-09-26 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ccf',
            fields=[
                ('nombre', models.CharField(max_length=150, verbose_name='Nombre')),
                ('codigo', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Codigo')),
                ('nit', models.CharField(max_length=12, verbose_name='Nit')),
                ('creado', models.DateField(auto_now_add=True, verbose_name='Creado')),
            ],
        ),
    ]
