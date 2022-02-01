"""Articulos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from aplicaciones.apps.views import crear_articulo, crear_proveedor, editarproveedor, eliminarproveedor, inicio

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',inicio,name="index"),
    path('crear_pro.html',crear_proveedor,name="crear proveedor"),
    path('crear_art.html',crear_articulo,name="crear_articulo"),
    path('editarproveedor/<int:id>/',editarproveedor,name="editar_proveedor"),
    path('eliminarproveedor/<int:id>/',eliminarproveedor,name="eliminar_proveedor"),
]
