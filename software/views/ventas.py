import decimal
from datetime import datetime, date, time
from decimal import Decimal
from django.db import connection
from software.views.apiBusquedaRUcDni import ApisNetPe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
import templates
from software.models.comprasModel import Compras

from software.models.cajaModel import Caja
from software.models.tipoTransaccion import TipoTransaccion
from software.models.transaccionModel import Transaccion

from software.models.ProveedoresModel import Proveedores
from software.models.TipoclienteModel import Tipocliente
from software.models.compradetalleModel import CompraDetalle
from software.models.ProductoModel import Producto
from software.models.categoriaModel import Categoria
from software.models.compradetalleModel import CompraDetalle
from software.models.VentaModel import Venta
from software.models.VentaDetalleModel import VentaDetalle
from software.models.UsuarioModel import Usuario
from software.models.UnidadesModel import Unidades
from software.models.TipousuarioModel import Tipousuario
from software.models.TipodocumentoModel import Tipodocumento
from software.models.TipoclienteModel import Tipocliente
from software.models.ProvinciasModel import Provincias
from software.models.ProveedoresModel import Proveedores
from software.models.NumserieModel import Numserie
from software.models.ModulosModel import Modulos
from software.models.empresaModel import Empresa
from software.models.empleadoModel import Empleado
from software.models.Tipo_entidadModel import TipoEntidad
from software.models.distritosModel import Distritos
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from software.models.detallecategoriaxunidadesModel import Detallecategoriaxunidades
from software.models.departamentosModel import Departamentos
from software.models.codigocorreoModel import CodigoCorreo
from software.models.TipoIgvModel import TipoIgv
from software.models.clientesModel import Clientes
from software.models.ModopagoModel import Modopago
from software.models.DepatamentoIgvModel import Detalletipoigvxdepartamento
from openpyxl import Workbook
from django.db.models import Sum
from openpyxl.utils import get_column_letter

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os
from django.conf import settings
from django.templatetags.static import static


# Create your views here.
import requests
import json


def ventas(request):
    id = request.session.get('idtipousuario')

    if id:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id)

        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT `venta`.`idventa`, `clientes`.`razonsocial`, `venta`.`total_a_pagar` AS `total`,
                `venta`.`fechaemision`, `numserie`.`numserie`, `venta`.`numcorrelativo`, `venta`.`ruta_pdf`, `venta`.`ruta_cdr`, `venta`.`respuesta_sunat_descripcion`, `venta`.`respuesta_sunat_codigo`, `venta`.`ruta_ticket`
                FROM `venta`
                INNER JOIN `venta_detalle` ON (`venta`.`idventa` = `venta_detalle`.`idventa`)
                INNER JOIN `numserie` ON (`venta`.`idnumserie` = `numserie`.`idnumserie`)
                INNER JOIN `clientes` ON (`clientes`.`idcliente` = `venta`.`idcliente`)
                WHERE `venta`.`estado` = 1
                GROUP BY `venta`.`idventa`, `clientes`.`razonsocial`, `venta`.`fechaemision`,
                `numserie`.`numserie`, `venta`.`numcorrelativo` 
                Order By `venta`.`idventa` DESC
                
            """)
            rows = cursor.fetchall()

        request.session.get('idusuario')

        return render(request, 'venta/venta.html', {'resultados': rows, "permisos": permisos})
    else:
        return HttpResponse("<h1>No tiene accedo señor</h1>")


def agregar(request):
    id = request.session.get('idtipousuario')
    if id:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id)
        tipo_documentos = Tipodocumento.objects.all()
        tipo_cliente = Tipocliente.objects.all()
        unidades = Unidades.objects.all()
        # tipo_igv = TipoIgv.objects.all()
        modoPago = Modopago.objects.all()

        empresa = Empresa.objects.filter(idempresa=1).first()
        id_departamento = str(empresa.ubigueo)[:2]

        # TIpo documento
        with connection.cursor() as cursor:
            # cursor.execute("""
            #     SELECT d.nombredepartamento, ti.id_tipo_igv, ti.tipo_igv
            #     FROM facsiswave.detalletipoigvxdepartamento dp
            #     INNER JOIN tipo_igvs ti ON ti.id_tipo_igv = dp.id_tipo_igv
            #     INNER JOIN departamentos d ON d.iddepartamentos = dp.iddepartamentos
            #     WHERE d.iddepartamentos = %s
            # """, [id_departamento])
            # rows = cursor.fetchall()
            cursor.execute("""
                SELECT d.nombredepartamento, ti.id_tipo_igv, ti.tipo_igv
                FROM facsiswave.detalletipoigvxdepartamento dp
                INNER JOIN tipo_igvs ti ON ti.id_tipo_igv = dp.id_tipo_igv
                INNER JOIN departamentos d ON d.iddepartamentos = dp.iddepartamentos
   
            """)
            rows = cursor.fetchall()

        data = {
            "tipoDocumentos": tipo_documentos,
            "unidades": unidades,
            "tipoClientes": tipo_cliente,
            'rows': rows,
            "modoPagos": modoPago,
            "permisos": permisos
        }
        return render(request, 'venta/agregarVenta.html', data)


def buscarSerie(request):

    doc = request.POST.get('doc')  # Acceder al valor 'doc' enviado por AJAX
    get_numserie = Numserie.objects.filter(
        idtipodocumento=doc, estado=1, idusuario=request.session.get('idusuario'))
    serie_list = list(get_numserie.values())
    return JsonResponse(serie_list, safe=False)


def buscarProducto(request):

    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')

        productos = Producto.objects.filter(
            nomproducto__icontains=busqueda, estado=1)
        unidad = Unidades.objects.filter(
            idunidad=productos[0].idunidad.idunidad)

        unidad_list = list(unidad.values())
        productos_list = list(productos.values())

        response_data = {
            'productos': productos_list,
            'unidad': unidad_list,
        }

        return JsonResponse(response_data, safe=False)
    return JsonResponse({'error': 'Método no permitido'}, status=400)


def dni(request):

    doc = request.POST.get('doc')
    APIS_TOKEN = 'apis-token-7422.K4qsT4qnQsAvf7Eb6rovatLjtysiiCge'
    api_consultas = ApisNetPe(APIS_TOKEN)
    perosna_info = api_consultas.get_person(doc)
    print("RESPUESTA API:", perosna_info)
    return JsonResponse(perosna_info, safe=False)


def ruc(request):

    doc = request.POST.get('doc')
    print(doc)
    APIS_TOKEN = 'apis-token-7422.K4qsT4qnQsAvf7Eb6rovatLjtysiiCge'
    api_consultas = ApisNetPe(APIS_TOKEN)
    empresa_info = api_consultas.get_company(doc)
    print("RESPUESTA API RUC:", empresa_info)
    return JsonResponse(empresa_info, safe=False)


def guardarVenta(request):
    # Datos totales
    totalGravada = request.POST.get('totalGravada')
    totalExonerada = request.POST.get('totalExonerada')
    totalIgv = request.POST.get('totalIgv')
    ventaTotal = request.POST.get('ventaTotal')

    # Obtener fecha actual
    fechaNow = date.today()

    # cliente
    docCliente = request.POST.get('doccliente')
    tipoCliente = request.POST.get('tipoCliente')
    nomcliente = request.POST.get('nomcliente')
    direccionCliente = request.POST.get('direccion')
    tipoPago = request.POST.get('tipoPago')
    ubigeo = request.POST.get('ubigeo')
    distrito = request.POST.get('distrito')
    provincia = request.POST.get('provincia')
    departamento = request.POST.get('departamento')
    # Para tipo pago
    getTipoPago = Modopago.objects.get(idmodoPago=tipoPago)

    # Para tipo entidad, dni o ruc
    tipo_entidad = 0
    if int(tipoCliente) == 1:
        tipo_entidad = 2

    elif int(tipoCliente) == 2:
        tipo_entidad = 1

    # Documento
    tipoDocumento = request.POST.get('tipoDocumento')
    print("Tipo de documento: ", tipoDocumento)
    # ss
    serie = request.POST.get('serie')
    placa = request.POST.get('placa')
    # fechDocumento = request.POST.get('fechDocumento')

    productos = request.POST.getlist('producto[nombre][]')
    unidades = request.POST.getlist('producto[unidad][]')
    cantidades = request.POST.getlist('producto[cantidad][]')
    precio_unitarios = request.POST.getlist('producto[precioUnitario][]')
    sub_totales = request.POST.getlist('producto[subTotal][]')

    # Tipo igv
    tipo_igv = request.POST.get('tipo_igv')

    getTipoIgv = TipoIgv.objects.get(id_tipo_igv=tipo_igv)

    # Empresa
    getEmpresa = Empresa.objects.get(idempresa=1)

    GetNumcorrelativo = Venta.objects.filter(
        idnumserie=serie
    ).order_by('-numcorrelativo').first()

    print(GetNumcorrelativo)

    if GetNumcorrelativo is None:
        intNumcorrelativo = 1  # Primera venta
        num_ceros = 6  # quieres formato 000001
    else:
        intNumcorrelativo = int(GetNumcorrelativo.numcorrelativo) + 1
        num_ceros = len(str(GetNumcorrelativo.numcorrelativo))

    nuevo_numcorrelativo = "{:0{}}".format(intNumcorrelativo, num_ceros)

    productos_sin_stock = []

    for nombre, cantidad in zip(productos, cantidades):
        obtener_producto = Producto.objects.filter(nomproducto=nombre).first()

        if obtener_producto:
            stockActual = obtener_producto.stockactual

            if stockActual < float(cantidad):
                productos_sin_stock.append(obtener_producto.nomproducto)
        else:
            return JsonResponse({"error": f"Producto {nombre} no encontrado"})

    if productos_sin_stock:
        mensaje = "Falta stock para los siguientes productos:<br>-" + \
            "<br>- ".join(productos_sin_stock)
        return JsonResponse({"mensaje": mensaje})

    # Obtener tipo cliente
    tipo_cliente = Tipocliente.objects.get(idtipocliente=tipoCliente)
    # obtener tipo_entidad
    getTipo_entidad = TipoEntidad.objects.get(id_tipo_entidad=tipo_entidad)
    # agregar cliente
    cliente = Clientes.objects.create(idtipocliente=tipo_cliente, numdoc=docCliente,
                                      razonsocial=nomcliente, direccion=direccionCliente, estado=1,
                                      id_tipo_entidad=getTipo_entidad)

    # Obtener numserie

    numserie = Numserie.objects.get(idnumserie=serie)

    # Obtener la hora actual
    hora_actual = datetime.now().time()

    # Formatear la hora actual en formato HH:MM:SS
    hora_actual_formateada = hora_actual.strftime('%H:%M:%S')

    venta_creada = Venta.objects.create(idnumserie=numserie,
                                        numcorrelativo=nuevo_numcorrelativo,
                                        idcliente=cliente,
                                        fechaemision=fechaNow,
                                        horaemision=hora_actual_formateada,
                                        estado=1,
                                        id_tipo_igv=getTipoIgv,
                                        idempresa=getEmpresa,
                                        idmodoPago=getTipoPago,
                                        total_gravada=totalGravada,
                                        total_igv=totalIgv,
                                        total_exonerada=totalExonerada,
                                        total_a_pagar=ventaTotal)

    # new_list= zip(productos,unidades,cantidades,precio_unitarios,sub_totales)

    for nombre, cantidad_subtotal, sub_total in zip(productos, cantidades, sub_totales):

        obtener_producto = Producto.objects.filter(nomproducto=nombre).first()
        stockActual = obtener_producto.stockactual
        # if stockActual < int(cantidad_subtotal):
        #     return redirect('agregarVenta')

        obtener_producto.stockactual = stockActual - float(cantidad_subtotal)
        obtener_producto.save()

        # precio_subtotal= cantidad_subtotal*precio_unitario #Tal vez
        VentaDetalle.objects.create(idventa=venta_creada, idproducto=obtener_producto,
                                    cantidad=cantidad_subtotal, preciosubtotal=sub_total)

    # Para transaccion
    ultimo_registro = Caja.objects.order_by('-id_caja').first()

    caja = Caja.objects.get(id_caja=ultimo_registro.id_caja)
    tipoTransaccion = TipoTransaccion.objects.get(id_tipo_transaccion=1)

    transaccion = Transaccion()
    transaccion.id_caja = caja
    transaccion.id_tipo_transaccion = tipoTransaccion
    transaccion.monto = ventaTotal
    transaccion.fecha = fechaNow
    transaccion.hora = hora_actual_formateada
    transaccion.save()

    # api sunat --------------
    detalles_api = []

    for nombre, cantidad, precio in zip(productos, cantidades, precio_unitarios):
        producto = Producto.objects.filter(nomproducto=nombre).first()

        tipo_igv_codigo = getTipoIgv.codigo  # 10 o 20

        porcentaje = 18 if tipo_igv_codigo == 10 else 0

        detalles_api.append({
            "codigo": producto.codigoproducto if hasattr(producto, 'codigoproducto') else nombre,
            "descripcion": nombre,
            "unidad": "NIU",
            "cantidad": float(cantidad),
            "mto_valor_unitario": float(precio),
            "porcentaje_igv": porcentaje,
            "tip_afe_igv": str(tipo_igv_codigo),
            "codigo_producto_sunat": "10101500"
        })

    print("Tipo cliente", numserie)
    if len(tipoCliente) == 1:
        tipo_doc_cliente = "6"  # RUC
    elif len(tipoCliente) == 2:
        tipo_doc_cliente = "1"  # DNI
        
    cliente_api = {
        "tipo_documento": tipo_doc_cliente,
        "numero_documento": docCliente,
        "razon_social": nomcliente,
        "direccion": direccionCliente,
        "ubigeo": ubigeo,
        "distrito": distrito,
        "provincia": provincia,
        "departamento": departamento
    }
    print("Cliente API:", cliente_api)
    
    data_api = {
        "company_id": 1,
        "branch_id": 1,
        "serie": numserie.numserie,
        "fecha_emision": str(fechaNow),
        "moneda": "PEN",
        "tipo_operacion": "0101",
        "forma_pago_tipo": "Contado",
        "client": cliente_api,
        "detalles": detalles_api,
        "usuario_creacion": "admin",
        "metodo_envio": "resumen_diario",
    }

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {request.session.get('api_token')}"
    }

    # =========================
    # 1. DEFINIR ENDPOINT BASE
    # =========================
    if numserie.idtipodocumento.codigosunat == '01':
        url = "http://localhost:8001/api/v1/invoices"
        tipo_doc_api = "invoices"

    elif numserie.idtipodocumento.codigosunat == '03':
        url = "http://localhost:8001/api/v1/boletas"
        tipo_doc_api = "boletas"

    # =========================
    # 2. ENVIAR A API
    # =========================
    try:
        response = requests.post(url, json=data_api, headers=headers)
        response_data = response.json()

        print("Respuesta API:", response_data)

        if response_data.get("success"):

            data = response_data["data"]
            api_id = data["id"]
            numero_completo = data["numero_completo"]

            # =========================
            # 3. GENERAR PDF DINÁMICO
            # =========================
            url_pdf = f"http://127.0.0.1:8001/api/v1/{tipo_doc_api}/{api_id}/generate-pdf"

            response_pdf = requests.post(
                url_pdf,
                json={"format": "80mm"},
                headers=headers
            )

            response_pdf_data = response_pdf.json()
            print("Respuesta PDF:", response_pdf_data)

            if response_pdf_data.get("success"):
                pdf_path = response_pdf_data["data"]["pdf_path"]
                ruta_ticket = f"http://127.0.0.1:8001/storage/{pdf_path}"
                apiId = response_pdf_data["data"]["document_id"]
                print("API ID:", api_id)
                print("Numero completo:", numero_completo)
                print("Ruta ticket:", ruta_ticket)
                print("Venta ID:", venta_creada.idventa)
                Venta.objects.filter(idventa=venta_creada.idventa).update(
                    ruta_ticket=ruta_ticket,
                    api_id=apiId
                )
            else:
                print("⚠️ No se generó PDF")

        else:
            print("Error API:", response_data)

            return JsonResponse({
                "mensaje": response_data.get("message", "Error al enviar a SUNAT"),
                "error": True
            }, status=400)

    except Exception as e:
        print("Error enviando a API:", e)

        return JsonResponse({
            "mensaje": str(e),
            "error": True
        }, status=500)

    return JsonResponse({
        "mensaje": "Venta exitosa",
        "ruta_ticket": ruta_ticket if 'ruta_ticket' in locals() else None
    })


def eliminarVentas(request, id):

    Venta.objects.filter(idventa=id).update(estado=0)

    return redirect('ventas')


def eliminarVentaDetalle(request, id):
    if request.method == 'GET':
        id2 = request.session.get('idtipousuario')
        if id2:
            permisos = Detalletipousuarioxmodulos.objects.filter(
                idtipousuario=id2)

            # Recuperar el objeto VentaDetalle que se va a eliminar
            venta_detalle = get_object_or_404(VentaDetalle, idventadetalle=id)

            # Recuperar el id de la venta asociada al VentaDetalle
            # Accede al id de la venta asociada al detalle
            id_venta = venta_detalle.idventa_id

            # Recuperar el producto asociado al detalle de venta
            producto = get_object_or_404(
                Producto, idproducto=venta_detalle.idproducto_id)

            # Actualizar el stock del producto
            producto.stockactual += venta_detalle.cantidad
            producto.save()

            # Eliminar el objeto VentaDetalle
            venta_detalle.delete()

            return redirect('editarVenta', id=id_venta)

        return JsonResponse({'error': 'No autorizado'}, status=403)

    return JsonResponse({'error': 'Método no permitido'}, status=405)


def editarVenta(request, id):
    id2 = request.session.get('idtipousuario')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)

        ventas = Venta.objects.get(pk=id)
        ventas_fechaemision = ventas.fechaemision.strftime('%Y-%m-%d')

        ventas_detalles = VentaDetalle.objects.filter(idventa=id)

        # Registro de la empresa
        empresa = Empresa.objects.filter(idempresa=1).first()

        id_departamento = str(empresa.ubigueo)[:2]

        # Formatear preciounitario en cada detalle de venta
        for detalle in ventas_detalles:
            detalle.preciounitario_formateado = str(
                detalle.idproducto.preciounitario).replace(',', '.')
            detalle.cantidad_formateado = str(
                detalle.cantidad).replace(',', '.')
            detalle.preciosubtotal_formateado = str(
                detalle.preciosubtotal).replace(',', '.')

        ventas.total_gravada_formateado = str(
            ventas.total_gravada).replace(',', '.')
        ventas.total_exonerada_formateado = str(
            ventas.total_exonerada).replace(',', '.')
        ventas.total_igv_formateado = str(ventas.total_igv).replace(',', '.')
        ventas.total_a_pagar_formateado = str(
            ventas.total_a_pagar).replace(',', '.')

        data = {
            'ventas': ventas,
            'ventas_detalles': ventas_detalles,
            'ventas_fechaemision': ventas_fechaemision,
            "permisos": permisos,
            # "rows":rows
        }

        return render(request, 'venta/editarVenta.html', data)


def guardarEditar(request):
    # Datos totales
    totalGravada = request.POST.get('totalGravada')
    totalExonerada = request.POST.get('totalExonerada')
    totalIgv = request.POST.get('totalIgv')
    ventaTotal = request.POST.get('ventaTotal')

    # Cliente
    docCliente = request.POST.get('doccliente')
    nomcliente = request.POST.get('nomcliente')
    direccionCliente = request.POST.get('direccion')
    idCliente = request.POST.get('idcliente')

    nombres = request.POST.getlist('producto[nombre][]')
    cantidades = request.POST.getlist('producto[cantidad][]')
    precio_unitarios = request.POST.getlist('producto[precioUnitario][]')
    sub_totales = request.POST.getlist('producto[subTotal][]')
    idproductos = request.POST.getlist('producto[idproducto][]')

    id_venta = request.POST.get('idVenta')

    venta = Venta.objects.get(idventa=id_venta)

    new_zip = zip(nombres, cantidades, precio_unitarios,
                  sub_totales, idproductos)
    productos_sin_stock = []
    for nombre, cantidad in zip(nombres, cantidades):
        obtener_producto = Producto.objects.filter(nomproducto=nombre).first()

        if obtener_producto:
            stockActual = obtener_producto.stockactual

            if stockActual < float(cantidad):
                productos_sin_stock.append(obtener_producto.nomproducto)
        else:
            return JsonResponse({"error": f"Producto {nombre} no encontrado"})

    if productos_sin_stock:
        mensaje = "Falta stock para los siguientes productos:<br>-" + \
            "<br>- ".join(productos_sin_stock)
        return JsonResponse({"mensaje": mensaje})

    # Si ya existía el registro, edita, si no resta el stock del producto nuevo y agrega un nuevo registro de venta detalle
    for nombre, cantidad, precio_unitario, subtotal, id_producto in new_zip:
        # Reemplaza las comas por puntos en el subtotal
        subtotal = subtotal.replace(',', '.')

        # Convierte los valores a Decimal
        cantidad_decimal = Decimal(cantidad)
        subtotal_decimal = Decimal(subtotal)

        # Si hay un id_producto, intenta actualizar el registro existente
        if id_producto:
            venta_detalle = VentaDetalle.objects.filter(
                idproducto=id_producto, idventa=venta).first()

            if venta_detalle:
                # Sumo la cantidad antes puesta y resto el nuevo
                obtener_producto = Producto.objects.filter(
                    nomproducto=nombre).first()
                stockActual = obtener_producto.stockactual + venta_detalle.cantidad
                obtener_producto.stockactual = stockActual - Decimal(cantidad)
                obtener_producto.save()

                # Actualizo datos en el detalle
                venta_detalle.cantidad = cantidad_decimal
                venta_detalle.preciosubtotal = subtotal_decimal
                venta_detalle.save()
        # else:
        else:
            print("Entro a crear")
            # Si no hay id_producto, busca el producto por su nombre y resta el stock
            producto = Producto.objects.get(nomproducto=nombre)
            stockActual = producto.stockactual
            producto.stockactual = stockActual - int(cantidad)
            producto.save()

            # Verifica si ya existe un registro para este producto en la venta actual
            venta_detalle_existente = VentaDetalle.objects.filter(
                idproducto=producto, idventa=venta).exists()

            if not venta_detalle_existente:
                # Crea un nuevo registro solo si no existe un registro para este producto en la venta actual
                VentaDetalle.objects.create(
                    idventa=venta, idproducto=producto, cantidad=cantidad_decimal, preciosubtotal=subtotal_decimal)

    # Cliente
    getCliente = Clientes.objects.get(idcliente=idCliente)
    getCliente.numdoc = docCliente
    getCliente.razonsocial = nomcliente
    getCliente.direccion = direccionCliente
    getCliente.save()
    # Editar totales de la venta
    venta.total_gravada = totalGravada
    venta.total_igv = totalIgv
    venta.total_exonerada = totalExonerada
    venta.total_a_pagar = ventaTotal
    venta.save()

    return JsonResponse({"mensaje": "Venta exitosa"})


def buscarFechaVentas(request):
    fecha_inicio = request.POST.get('fechaInicio')
    fecha_fin = request.POST.get('fechaFin')

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT venta.idventa, clientes.razonsocial, SUM(venta_detalle.preciosubtotal) AS total,
            venta.fechaemision, numserie.numserie, venta.numcorrelativo
            FROM venta
            INNER JOIN venta_detalle ON (venta.idventa = venta_detalle.idventa)
            INNER JOIN numserie ON (venta.idnumserie = numserie.idnumserie)
            INNER JOIN clientes ON (clientes.idcliente = venta.idcliente)
            WHERE (venta.estado = 1) and (venta.fechaemision BETWEEN %s AND %s)
            GROUP BY venta.idventa, clientes.razonsocial, venta.fechaemision,
            numserie.numserie, venta.numcorrelativo
        """, [fecha_inicio, fecha_fin])
        rows = cursor.fetchall()

    resultado_json = list(rows)
    return JsonResponse(resultado_json, safe=False)


def export_to_excel_ventas(request):
    # Obtener datos de ventas con el total calculado
    ventas = Venta.objects.annotate(
        total=Sum('ventadetalle__preciosubtotal')
    ).values(
        'idventa', 'idcliente__razonsocial', 'numcorrelativo', 'fechaemision', 'total', 'idnumserie__idtipodocumento__abrrdoc'
    ).order_by(
        'idventa', 'idcliente', 'fechaemision'
    )

    # Crear un workbook de Excel
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Ventas"

    # Crear la fila de encabezado
    headers = ["Venta", "Cliente", "Total", "Fecha", "Doc"]
    sheet.append(headers)

    # Ajustar el ancho de la columna de fecha
    fecha_columna = sheet.column_dimensions['D']
    fecha_columna.width = 15  # Ajustar el ancho de la columna de fecha

    # Agregar datos de ventas
    for venta in ventas:
        # Verificar si la fecha de emisión es None
        if venta['fechaemision'] is None:
            fecha_emision = ""  # O cualquier otro valor predeterminado que desees
        else:
            # Formatear la fecha como cadena antes de agregarla al Excel
            fecha_emision = venta['fechaemision'].strftime("%d/%m/%Y")
        # Obtener el prefijo del documento según el tipo de documento
        prefijo_doc = venta['idnumserie__idtipodocumento__abrrdoc'] if venta['idnumserie__idtipodocumento__abrrdoc'] else ''
        doc = f"{prefijo_doc}{venta['numcorrelativo']}-{venta['idventa']}"
        sheet.append([
            venta['idventa'],
            venta['idcliente__razonsocial'],
            venta['total'],
            fecha_emision,
            doc
        ])

    # Configurar la respuesta HTTP
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=ventas.xlsx'

    # Guardar el workbook en la respuesta
    workbook.save(response)

    return response


def custom_json_serializer(obj):
    if isinstance(obj, (datetime, date)):
        return obj.isoformat()
    elif isinstance(obj, time):
        return obj.strftime('%H:%M:%S')
    elif isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")


def enviarSunat(request, id):
    venta = Venta.objects.get(idventa=id)
    tipoDocumento = venta.idnumserie.idtipodocumento.codigosunat

    print("Tipo de documento:", tipoDocumento)
    print("id api:", venta.api_id)

    if tipoDocumento == '01':
        url = f"http://localhost:8001/api/v1/invoices/{venta.api_id}/send-sunat"
        base_storage = "http://127.0.0.1:8001/storage/"
    elif tipoDocumento == '03':
        url = f"http://localhost:8001/api/v1/boletas/{venta.api_id}/send-sunat"
        base_storage = "http://127.0.0.1:8001/storage/"

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": f"Bearer {request.session.get('api_token')}"
    }

    try:
        response = requests.post(url, headers=headers)
        data = response.json()

        print("Respuesta SUNAT:", data)

        if data.get("success"):

            data_sunat = data["data"]

            # =========================
            # 1. RUTAS
            # =========================
            xml_path = data_sunat.get("xml_path")
            cdr_path = data_sunat.get("cdr_path")

            venta.ruta_pdf = base_storage + xml_path if xml_path else None
            venta.ruta_cdr = base_storage + cdr_path if cdr_path else None

            # =========================
            # 2. RESPUESTA SUNAT
            # =========================
            respuesta_sunat = data_sunat.get("respuesta_sunat")

            if respuesta_sunat:
                respuesta_json = json.loads(respuesta_sunat)

                venta.respuesta_sunat_codigo = respuesta_json.get("code")
                venta.respuesta_sunat_descripcion = respuesta_json.get(
                    "description")

            # =========================
            # 4. GUARDAR
            # =========================
            venta.save()

            return JsonResponse({
                "mensaje": "Enviado a SUNAT correctamente",
                "codigo_sunat": venta.respuesta_sunat_codigo,
                "descripcion_sunat": venta.respuesta_sunat_descripcion
            })

        else:
            return JsonResponse({
                "error": "Error al enviar a SUNAT",
                "detalle": data
            })

    except Exception as e:
        print("Error enviando a SUNAT:", e)
        return JsonResponse({
            "error": str(e)
        })
