from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Cursos)
class CursoAdmin(admin.ModelAdmin):
    pass

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass
