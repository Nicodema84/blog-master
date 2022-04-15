from django.db import models
from blog.models import Perfil, User
# Create your models here.

class Chat(models.Model):
    mensaje = models.CharField(max_length=150)
    emisor = models.ForeignKey(Perfil, on_delete=models.CASCADE, default=None, null=True)
    receptor = models.IntegerField()

    def __str__(self) -> str:
        return str(self.mensaje)