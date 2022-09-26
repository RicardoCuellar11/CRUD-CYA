from django.db import models

# Create your models here.


class ccf(models.Model):
    nombre = models.CharField(
        verbose_name='Nombre',
        max_length=150
    )
    codigo = models.CharField(
        primary_key=True,
        verbose_name='Codigo',
        max_length=10
    ) 
    nit = models.CharField(
        verbose_name='Nit',
        max_length=12
    )
    creado = models.DateField(
        auto_now_add=True,
        verbose_name='Creado'
    )


class Meta:
    db_table = 'ccf'
