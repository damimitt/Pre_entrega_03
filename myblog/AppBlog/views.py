from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import *
from .models import *

# Create your views here.
def inicio(request):
    return render(request,'index')



def cursos(request):
    return render(request,'AppBlog/consulta_cursos.html')


def registro_cursos(request):
    if request.method == 'POST':
        mi_formulario = CursoFormulario(request.POST)
        
        print(mi_formulario)
        
        if mi_formulario.is_valid():
            
            informacion = mi_formulario.cleaned_data
            
            curso = Cursos(nombre=informacion['nombre'], camada=informacion['camada'])
            
            curso.save()
            return render(request,'AppBlog/guardado_exito.html')
    else:
        mi_formulario = CursoFormulario()
        return render(request,'AppBlog/registro_cursos.html', {'mi_formulario': mi_formulario})




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

