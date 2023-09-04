from django.db import models

# Create your models here.

class cursos(models.Model):
    
    nombre = models.CharField(max_length=200)
    camada = models.IntegerField()
    
class estudiantes(models.Model):
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    
class entregables(models.Model):
    
    titulo_trabajo = models.CharField(max_length=50)
    fecha_entrega = models.DateField()
    entregado = models.BooleanField()
    