from multiprocessing import context
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, redirect
from django.http import HttpResponse, request
from django.http.response import JsonResponse
from .models import Reseña, Avatar, Mensaje
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required  
from appmodel.forms import UserRegisterForm, UserEditform , AvatarForm, ReseñaFormulario 
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from rest_framework.parsers import JSONParser
from .serializer import MensajeSerializer
from django.views.decorators.csrf import csrf_exempt


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

#------------------------Mensajes----------------------------------------------------------------
@csrf_exempt
def message_list(request, sender=None, receiver=None):

    if request.method == 'GET':
        messages = Mensaje.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        serializer = MensajeSerializer(messages, many=True, context={'request': request})
        for message in messages:
            message.is_read = True
            message.save()
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MensajeSerializer(data=data)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=201)
        else:
            return JsonResponse(serializer.errors , status=400)

def chat_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        return render(request, 'appmodel/chat.html',
                      {'users': User.objects.exclude(username=request.user.username)})


def message_view(request, sender, receiver):
    if not request.user.is_authenticated:
        return redirect('login')
    if request.method == "GET":
        return render(request, "appmodel/messages.html",
                      {'users': User.objects.exclude(username=request.user.username),
                       'receiver': User.objects.get(id=receiver),
                       'messages': Mensaje.objects.filter(sender_id=sender, receiver_id=receiver) |
                                   Mensaje.objects.filter(sender_id=receiver, receiver_id=sender)})


