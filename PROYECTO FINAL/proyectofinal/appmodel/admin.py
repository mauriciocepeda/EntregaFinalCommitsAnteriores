from django.contrib import admin
from .models import Alumno, Profesor, Curso

admin.site.register(Alumno)
admin.site.register(Curso)
admin.site.register(Profesor)