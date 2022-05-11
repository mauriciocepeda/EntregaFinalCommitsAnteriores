
from django.http import HttpResponse, request
from django.shortcuts import render
from django.template import Context, Template, loader

from .forms import Cursoformulario, Alumnoformulario, Profesorformulario
from .models import alumno, curso, profesor

def inicio(request):
    return render(request, 'appcoder\inicio.html')

def cursoformulario(request):
    if request.method=="POST":
        miformulario=Cursoformulario(request.POST)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            curso1= curso(Nombre=informacion['nombre'], Comision=informacion['comision'])
            curso1.save()
            return render(request, 'appcoder\inicio.html')
    else:
        miformulario=Cursoformulario()
    return render (request, 'appcoder\curso.html', {'miformulario': miformulario})

def alumnoformulario(request):
    if request.method=="POST":
        miformulario=Alumnoformulario(request.POST)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            alumno1= alumno(Nombre=informacion['nombre'], Apellido=informacion['apellido'], Documento=informacion['documento'])
            alumno1.save()
            return render(request, 'appcoder\inicio.html')
    else:
        miformulario=Alumnoformulario()
    return render (request, 'appcoder\\alumno.html', {'miformulario': miformulario})

def profesorformulario(request):

    if request.method=="POST":
        miformulario=Profesorformulario(request.POST)
        if miformulario.is_valid():
            informacion=miformulario.cleaned_data
            profesor1= profesor(Nombre=informacion['nombre'], Apellido=informacion['apellido'], Email=informacion['email'], Materia=informacion['materia'])
            profesor1.save()
            return render(request, 'appcoder\inicio.html')
    else:
        miformulario=Profesorformulario()
    return render (request, 'appcoder\profesor.html', {'miformulario': miformulario})

def busqueda(request):
    return render(request, 'appcoder/busqueda.html' )

def resultadosbusqueda(request):

    if request.GET['nombre']:
        nombre= request.GET['nombre']
        cursos=curso.objects.filter(Nombre=nombre)
        return render(request, 'appcoder\\resultadosbusqueda.html', {'cursos':cursos, 'nombre':nombre})

    else:
        rta='No has ingresado ningun dato. Por favor, vuelve a la pagina de cursos.'
        return render (request, 'appcoder\\resultadosbusqueda.html', {"rta": rta})
