from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from software.models.CotizacionModel import Cotizacion
from software.models.CotizacionDetalleModel import CotizacionDetalle
from software.models.clientesModel import Clientes
from software.models.TipoclienteModel import Tipocliente
from software.models.Tipo_entidadModel import TipoEntidad
from software.models.empresaModel import Empresa
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from software.views.apiBusquedaRUcDni import ApisNetPe

APIS_TOKEN = 'apis-token-7422.K4qsT4qnQsAvf7Eb6rovatLjtysiiCge'


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
    data = {'permisos': permisos}
    return render(request, 'cotizacion/agregarCotizacion.html', data)


def buscarCliente(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)

    doc = request.POST.get('doc', '').strip()
    if not doc:
        return JsonResponse({'error': 'Ingrese un documento'}, status=400)

    # Buscar en la BD local primero
    cliente = Clientes.objects.filter(numdoc=doc, estado=1).first()
    if cliente:
        return JsonResponse({
            'found': True,
            'idcliente': cliente.idcliente,
            'nombre': cliente.razonsocial,
            'direccion': cliente.direccion or '',
        })

    # Consultar API externa
    try:
        api = ApisNetPe(APIS_TOKEN)
        if len(doc) == 8:
            info = api.get_person(doc)
            nombre = f"{info.get('nombres', '')} {info.get('apellidoPaterno', '')} {info.get('apellidoMaterno', '')}".strip()
            direccion = '-'
        elif len(doc) == 11:
            info = api.get_company(doc)
            nombre = info.get('razonSocial', '')
            direccion = info.get('direccion', '-')
        else:
            return JsonResponse({'error': 'Documento inválido (8=DNI, 11=RUC)'}, status=400)

        if not nombre:
            return JsonResponse({'error': 'No se encontró información'}, status=404)

        # Crear cliente automáticamente
        tipocliente = Tipocliente.objects.first()
        tipo_entidad = TipoEntidad.objects.filter(
            codigoentidad='1' if len(doc) == 8 else '6'
        ).first() or TipoEntidad.objects.first()

        nuevo_cliente = Clientes.objects.create(
            numdoc=doc,
            razonsocial=nombre,
            direccion=direccion,
            estado=1,
            idtipocliente=tipocliente,
            id_tipo_entidad=tipo_entidad,
        )

        return JsonResponse({
            'found': False,
            'created': True,
            'idcliente': nuevo_cliente.idcliente,
            'nombre': nombre,
            'direccion': direccion,
        })

    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


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
