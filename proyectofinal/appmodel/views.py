from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render
from django.http import HttpResponse, request
from numpy import empty
from .models import Reseña, Avatar
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required  
from appmodel.forms import UserRegisterForm, UserEditform , AvatarForm  
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User


@login_required
def inicio(request):
    return render(request, 'appmodel/inicio.html')

@login_required
def perfil(request):
    avatares=Avatar.objects.filter(user=request.user)
    if avatares:
        return render(request, 'appmodel/perfil.html', {'url':avatares[0].imagen.url})
    else:
        return render(request, 'appmodel/perfil.html')






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
    fields=['fecha','titulo','cuerpo','tapa']

class ReseñaEditar(LoginRequiredMixin,UpdateView):
    model=Reseña
    success_url=reverse_lazy('reseñas')
    fields=['fecha','titulo','cuerpo','tapa']

class ReseñaBorrar(LoginRequiredMixin,DeleteView):
    model=Reseña
    success_url=reverse_lazy('reseñas')
    fields=['fecha','titulo','cuerpo','tapa']


#---------------------Login, Logout, Registrate---------

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'appmodel/inicio.html',{"mensaje":'Usuario creado'})
        else:
            form=UserRegisterForm()
            return render(request, 'appmodel/registro.html',{"mensaje":"algo fallo, el usuario no pudo crearse",'form':form})
    else:
        form=UserRegisterForm()
        return render(request, 'appmodel/registro.html',{"form":form})

def agregar_avatar(request):
    if request.method=='POST':
        avatarform=AvatarForm(request.POST, request.FILES)
        if avatarform.is_valid():
            avatarviejo=Avatar.objects.filter(user=request.user)
            if avatarviejo:
                avatarviejo.delete()
            u=User.objects.get(username=request.user)
            avatar=Avatar(user=u,imagen=avatarform.cleaned_data['imagen'])
            avatar.save()
            return render(request, 'appmodel/inicio.html',{"mensaje":f"avatar agregado exitosamente"})
    else:
        avatarform=AvatarForm()
        return render (request,'appmodel/agregar_avatar.html',{'form':avatarform})

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

@login_required
def editar_perfil(request):
    usuario=request.user

    if request.method=="POST":
        form=UserEditform(request.POST, instance=usuario)
        if form.is_valid():
            informacion=form.cleaned_data
            usuario.email=informacion['email']
            usuario.set_password(informacion['password1'])
            usuario.save()
            return render(request,'appmodel/inicio.html', {"mensaje":"su perfil a sido actualizado exitosamente"})
    else:
        form=UserEditform(instance=usuario)
    return render (request,'appmodel/editar_perfil.html', {'form':form,'mensaje':'Edita tu perfil'})


