from django.db import models

# Create your models here.

class Cursos(models.Model):
    
    nombre = models.CharField(max_length=200)
    camada = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} ({self.camada})"
    
class Alumno(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} ({self.apellido})"
    

class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.nombre} ({self.apellido})"