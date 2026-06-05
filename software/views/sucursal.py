from django.http import HttpResponse
from django.shortcuts import redirect, render

from software.models.SucursalModel import Sucursal
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos


def sucursales(request):
    id2 = request.session.get('idtipousuario')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        lista = Sucursal.objects.all()
        data = {
            'sucursales': lista,
            'permisos': permisos,
        }
        return render(request, 'sucursal/sucursal.html', data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")


def sucursalAgregar(request):
    nombre = request.POST.get('nombreSucursal')
    sucursal = Sucursal()
    sucursal.nombre_sucursal = nombre
    sucursal.save()
    return redirect('sucursales')


def sucursalEditar(request):
    id = request.POST.get('idsucursal2')
    nombre = request.POST.get('nombreSucursal2')
    Sucursal.objects.filter(idsucursal=id).update(nombre_sucursal=nombre)
    return redirect('sucursales')


def sucursalEliminar(request, id):
    Sucursal.objects.filter(idsucursal=id).delete()
    return redirect('sucursales')
