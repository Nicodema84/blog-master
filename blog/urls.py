from django.contrib import admin
from django.urls import  path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pages', views.index, name='index'),
    path('pages/<int:id>', views.publicacion, name='publicacion'),
    path('autor/<int:id>', views.blog, name='blog'),
    path('inicio', views.inicio, name='inicio'),
    path('cerrar', views.cerrar, name='cerrar'),
    path('perfil', views.perfil, name='perfil'),
    path('publicaciones', views.publicaciones, name='publicaciones'),
    path('eliminar/<str:blog_id>', views.eliminar, name='eliminar'),
    path('registro', views.registro, name='registro'),
    path('eliminarComentario/<str:comentario_id>', views.eliminarComentario, name='eliminarComentario'),
    path('about', views.about, name='about'),
    path('edit/<str:id>', views.edit, name='edit')

]