
from tkinter import E
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Reseña
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate, logout


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
    success_url=reverse_lazy('reseñas')
    fields=['titulo','fecha','cuerpo', 'valoracion']

class ReseñaEditar(UpdateView):
    model=Reseña
    success_url=reverse_lazy('reseñas')
    fields=['titulo','fecha','cuerpo','valoracion']

class ReseñaBorrar(DeleteView):
    model=Reseña
    success_url=reverse_lazy('reseñas')
    fields=['titulo','fecha','cuerpo','valoracion']


#---------------------Login, Logout, Registrate---------

def login_request(request):
    if request.method=="POST":
        form=AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            nombre=form.cleaned_data.get('username')
            contraseña=form.cleaned_data.get('password')
            user=authenticate(username=nombre, password=contraseña)

            if user is not None:
                login(request, user)

                return render(request, 'appmodel/reseñas.html')
            else:
                return render(request, 'appmodel/inicio.html')
        else:
            return render(request, 'appmodel/inicio.html')
    else:
        form=AuthenticationForm()
        return render(request, 'appmodel/login.html', {"form":form} )

def register(request):
    if request.method=="POST":
        form=UserCreationForm(data=request.POST)
        if form.is_valid():
            user=form.cleaned_data.get('username')
            form.save()
            return render(request, 'appmodel/inicio.html', {"mensaje": "usuario creado"})
        else:
            return render(request, 'appmodel/login.html',{"mensaje":"algo falle, el usuario no pudo crearse"})

    else:
        form=UserCreationForm()
        return render(request, 'appmodel/login.html',{"form":form})



