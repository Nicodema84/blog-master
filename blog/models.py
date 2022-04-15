from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from pickle import TRUE
from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from django import forms



class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(max_length=40)
    imagen = models.ImageField(upload_to='media', blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Perfiles'

    def __unicode__(self,):
        return str(self.imagen)

    def __str__(self) -> str:
        return self.user.username + ' ' + self.apellido



class Publicacion(models.Model):
    titulo = models.CharField(max_length=50)
    presentacion = models.CharField(max_length=75, default=None, null=True)
    parrafo = models.CharField(max_length=400)
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, default=None, null=True)
    fecha = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(upload_to='media', blank=True, null=True)

    def __unicode__(self,):
        return str(self.imagen)

    class Meta:
        verbose_name_plural = 'Publicaciones'

    def __str__(self) -> str:
        return self.titulo




class Comentario(models.Model):
    comentario = models.CharField(max_length=400)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE, default=None, null=True)
    autor = models.ForeignKey(Perfil, on_delete=models.CASCADE, default=None, null=True)

    def __str__(self) -> str:
        return str(self.autor)
