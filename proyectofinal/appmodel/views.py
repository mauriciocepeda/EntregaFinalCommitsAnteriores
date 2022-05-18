from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Reseña

def inicio(request):
    return render (request, 'appmodel/inicio.html')


#----------------------------------------------------------------------


class ReseñaLista(ListView):
    model=Reseña
    template_name= 'appmodel/reseñas.html'


class ReseñaDetalle(DetailView):
    model=Reseña
    template_name= 'appmodel/reseña_detalle.html'

class ReseñaCrear(CreateView):
    model=Reseña
    success_url=reverse_lazy('listareseñas')
    fields=['titulo','fecha','cuerpo', 'valoracion']

class ReseñaEditar(UpdateView):
    model=Reseña
    success_url=reverse_lazy('listareseñas')
    fields=['titulo','fecha','cuerpo','valoracion']

class ReseñaBorrar(DeleteView):
    model=Reseña
    sucess_url=reverse_lazy('listareseñas')
    fields=['titulo','fecha','cuerpo','valoracion']


#-----------------------------------------
