from django.db import models

class alumno (models.Model):
    Nombre=models.CharField(max_length=255)
    Apellido=models.CharField(max_length=255)
    Documento=models.IntegerField()

    def __str__(self):
        return f"ALUMNO {self.Nombre} {self.Apellido}"

class curso(models.Model):
    Nombre=models.CharField(max_length=255)
    Comision=models.IntegerField()

    def __str__(self):
        return f'CURSO: {self.Nombre} {self.Comision}'

class profesor(models.Model):
    Nombre=models.CharField(max_length=255)
    Apellido=models.CharField(max_length=255)
    Email=models.EmailField()
    Materia=models.CharField(max_length=255)

    def __str__(self):
        return f"PROFESOR {self.Nombre} {self.Apellido} \n MATERIA: {self.Materia}"


