from django import views
from proyectofinal.urls import path
from appmodel.views import inicio, ReseñaLista, ReseñaDetalle, ReseñaCrear, ReseñaEditar, ReseñaBorrar
from appmodel.views import login_request, register

urlpatterns = [
    path('inicio', inicio, name='inicio'),

#---------------reseñas crud --------------------------
    path('reseñas', ReseñaLista.as_view(), name='reseñas'),
    path('reseñas/<pk>', ReseñaDetalle.as_view(), name='reseñadetalle'),
    path('reseñas/crear/', ReseñaCrear.as_view(), name='reseñacrear'),
    path('reseñas/editar/<pk>', ReseñaEditar.as_view(), name='reseñaeditar'),
    path('reseñas/borrar/<pk>', ReseñaBorrar.as_view(), name='reseñaborrar'),

#---------------Login-Logout-Registro------------------------------------------

    path('login_request', login_request , name ='login'),
    path('register', register , name ='register'),
    
]