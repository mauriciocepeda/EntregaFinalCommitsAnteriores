from django import views
from proyectofinal.urls import path
from .views import inicio, alumnos, profesores, cursos
from .views import Alumnoslista, AlumnoDetalle, AlumnoCrear, AlumnoEditar, AlumnoBorrar

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('alumnos/', alumnos, name='alumnos'),
    path('profesores/', profesores, name='profesores'),

    path('alumnos/lista', Alumnoslista.as_view(), name='listaalumnos'),
    path('alumnos/<pk>', AlumnoDetalle.as_view(), name='alumnodetalle'),
    path('alumnos/crear/', AlumnoCrear.as_view(), name='alumnocrear'),
    path('alumnos/editar/<pk>', AlumnoEditar.as_view(), name='alumnoeditar'),
    path('alumnos/borrar/<pk>', AlumnoBorrar.as_view(), name='alumnoborrar'),

]