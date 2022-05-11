from django import views
from proyectofinal.urls import path
from .views import resultadosbusqueda, cursoformulario, inicio, alumnoformulario, profesorformulario, busqueda

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', cursoformulario, name='cursos'),
    path('alumnos/', alumnoformulario, name='alumnos'),
    path('profesores/', profesorformulario, name='profesores'),
    path('busqueda/', busqueda, name='busqueda'),
    path('resultadosbusqueda/', resultadosbusqueda, name='resultadosbusqueda'),

]