from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from software.models.cajaModel import Caja
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from software.models.UsuarioModel import Usuario
from software.models.SucursalModel import Sucursal


def mostrar_caja(request):
    id2 = request.session.get('idtipousuario')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        es_superadmin = request.session.get('es_superadmin', False)
        idsucursal = request.session.get('idsucursal')
        sucursal_filtro = request.GET.get('sucursal') if es_superadmin else None
        sucursales = Sucursal.objects.all() if es_superadmin else []

        qs = Caja.objects.select_related('usuario_apertura__idsucursal', 'usuario_cierre').all()
        if es_superadmin and sucursal_filtro:
            qs = qs.filter(usuario_apertura__idsucursal=sucursal_filtro)
        elif not es_superadmin:
            qs = qs.filter(usuario_apertura__idsucursal=idsucursal)

        data = {
            'cajas_registros_for': qs,
            'permisos': permisos,
            'sucursales': sucursales,
            'sucursal_filtro': sucursal_filtro or '',
        }

        return render(request, 'caja/mostrarCajas.html', data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")