from django.shortcuts import render
from django.http import HttpResponse
from .forms import CursoFormulario
from .models import *

# Create your views here.
def inicio(request):
    return render(request,'AppBlog/inicio.html')

def cursos2(request):
    return render(request,'AppBlog/cursos.html')

def entregables(request):
    return render(request,'AppBlog/entregables.html')

def estudiantes(request):
    return render(request,'AppBlog/estudiantes.html')

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
            return render(request,'AppBlog/inicio.html')
    else:
        mi_formulario = CursoFormulario()
        return render(request,'AppBlog/cursos.html', {'mi_formulario': mi_formulario})