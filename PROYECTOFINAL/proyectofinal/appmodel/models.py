from django.db import models

class Alumno (models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    documento=models.IntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre=models.CharField(max_length=255)
    comision=models.IntegerField()

    def __str__(self):
        return f'CURSO: {self.nombre} {self.comision}'

class Profesor(models.Model):
    nombre=models.CharField(max_length=255)
    apellido=models.CharField(max_length=255)
    email=models.EmailField()
    materia=models.CharField(max_length=255)

    def __str__(self):
        return f"PROFESOR {self.nombre} {self.apellido} \n MATERIA: {self.materia}"
