from django.http import HttpResponse
from django.shortcuts import redirect, render

from software.models.ProveedoresModel import Proveedores
from software.models.TipoclienteModel import Tipocliente
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos


def proveedores(request):
    idtipousuario = request.session.get('idtipousuario')
    if not idtipousuario:
        return HttpResponse("<h1>No tiene acceso señor</h1>")

    permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=idtipousuario)
    proveedores_registros = Proveedores.objects.filter(estado=1).select_related('idtipocliente')
    tipo_clientes = Tipocliente.objects.filter(estado=1)

    data = {
        'proveedores': proveedores_registros,
        'tipo_clientes': tipo_clientes,
        'permisos': permisos
    }
    return render(request, 'proveedores/proveedores.html', data)


def agregar(request):
    if request.method == 'POST':
        idtipocliente = request.POST.get('idtipocliente')
        numdoc = request.POST.get('numdoc')
        razonsocial = request.POST.get('razonsocial')

        Proveedores.objects.create(
            idtipocliente_id=idtipocliente,
            numdoc=numdoc,
            razonsocial=razonsocial,
            estado=1
        )

    return redirect('proveedores')


def editar(request):
    if request.method == 'POST':
        idproveedor = request.POST.get('idproveedor')
        proveedor = Proveedores.objects.get(idproveedor=idproveedor)
        proveedor.idtipocliente_id = request.POST.get('idtipocliente')
        proveedor.numdoc = request.POST.get('numdoc')
        proveedor.razonsocial = request.POST.get('razonsocial')
        proveedor.save()

    return redirect('proveedores')


def eliminar(request, id):
    Proveedores.objects.filter(idproveedor=id).update(estado=0)
    return redirect('proveedores')
