from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.IntegerField()
    
class AlumnoFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    
class ProfesoresFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    