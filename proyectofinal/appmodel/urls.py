from proyectofinal.urls import path
from appmodel.views import inicio, ReseñaLista, ReseñaDetalle, ReseñaCrear, ReseñaEditar, ReseñaBorrar, perfil
from appmodel.views import login_request, register, editar_perfil, agregar_avatar
from django.contrib.auth.views import LogoutView
urlpatterns = [
    path('', inicio, name='inicio'),
    path('perfil', perfil, name='perfil'),
#---------------reseñas crud --------------------------
    path('reseñas', ReseñaLista.as_view(), name='reseñas'),
    path('reseñas/<pk>', ReseñaDetalle.as_view(), name='reseñadetalle'),
    path('reseñas/crear/', ReseñaCrear.as_view(), name='reseñacrear'),
    path('reseñas/editar/<pk>', ReseñaEditar.as_view(), name='reseñaeditar'),
    path('reseñas/borrar/<pk>', ReseñaBorrar.as_view(), name='reseñaborrar'),

#---------------Login-Logout-Registro------------------------------------------

    path('login_request', login_request , name ='login'),
    path('register', register , name ='register'),
    path('logout', LogoutView.as_view(template_name='appmodel/logout.html') , name ='logout'),
    path('editar_perfil',editar_perfil, name='editar_perfil'),
    path('agregar_avatar',agregar_avatar, name='agregar_avatar'),
    
]