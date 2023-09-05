from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField()
    camada = forms.CharField()
    
class EstudiantesFormulario(forms.Form):
    
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()