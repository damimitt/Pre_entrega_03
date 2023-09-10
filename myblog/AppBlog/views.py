from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def inicio(request):
    return render(request,'index')

def consultar_cursos(request):
    curso = Cursos.objects.all()
    print(curso)
    return render(request,"AppBlog/consulta_cursos.html", {"value" : curso})

def registro_cursos(request):
    if request.method == 'GET':
        mi_formulario = CursoFormulario()
        return render(request,
                    'AppBlog/registro_cursos.html',
                    {'mi_formulario': CursoFormulario()})
    else:
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            modelo = Cursos(
                            nombre = informacion['nombre'],
                            camada = informacion['camada']                
            )
            modelo.save()
        return redirect('guardado_con_exito')


def registro_alumnos(request):
    if request.method == 'GET':
        mi_formulario = AlumnoFormulario()
        return render(request,
                      'AppBlog/registro_alumnos.html',
                      {'mi_formulario' : AlumnoFormulario()})
    else:
        mi_formulario = AlumnoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            modelo = Alumno(
                        nombre = informacion['nombre'],
                        apellido = informacion['apellido']
                        )
            modelo.save()
        return redirect('guardado_con_exito')
    
    
def inicio(request):
    return render(request,'AppBlog/inicio.html')

def guardado_con_exito(request):
    return render(request,'AppBlog/guardado_exito.html')

