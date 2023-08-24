from django.urls import path
from . import views

urlpatterns = [

    path('',views.home,name='home'),
    path('room/<str:pk>/',views.rooms,name='room'),
    path('data/',views.data,name='data'),
    path('create-room/',views.createRoom,name='create_room'),
    path('update-room/<str:pk>/',views.updateRoom,name='update_room'),
    path('delete-room/<str:pk>/',views.deleteRoom,name='delete_room')
]