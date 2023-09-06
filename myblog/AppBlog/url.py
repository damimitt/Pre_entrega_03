from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name= "index"),
    path('consulta_cursos/', cursos, name= 'consulta_cursos'),
    path('registro_cursos/', registro_cursos, name= 'registro_cursos'),
    path('guardado_con_exito/', guardado_con_exito, name= 'guardado_con_exito'),
    path('registro_alumnos/', registro_alumnos, name= 'registro_alumnos'),
    
]



