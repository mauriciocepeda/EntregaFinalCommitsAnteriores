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



class Mensaje(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)



