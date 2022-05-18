from django.db import models

class Reseña(models.Model):
    titulo=models.CharField(max_length=255)
    fecha=models.DateField(max_length=255)
    cuerpo=models.CharField(max_length=255)
    valoracion=models.IntegerField()

    def __str__(self):
        return f"Reseña: {self.titulo}"
