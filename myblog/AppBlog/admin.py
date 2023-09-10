from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    pass

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    pass

@admin.register(Profesores)
class ProfesoresAdmin(admin.ModelAdmin):
    pass
