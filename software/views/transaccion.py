from django.utils import timezone
from django.shortcuts import get_object_or_404
from datetime import datetime, date
from decimal import Decimal
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from software.models.cajaModel import Caja
from software.models.UsuarioModel import Usuario
from software.models.tipoTransaccion import TipoTransaccion
from software.models.transaccionModel import Transaccion

def mostrar_Transaccion(request):
    id2 = request.session.get('idtipousuario')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        usuario = Usuario.objects.get(idusuario=request.session.get('idusuario'))
        transacciones_registros = Transaccion.objects.all()
        cajas = Caja.objects.all()
        tipoTransacciones=TipoTransaccion.objects.all()

        data = {
            'transacciones_registros_for':transacciones_registros,'tipoTransacciones':tipoTransacciones,
            "permisos":permisos
        }
        
        return render(request, 'transaccion/mostrarTransaccion.html',data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")

def agregar_Transaccion(request):
    if request.method == "POST":
        try:
            tipoTransaccion = request.POST.get('tipoTransaccion2')
            descripcionTrans = request.POST.get('descripcionTransaccion2')
            montotrans = request.POST.get('montoTransaccion2')
            
            # Obtener el usuario de la sesión
            id_usuario = request.session.get('idusuario')
            if not id_usuario:
                return JsonResponse({"error": "Usuario no autenticado"}, status=400)
            
            usuario = get_object_or_404(Usuario, idusuario=id_usuario)

            # Obtener la última caja del usuario de apertura
            caja = Caja.objects.filter(usuario_apertura=usuario).order_by('-id_caja').first()
            if not caja:
                return JsonResponse({"error": "No hay cajas disponibles para este usuario"}, status=400)

            # Traer la instancia de tipo transaccion
            getTipoTransaccion = get_object_or_404(TipoTransaccion, id_tipo_transaccion=tipoTransaccion)

            # Crear la transacción con la caja y otros datos
            transaccion = Transaccion.objects.create(
                id_tipo_transaccion=getTipoTransaccion,
                descripcion=descripcionTrans,
                monto=montotrans,
                id_caja=caja,
                
            )

            transaccion.save()
            return JsonResponse({"message": "Transacción agregada exitosamente"}, status=201)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)

def editar_Transaccion(request):
    if request.method == "POST":
        try:
            id_transaccion = request.POST.get('id_transaccion')
            tipoTransaccion = request.POST.get('tipoTransaccion1')
            descripcionTrans = request.POST.get('descripcionTransaccion1')
            montotrans = request.POST.get('montoTransaccion1').replace(',', '.')
            
            # Obtener el usuario de la sesión
            id_usuario = request.session.get('idusuario')
            if not id_usuario:
                return JsonResponse({"error": "Usuario no autenticado"}, status=400)
            
            usuario = get_object_or_404(Usuario, idusuario=id_usuario)

            # Obtener la última caja del usuario de apertura
            caja = Caja.objects.filter(usuario_apertura=usuario).order_by('-id_caja').first()
            if not caja:
                return JsonResponse({"error": "No hay cajas disponibles para este usuario"}, status=400)

            # Traer la instancia de tipo transaccion
            getTipoTransaccion = get_object_or_404(TipoTransaccion, id_tipo_transaccion=tipoTransaccion)
            
            # Obtener la transacción existente
            transaccion = get_object_or_404(Transaccion, id_transaccion=id_transaccion)
            transaccion.id_tipo_transaccion = getTipoTransaccion
            transaccion.monto = montotrans
            transaccion.descripcion = descripcionTrans
    
            transaccion.save()
            return JsonResponse({"message": "Transacción actualizada exitosamente"}, status=200)
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)

    return JsonResponse({"error": "Método no permitido"}, status=405)