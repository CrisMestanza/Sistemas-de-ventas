from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from software.models.cajaModel import Caja
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from software.models.UsuarioModel import Usuario


def mostrar_caja(request):
    id2 = request.session.get('idtipousuario')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        usuario = Usuario.objects.get(idusuario=request.session.get('idusuario'))
        cajas_registros = Caja.objects.all()

        data = {
            'cajas_registros_for':cajas_registros,
            "permisos":permisos
        }
        
        return render(request, 'caja/mostrarCajas.html',data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")