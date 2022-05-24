from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse, request
from .models import Reseña, Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin     
from django.contrib.auth.decorators import login_required  
from appmodel.forms import UserRegisterForm, UserEditform       
from django.contrib.auth import login, authenticate, logout

@login_required
def inicio(request):
    avatar=Avatar.objects.filter(user=request.user.id)

    return render (request, 'appmodel/inicio.html',{'url':avatar[0].imagen.url})

def perfil(request):
    avatar=Avatar.objects.filter(user=request.user.id)

    return render(request, 'appmodel/perfil.html',{'url':avatar[0].imagen.url})






#----------------------------------------------------------------------


class ReseñaLista(LoginRequiredMixin,ListView):
    model=Reseña
    template_name= 'appmodel/reseñas.html'

class ReseñaDetalle(LoginRequiredMixin, DetailView):
    model=Reseña
    template_name= 'appmodel/reseña_detalle.html'

class ReseñaCrear(LoginRequiredMixin,CreateView):
    model=Reseña
    success_url=reverse_lazy('reseñas')
    fields=['titulo','fecha','cuerpo', 'valoracion']

class ReseñaEditar(LoginRequiredMixin,UpdateView):
    model=Reseña
    success_url=reverse_lazy('reseñas')
    fields=['titulo','fecha','cuerpo','valoracion']

class ReseñaBorrar(LoginRequiredMixin,DeleteView):
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

                return render(request, 'appmodel/inicio.html',{"mensaje":f"Bienvenido! {nombre}"})
            else:
                return render(request, 'appmodel/login.html', {"mensaje":"Usuario o contraseña invalida, intentelo nuevamente...", "form_vacio":form})
        else:
            return render(request, 'appmodel/login.html', {"mensaje":"usuario o contraseña invalida, intentelo nuevamente...", "form_vacio":form})
    else:
        form=AuthenticationForm()
        return render(request, 'appmodel/login.html', {"form":form} )

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(data=request.POST)
        if form.is_valid():
            nombre=form.cleaned_data.get('username')
            form.save()
            return render(request, 'appmodel/inicio.html', {"mensaje":f"usuario creado exitosamente, bienvenido! {nombre}"})
        else:
            return render(request, 'appmodel/registro.html',{"mensaje":"algo fallo, el usuario no pudo crearse"})

    else:
        form=UserRegisterForm()
        return render(request, 'appmodel/registro.html',{"form":form})

@login_required
def editar_perfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserRegisterForm(request.POST, instance=usuario)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.email=informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.save()
            return render(request,'appmodel/perfil.html', {"mensajeeditar":"su perfil a sido actualizado exitosamente"})
    else:
        form=UserRegisterForm(instance=usuario)
    return render (request,'appmodel/editar_perfil.html', {'form':form,'mensaje':'Edita tu perfil'})