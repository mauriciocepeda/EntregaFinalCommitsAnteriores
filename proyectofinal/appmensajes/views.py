from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from .models import Mensaje
from .forms import MensajeFormulario


def chats(request):
        return render(request, 'appmodel/chats.html',
                      {'users': User.objects.exclude(username=request.user.username)})

def chat_detalle(request, sender=None, receiver=None):
    if request.method == 'GET':
        messages = Mensaje.objects.filter(sender_id=sender, receiver_id=receiver, is_read=False)
        for message in messages:
            message.is_read=True
            message.save()
        form=MensajeFormulario()
        return render (request, 'appmodel/chat_detalle.html', {'users': User.objects.exclude(username=request.user.username),
        'form':form,
        'sender':sender,
        'receiver':receiver,
        'messages': Mensaje.objects.filter(sender_id=sender, receiver_id=receiver) | 
        Mensaje.objects.filter(sender_id=receiver, receiver_id=sender)})

    else:
        form_vacio=MensajeFormulario()
        data=MensajeFormulario(request.POST)
        if data.is_valid():
            data_clean=data.cleaned_data.get('message')
            message=Mensaje(sender_id=sender, receiver_id=receiver, message=data_clean)
            message.save()
            return render(request, 'appmodel/chat_detalle.html', {'users': User.objects.exclude(username=request.user.username),
            'form':form_vacio,
            'form_lleno':data,
            'sender':sender,
            'receiver':receiver,
            'messages': Mensaje.objects.filter(sender_id=sender, receiver_id=receiver) |
             Mensaje.objects.filter(sender_id=receiver, receiver_id=sender)})