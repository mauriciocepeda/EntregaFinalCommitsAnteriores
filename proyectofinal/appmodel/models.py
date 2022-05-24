from django.db import models
from django.contrib.auth.models import User

class Reseña(models.Model):
    titulo=models.CharField(max_length=255)
    fecha=models.DateField(max_length=255)
    cuerpo=models.CharField(max_length=255)
    valoracion=models.IntegerField()

    def __str__(self):
        return f"Reseña: {self.titulo}"

class Avatar(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to='avatares', null=True,blank=True)
