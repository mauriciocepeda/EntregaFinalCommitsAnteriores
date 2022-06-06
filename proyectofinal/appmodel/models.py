from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils import timezone

class Reseña(models.Model):
    fecha=models.DateField(default=timezone.now)
    titulo=models.CharField(max_length=255)
    cuerpo=RichTextField(max_length=3000)
    tapa=models.ImageField(blank=True, upload_to='tapas')
    def __str__(self):
        return f"Reseña: {self.titulo}"

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True,blank=True)



