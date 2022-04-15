from django.contrib import admin
from blog.models import Perfil, Publicacion, Comentario
from django import forms
from django.utils.safestring import mark_safe
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode



# Register your models here.
# admin.site.register(Perfil)
# admin.site.register(Publicacion)
# admin.site.register(Comentario)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):  
    fieldsets = [
    ['Informacion personal', {
        'fields': ['user', 'apellido', 'email', 'imagen',   ]
    }],
    ]


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("titulo", "autor")
    ordering = ("titulo", "autor")
    list_filter = ("autor", )
    search_fields = ("titulo__icontains", "autor__user__username__icontains", "autor__apellido__icontains")
    fieldsets = [
         ['Datos de la publicacion', {
        'fields': ['titulo', 'presentacion', 'parrafo', 'autor', 'imagen']
    }],
    ]

    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(PublicacionAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'parrafo':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("publicacion", "autor")
    ordering = ("publicacion", "autor")
    list_filter = ("publicacion",)
    search_fields = ("publicacion__titulo__icontains",)
    fieldsets = [
         ['Datos del comentario', {
        'fields': ['comentario', 'publicacion', 'autor']
    }],
    ]
    
    def formfield_for_dbfield(self, db_field, **kwargs):
        formfield = super(ComentarioAdmin, self).formfield_for_dbfield(db_field, **kwargs)
        if db_field.name == 'comentario':
            formfield.widget = forms.Textarea(attrs=formfield.widget.attrs)
        return formfield
    


admin.site.site_header = "Administrador de blog en django"
admin.site.site_title = "Blog en django admin"
admin.site.index_title = "Administracion del blog"
admin.site.site_url = "/blogs"

