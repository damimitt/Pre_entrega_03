from django.urls import path
from AppBlog import views

urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('cursos/', views.cursos_formulario, name= 'cursos'),
    path('entregables/', views.entregables, name= 'entregables'),
    path('estudiantes/', views.estudiantes_formulario, name= 'estudiantes'),
    
]



