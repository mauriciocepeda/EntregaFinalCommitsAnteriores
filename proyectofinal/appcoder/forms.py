from django import forms

class Cursoformulario(forms.Form):
    nombre=forms.CharField()
    comision=forms.IntegerField()
    
class Alumnoformulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    documento=forms.IntegerField()

class Profesorformulario(forms.Form):
    nombre=forms.CharField()
    apellido=forms.CharField()
    email=forms.EmailField()
    materia=forms.CharField()