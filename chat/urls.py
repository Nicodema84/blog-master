from django.contrib import admin
from django.urls import  path
from . import views

urlpatterns = [

    path('', views.casilla, name='casilla'),
    path('new', views.nuevo_mensaje, name='nuevo_mensaje'),
    path('<int:id_mensaje>', views.mensaje, name='mensaje')

]