from django.shortcuts import render
from django.http import HttpResponse
from .forms import CursoFormulario, EstudiantesFormulario
from .models import *

# Create your views here.
def inicio(request):
    return render(request,'AppBlog/inicio.html')

def cursos_formulario(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            
            curso = cursos(nombre=informacion['nombre'], camada=informacion['camada'])
            
            curso.save()
            return render(request,'AppBlog/guardado_exito.html')
    else:
        mi_formulario = CursoFormulario()
        return render(request,'AppBlog/cursos.html', {'mi_formulario': mi_formulario})

def entregables(request):
    return render(request,'AppBlog/entregables.html')

def estudiantes3(request):
    return render(request,'AppBlog/estudiantes.html')

def inicio(request):
    return render(request,'AppBlog/inicio.html')

def estudiantes_formulario(request):
    if request.method == 'POST':
        mi_formulario = EstudiantesFormulario(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            
            curso = estudiantes(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            
            curso.save()
            return render(request,'AppBlog/guardado_exito.html')
    else:
        mi_formulario = EstudiantesFormulario()
        return render(request,'AppBlog/estudiantes.html', {'mi_formulario': mi_formulario})
