from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    password1=forms.CharField(label="Ingrese contraseña", widget=forms.PasswordInput)
    password2=forms.CharField(label="ingrese nuevamente", widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=['username','email', 'password1','password2']
        help_texts={k:"" for k in fields}

class UserLoginForm(AuthenticationForm):         #probar su uso, quizas se implemente mas adelante
    username=forms.CharField(label="Nombre de usuario")
    password=forms.CharField(label="Contraseña", widget=forms.PasswordInput )

    class Meta:
        model=User
        fields=['username', 'password']
        help_texts={k:""for k in fields}