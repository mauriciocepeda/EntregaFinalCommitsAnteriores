from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Alumno, Curso, Profesor

def inicio(request):
    return render (request, 'appmodel/inicio.html')

def alumnos(request):
    return render (request, 'appmodel/alumnos.html')

def profesores(request):
    return render (request, 'appmodel/profesores.html')

def cursos(request):
    return render (request, 'appmodel/cursos.html')

#----------------------------------------------------------------------

class Alumnoslista(ListView):
    model=Alumno
    template_name='appmodel/alumnos.html'

class AlumnoDetalle(DetailView):
    model=Alumno
    template_name='appmodel/alumno_detalle.html'

class AlumnoCrear(CreateView):
    model=Alumno
    success_url= reverse_lazy('listaalumnos')
    fields=['nombre', 'apellido', 'documento']

class AlumnoEditar(UpdateView):
    model=Alumno
    success_url= reverse_lazy('listaalumnos')
    fields=['nombre', 'apellido', 'documento']

class AlumnoBorrar(DeleteView):
    model=Alumno
    success_url=reverse_lazy('listaalumnos')
    fields=('nombre','apellido','documento')
