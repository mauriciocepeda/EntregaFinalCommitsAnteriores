from django.contrib import admin

from .models import alumno, profesor, curso

admin.site.register(alumno)
admin.site.register(curso)
admin.site.register(profesor)