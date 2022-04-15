from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from blog.models import Perfil, User
from .models import Chat
# Create your views here.

@login_required(login_url='/inicio') 
def casilla(request):
    chats = Chat.objects.filter(receptor = request.user.id)
    context = {
        'chats' : chats
    }
    return render(request, 'casilla.html', context)

def nuevo_mensaje (request):
    perfiles = Perfil.objects.all()
    context = {
        'perfiles' : perfiles
    }
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        emisor = Perfil.objects.get(user=User.objects.get(id=request.user.id))
        receptor = request.POST.get('id_receptor')
        nuevoMensaje = Chat(mensaje = mensaje, emisor=emisor , receptor=receptor )
        nuevoMensaje.save()
        return redirect ('casilla')
    return render (request, 'nuevo_mensaje.html', context)

def mensaje(request, id_mensaje):
    chat=Chat.objects.get(id=id_mensaje)
    context = {
        'chat' : chat
    }
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        emisor = Perfil.objects.get(user=User.objects.get(id=request.user.id))
        receptor = request.POST.get('receptor')
        nuevo_mensaje = Chat(mensaje=mensaje, emisor=emisor, receptor=receptor)
        nuevo_mensaje.save()
        return redirect ('casilla')
    return render (request, 'mensaje.html', context)