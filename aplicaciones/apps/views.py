from django.shortcuts import redirect, render

from aplicaciones.apps.forms import ProveedorForm
from .models import Proveedor

def inicio(request):
    proveedores = Proveedor.objects.all()
    return render(request, "index.html",{'p':proveedores})

def crear_proveedor(request):
    if request.method == 'GET':
        form = ProveedorForm()
        contexto={'form':form}
    else:
        form = ProveedorForm(request.POST)
        contexto={'form':form}
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request,"crear_pro.html",contexto)

def crear_articulo(request):
    return render(request,"crear_art.html")


def editarproveedor(request, id):
    proveedor = Proveedor.objects.get(id=id)
    if request.method == 'GET':
        form = ProveedorForm(instance=proveedor)
        contesto = {'form':form}
    else:
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'crear_pro.html',contesto)
    
def eliminarproveedor(request,id):
    proveedor = Proveedor.objects.get(id = id)
    proveedor.delete()
    return redirect('index')    