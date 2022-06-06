from proyectofinal.urls import path
from appmensajes.views import chats, chat_detalle

urlpatterns = [
    path('chats/',chats, name='chats'),
    path('chats/<int:sender>/<int:receiver>/', chat_detalle, name='chat_detalle'),
]