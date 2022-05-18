from django import views
from proyectofinal.urls import path
from .views import ReseñaLista,ReseñaDetalle, ReseñaCrear, ReseñaEditar,ReseñaBorrar, inicio

urlpatterns = [
    path('', inicio, name='inicio'),


    path('reseñas', ReseñaLista.as_view(), name='reseñas'),
    path('reseñas/<pk>', ReseñaDetalle.as_view(), name='reseñadetalle'),
    path('reseñas/crear/', ReseñaCrear.as_view(), name='reseñacrear'),
    path('reseñas/editar/<pk>', ReseñaEditar.as_view(), name='reseñaeditar'),
    path('reseñas/borrar/<pk>', ReseñaBorrar.as_view(), name='reseñaborrar'),

]