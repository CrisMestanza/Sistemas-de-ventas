from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from software.models.CotizacionModel import Cotizacion
from software.models.CotizacionDetalleModel import CotizacionDetalle
from software.models.clientesModel import Clientes
from software.models.empresaModel import Empresa
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos


def cotizaciones(request):
    id2 = request.session.get('idtipousuario')
    if not id2:
        return HttpResponse("<h1>No tiene acceso</h1>")
    permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
    lista = Cotizacion.objects.filter(estado=1).select_related('idcliente').order_by('-idcotizacion')
    data = {'cotizaciones': lista, 'permisos': permisos}
    return render(request, 'cotizacion/cotizaciones.html', data)


def agregar(request):
    id2 = request.session.get('idtipousuario')
    if not id2:
        return HttpResponse("<h1>No tiene acceso</h1>")
    permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
    clientes = Clientes.objects.filter(estado=1)
    data = {'clientes': clientes, 'permisos': permisos}
    return render(request, 'cotizacion/agregarCotizacion.html', data)


def guardar(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    try:
        idcliente = request.POST.get('idcliente')
        observaciones = request.POST.get('observaciones', '')
        productos = request.POST.getlist('producto[]')
        descripciones = request.POST.getlist('descripcion[]')
        cantidades = request.POST.getlist('cantidad[]')
        precios = request.POST.getlist('preciounitario[]')
        subtotales = request.POST.getlist('subtotal[]')

        if not productos:
            return JsonResponse({'error': 'Agregue al menos un ítem'}, status=400)

        cliente = get_object_or_404(Clientes, idcliente=idcliente)
        total = sum(float(s) for s in subtotales)

        cotizacion = Cotizacion.objects.create(
            idcliente=cliente,
            total=round(total, 2),
            observaciones=observaciones,
            estado=1,
        )

        for i in range(len(productos)):
            CotizacionDetalle.objects.create(
                idcotizacion=cotizacion,
                producto=productos[i],
                descripcion=descripciones[i] if i < len(descripciones) else '',
                cantidad=float(cantidades[i]),
                preciounitario=float(precios[i]),
                subtotal=float(subtotales[i]),
            )

        return JsonResponse({'success': True, 'id': cotizacion.idcotizacion})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def imprimir(request, id):
    id2 = request.session.get('idtipousuario')
    if not id2:
        return HttpResponse("<h1>No tiene acceso</h1>")
    cotizacion = get_object_or_404(Cotizacion, idcotizacion=id)
    detalles = CotizacionDetalle.objects.filter(idcotizacion=cotizacion)
    empresa = Empresa.objects.first()
    data = {'cotizacion': cotizacion, 'detalles': detalles, 'empresa': empresa}
    return render(request, 'cotizacion/imprimirCotizacion.html', data)


def eliminar(request, id):
    Cotizacion.objects.filter(idcotizacion=id).update(estado=0)
    return redirect('cotizaciones')
