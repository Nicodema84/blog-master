from ast import Not
from multiprocessing import context
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import formulario
from.models import Perfil, Publicacion
from django.contrib.auth import authenticate, login
from blog.models import Perfil, User, Comentario
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core import serializers


# Create your views here.
@login_required(login_url='/inicio') 
def index (request):
    pepe = 'papa'
    context = {'papa': pepe}
    if request.method == 'POST':
        valor = request.POST.get("valor-busqueda")
        if valor == "1":
            perfiles = Perfil.objects.all()
            if perfiles:
                context={'perfil' : perfiles,
                        'valor' : valor
                }
            else:
                context={
                    'perfil' : None,
                    'valor' : valor,
                    'error' : 'No hay autores'
                }
        else:
            if valor == "2":
                publicaciones = Publicacion.objects.all()
                if publicaciones:
                    context={'publicacion' : publicaciones,
                            'valor' : valor
                    }
                else:
                    context={
                        'publicacion' : None,
                        'valor' : valor,
                        'error' : 'No hay publicaciones'
                    }
            else:
                return redirect('index')
    return render(request, 'index.html', context)



def inicio(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request,'Usuario o contraseña incorrecta')
            return redirect('inicio')
    return render(request, 'blog/login.html')


def home(request):
    pepe = 'papa'
    context = {'papa': pepe}
    if request.method == 'POST':
        valor = request.POST.get("valor-busqueda")
        if valor == "1":
            perfiles = Perfil.objects.all()
            if perfiles:
                context={'perfil' : perfiles,
                        'valor' : valor
                }
            else:
                context={
                    'perfil' : None,
                    'valor' : valor,
                    'error' : 'No hay autores'
                }
        else:
            if valor == "2":
                publicaciones = Publicacion.objects.all()
                if publicaciones:
                    context={'publicacion' : publicaciones,
                            'valor' : valor
                    }
                else:
                    context={
                        'publicacion' : None,
                        'valor' : valor,
                        'error' : 'No hay publicaciones'
                    }
            else:
                return redirect('home')
    return render(request, 'index.html', context)




def cerrar(request):
    logout(request)
    return redirect('home')



@login_required(login_url='/inicio') 
def blog(request, id): 
    blog_autor = Perfil.objects.get(id=id)
    blogs = Publicacion.objects.filter(autor=blog_autor)
    if request.method == 'POST':
        com=request.POST.get('comentario')
        perfil=Perfil.objects.get(user=User.objects.get(id=request.user.id))
        blog=Publicacion.objects.get(id=request.POST.get('idBlog'))
        comentario=Comentario(comentario=com, publicacion=blog, autor=perfil)
        comentario.save()
    comentarios = Comentario.objects.all()
    
    context={
        'perfil' : blog_autor,
        'blog' : blogs,
        'comentarios' : comentarios
    }
    return render(request, 'blog/blog.html', context)



@login_required(login_url='/inicio') 
def agregar(request):
    if request.method == 'POST':
        form = formulario(request.POST, request.FILES)
        form.imagen = "../media/descarga.jpg"
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = formulario()
    context ={'form':form}
    return render(request, 'blog/agregar.html', context)



@login_required(login_url='/inicio')
def edit(request, id):
    blog= Publicacion.objects.get(id=id)
    if request.method == "POST":
        titulo=request.POST.get('titulo')
        presentacion=request.POST.get('presentacion')
        contenido=request.POST.get('contenido')
        imagen=request.POST.get('imagen')
        blog.titulo=titulo
        blog.presentacion=presentacion
        blog.parrafo= contenido
        if imagen == "":
            blog.save() 
        else:
            blog.imagen=imagen
            blog.save()       
        return redirect('publicaciones')
    context= {'blog' : blog}
    return render(request, 'blog/edit.html', context)



@login_required(login_url='/inicio')
def perfil(request):
    perfil=Perfil.objects.get(user=User.objects.get(id=request.user.id))
    context={'perfilLogin':perfil}
    if request.method == 'POST':
        tit=request.POST.get('titulo')
        pre=request.POST.get('presentacion')
        cont=request.POST.get('contenido')
        img=request.POST.get('imagen')
        blog=Publicacion(titulo=tit, presentacion=pre, parrafo=cont, autor=perfil, imagen=img)
        blog.save()
    return render(request , 'blog/perfil.html',context)



@login_required(login_url='/inicio')
def publicaciones(request):
    perfiles = Perfil.objects.all()
    for perfil in perfiles:
        if perfil.user.id == request.user.id:
            perfilLogin=perfil
    blog = Publicacion.objects.filter(autor=perfilLogin)
    comentario=Comentario.objects.all()
    context= {'blogs': blog,
               'comentarios': comentario
    }
    return render(request, 'blog/publicaciones.html', context)



@login_required(login_url='/inicio')
def eliminar(request, blog_id):
    publicacion= Publicacion.objects.get(id=blog_id)
    publicacion.delete()
    return JsonResponse({'id': blog_id})


def eliminarComentario(request, comentario_id):
    comentario = Comentario.objects.get(id=comentario_id)
    comentario.delete()

    return JsonResponse({'id': comentario_id })

def registro(request):
    if request.method == 'POST':
        if request.POST.get('contraseña') != request.POST.get('usuario'):
            if request.POST.get('contraseña') == request.POST.get('contraseña2'):
                username=request.POST.get('usuario')
                contraseña=request.POST.get('contraseña')
                usuario=User(username=username)
                usuario.set_password(contraseña)
                usuario.save()
                ape=request.POST.get('apellido')
                eml=request.POST.get('email')
                img=request.POST.get('imagen')
                perfil=Perfil(user=usuario, apellido=ape, email=eml, imagen=img)
                perfil.save()
                return redirect (inicio)
            else:
                messages.error(request,'Las contraseñas no coinciden')
                return redirect('registro')
        else:
            messages.error(request,'La contraseña no puede ser igual al usuario')
            return redirect('registro')
    return render(request, 'blog/registro.html')

def about(request):
    return render(request, 'blog/about.html')


def publicacion(request,id):
    blogs = Publicacion.objects.get(id=id)
    if request.method == 'POST':
        com=request.POST.get('comentario')
        perfil=Perfil.objects.get(user=User.objects.get(id=request.user.id))
        blog=Publicacion.objects.get(id=request.POST.get('idBlog'))
        comentario=Comentario(comentario=com, publicacion=blog, autor=perfil)
        comentario.save()
    comentarios = Comentario.objects.all()        
    context = {
        'blogs': blogs,
        'comentarios':comentarios
    }
    return render(request, 'blog/publicacion.html', context)