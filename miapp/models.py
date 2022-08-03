from django.db import models

class Curso(models.Model):
    codigo = models.CharField(max_length=100)
    nombre = models.TextField()
    hora = models.CharField(max_length=100)
    creditos = models.CharField(max_length=100)
    estado = models.BooleanField()

class Carrera(models.Model):
    nombre = models.TextField()
    n_corto = models.CharField(max_length=100)
    imagen = models.TextField()
    estado = models.CharField(max_length=1)

