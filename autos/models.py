from django.db import models

class Autos(models.Model):
    marca = models.CharField(max_length=20)
    nombre = models.CharField(max_length=30)
    modelo = models.IntegerField()
    color = models.CharField(max_length=20)

class Clientes(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=30)
    direccion = models.CharField(max_length=200)
    email = models.CharField(max_length=250)
    telefono = models.CharField(max_length=20)

