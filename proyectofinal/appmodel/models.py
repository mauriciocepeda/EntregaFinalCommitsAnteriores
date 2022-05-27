from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Reseña(models.Model):
    fecha=models.DateField(max_length=255)
    titulo=models.CharField(max_length=255)
    cuerpo=RichTextField(max_length=255,null=True,blank=True)

    def __str__(self):
        return f"Reseña: {self.titulo}"

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True,blank=True)
