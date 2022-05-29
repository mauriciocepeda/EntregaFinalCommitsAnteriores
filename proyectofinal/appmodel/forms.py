from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.views.generic import CreateView

from appmodel.models import Reseña


class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese contraseña",widget=forms.PasswordInput)
    password2=forms.CharField(label="ingrese nuevamente",widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']
        help_texts={k:"" for k in fields}

class UserLoginForm(AuthenticationForm):         #probar su uso, quizas se implemente mas adelante
    username=forms.CharField(label="Nombre de usuario")
    password=forms.CharField(label="Contraseña", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username', 'password']
        help_texts={k:""for k in fields}


class UserEditform(UserCreationForm):
    email=forms.EmailField(label="Email")
    password1=forms.CharField(label="Nueva contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="ingrese nuevamente", widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email', 'password1','password2']
        help_texts={k:"" for k in fields}


class AvatarForm(forms.Form):
    imagen=forms.ImageField(label='ingrese un avatar')


class ReseñaFormulario(CreateView):
    fecha=forms.DateTimeField(initial=timezone.now)
    titulo=forms.CharField(max_length=255)
    cuerpo=forms.CharField(max_length=3000)
    tapa=forms.ImageField()
    class Meta:
        model=Reseña
        fields=['fecha','titulo','cuerpo','tapa']
        help_texts={k:"" for k in fields}