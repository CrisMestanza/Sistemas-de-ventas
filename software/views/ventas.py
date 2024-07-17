import decimal
from datetime import datetime, date, time
from decimal import Decimal
from django.db import connection
from software.views.apiBusquedaRUcDni import ApisNetPe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
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
                `venta`.`fechaemision`, `numserie`.`numserie`, `venta`.`numcorrelativo`, `venta`.`ruta_pdf`, `venta`.`ruta_cdr`, `venta`.`respuesta_sunat_descripcion`, `venta`.`respuesta_sunat_codigo`
                FROM `venta`
                INNER JOIN `venta_detalle` ON (`venta`.`idventa` = `venta_detalle`.`idventa`)
                INNER JOIN `numserie` ON (`venta`.`idnumserie` = `numserie`.`idnumserie`)
                INNER JOIN `clientes` ON (`clientes`.`idcliente` = `venta`.`idcliente`)
                WHERE `venta`.`estado` = 1
                GROUP BY `venta`.`idventa`, `clientes`.`razonsocial`, `venta`.`fechaemision`,
                `numserie`.`numserie`, `venta`.`numcorrelativo`
            """)
            rows = cursor.fetchall()
            
        request.session.get('idusuario')

        return render(request, 'venta/venta.html', {'resultados': rows,"permisos":permisos})
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

        #TIpo documento
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT d.nombredepartamento, ti.id_tipo_igv, ti.tipo_igv
                FROM facsiswave.detalletipoigvxdepartamento dp
                INNER JOIN tipo_igvs ti ON ti.id_tipo_igv = dp.id_tipo_igv
                INNER JOIN departamentos d ON d.iddepartamentos = dp.iddepartamentos
                WHERE d.iddepartamentos = %s
            """, [id_departamento])
            rows = cursor.fetchall()
        
        data = {
            "tipoDocumentos": tipo_documentos,
            "unidades": unidades,
            "tipoClientes": tipo_cliente,
            'rows':rows,
            "modoPagos":modoPago,
            "permisos":permisos
        }
        return render(request, 'venta/agregarVenta.html', data)


def buscarSerie(request):

    doc = request.POST.get('doc')  # Acceder al valor 'doc' enviado por AJAX
    get_numserie = Numserie.objects.filter(idtipodocumento=doc, estado=1, idusuario=request.session.get('idusuario'))
    serie_list = list(get_numserie.values())
    return JsonResponse(serie_list, safe=False)


def buscarProducto(request):

    if request.method == 'POST':
        busqueda = request.POST.get('busqueda')
        
        productos = Producto.objects.filter(nomproducto__icontains=busqueda, estado=1)
        unidad = Unidades.objects.filter(idunidad=productos[0].idunidad.idunidad)
        
        unidad_list= list(unidad.values())
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
    return JsonResponse(perosna_info, safe=False)


def ruc(request):

    doc = request.POST.get('doc')
    print(doc)
    APIS_TOKEN = 'apis-token-7422.K4qsT4qnQsAvf7Eb6rovatLjtysiiCge'
    api_consultas = ApisNetPe(APIS_TOKEN)
    empresa_info = api_consultas.get_company(doc)
    return JsonResponse(empresa_info, safe=False)


def guardarVenta(request):
    #Datos totales
    totalGravada = request.POST.get('totalGravada')
    totalExonerada = request.POST.get('totalExonerada')
    totalIgv = request.POST.get('totalIgv')
    ventaTotal = request.POST.get('ventaTotal')
    

    #Obtener fecha actual
    fechaNow = date.today()
    
    # cliente
    docCliente = request.POST.get('doccliente')
    tipoCliente = request.POST.get('tipoCliente')
    nomcliente = request.POST.get('nomcliente')
    direccionCliente = request.POST.get('direccion')
    tipoPago = request.POST.get('tipoPago')
    
    #Para tipo pago 
    getTipoPago = Modopago.objects.get(idmodoPago=tipoPago)
    
    #Para tipo entidad, dni o ruc
    tipo_entidad = 0
    if int(tipoCliente) == 1:
        tipo_entidad = 2
        
    elif int(tipoCliente) == 2:   
        tipo_entidad = 1

    # Documento
    tipoDocumento = request.POST.get('tipoDocumento')
    serie = request.POST.get('serie')
    placa = request.POST.get('placa')
    # fechDocumento = request.POST.get('fechDocumento')

    productos = request.POST.getlist('producto[nombre][]')
    unidades = request.POST.getlist('producto[unidad][]')
    cantidades = request.POST.getlist('producto[cantidad][]')
    precio_unitarios = request.POST.getlist('producto[precioUnitario][]')
    sub_totales = request.POST.getlist('producto[subTotal][]')

    #Tipo igv
    tipo_igv = request.POST.get('tipo_igv')
    
    getTipoIgv = TipoIgv.objects.get(id_tipo_igv=tipo_igv)
    
    #Empresa
    getEmpresa = Empresa.objects.get(idempresa=1)
    
    # Obtener el numero correlativo y sumarlo +1
    GetNumcorrelativo = Venta.objects.filter(
        idnumserie=serie).order_by('-numcorrelativo').first()

    intNumcorrelativo = int(GetNumcorrelativo.numcorrelativo)+1

    num_ceros = len(str(GetNumcorrelativo.numcorrelativo))

    nuevo_numcorrelativo = "{:0{}}".format(intNumcorrelativo, num_ceros)

    productos_sin_stock = []

    for nombre, cantidad in zip(productos, cantidades):
        obtener_producto = Producto.objects.filter(nomproducto=nombre).first()
        
        if obtener_producto:
            stockActual = obtener_producto.stockactual

            if stockActual < int(cantidad):
                productos_sin_stock.append(obtener_producto.nomproducto)
        else:
            return JsonResponse({"error": f"Producto {nombre} no encontrado"})

    if productos_sin_stock:
        mensaje = "Falta stock para los siguientes productos:<br>-" + "<br>- ".join(productos_sin_stock)
        return JsonResponse({"mensaje": mensaje})
    

    # Obtener tipo cliente 
    tipo_cliente = Tipocliente.objects.get(idtipocliente=tipoCliente)
    #obtener tipo_entidad
    getTipo_entidad =  TipoEntidad.objects.get(id_tipo_entidad=tipo_entidad)
    #agregar cliente
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
                                        idempresa = getEmpresa,
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
        
        obtener_producto.stockactual = stockActual - int(cantidad_subtotal)
        obtener_producto.save()
        
        # precio_subtotal= cantidad_subtotal*precio_unitario #Tal vez
        VentaDetalle.objects.create(idventa=venta_creada, idproducto=obtener_producto,
                                    cantidad=cantidad_subtotal, preciosubtotal=sub_total)

    #Para transaccion
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
    
    return JsonResponse({"mensaje": "Venta exitosa"})


def eliminarVentas(request, id):

    Venta.objects.filter(idventa=id).update(estado=0)

    return redirect('ventas')


def editarVenta(request, id):
    id2 = request.session.get('idtipousuario')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        
        ventas = Venta.objects.get(pk=id)
        ventas_fechaemision = ventas.fechaemision.strftime('%Y-%m-%d')
        
        ventas_detalles = VentaDetalle.objects.filter(idventa=id)
        
        #Registro de la empresa
        empresa = Empresa.objects.filter(idempresa=1).first()
        
        id_departamento = str(empresa.ubigueo)[:2]

        #TIpo documento
        # with connection.cursor() as cursor:
        #     cursor.execute("""
        #         SELECT d.nombredepartamento, ti.id_tipo_igv, ti.tipo_igv
        #         FROM facsiswave.detalletipoigvxdepartamento dp
        #         INNER JOIN tipo_igvs ti ON ti.id_tipo_igv = dp.id_tipo_igv
        #         INNER JOIN departamentos d ON d.iddepartamentos = dp.iddepartamentos
        #         WHERE d.iddepartamentos = %s
        #     """, [id_departamento])
        #     rows = cursor.fetchall()
            
        # Formatear preciounitario en cada detalle de venta
        for detalle in ventas_detalles:
            detalle.preciounitario_formateado = str(detalle.idproducto.preciounitario).replace(',', '.')

        data = {
            'ventas': ventas,
            'ventas_detalles': ventas_detalles,
            'ventas_fechaemision': ventas_fechaemision,
            "permisos":permisos,
            # "rows":rows
        }

        return render(request, 'venta/editarVenta.html', data)
    

def guardarEditar(request):    
    #Datos totales
    totalGravada = request.POST.get('totalGravada')
    totalExonerada = request.POST.get('totalExonerada')
    totalIgv = request.POST.get('totalIgv')
    ventaTotal = request.POST.get('ventaTotal')
    
    #Cliente
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

    #Si ya existía el registro, edita, si no resta el stock del producto nuevo y agrega un nuevo registro de venta detalle
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
                #Sumo la cantidad antes puesta y resto el nuevo
                obtener_producto = Producto.objects.filter(nomproducto=nombre).first()
                stockActual = obtener_producto.stockactual + venta_detalle.cantidad
                obtener_producto.stockactual = stockActual - int(cantidad)
                obtener_producto.save()
                
                #Actualizo datos en el detalle
                venta_detalle.cantidad = cantidad_decimal
                venta_detalle.preciosubtotal = subtotal_decimal
                venta_detalle.save()
        #else:        
        if id_producto == '':
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
             
             

    #Cliente
    getCliente = Clientes.objects.get(idcliente=idCliente)
    getCliente.numdoc = docCliente
    getCliente.razonsocial = nomcliente
    getCliente.direccion = direccionCliente
    getCliente.save()
    #Editar totales de la venta
    venta.total_gravada =totalGravada
    venta.total_igv = totalIgv
    venta.total_exonerada = totalExonerada
    venta.total_a_pagar = ventaTotal
    venta.save()
    
    return redirect('ventas')


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
    # Recoger datos para envío a SUNAT
    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT 
                e.ruc as ruc,  
                e.razonsocial as razon_social, 
                e.nombrecomercial as nombre_comercial, 
                e.direccion as domicilio_fiscal, 
                e.ubigueo as ubigeo, 
                d.nombredistrito as distrito, 
                pr.nombreprovincia as provincia, 
                dp.nombredepartamento as departamento, 
                e.mododev as modo, 
                e.usersec as usu_secundario_produccion_user, 
                e.passwordsec as usu_secundario_produccion_password,

                c.razonsocial AS razon_social_nombres, 
                c.numdoc AS numero_documento, 
                te.codigo AS codigo_tipo_entidad,
                c.direccion AS cliente_direccion, 

                n.numserie as serie, 
                v.numcorrelativo as numero, 
                v.fechaemision as fecha_emision, 
                v.horaemision as hora_emision, 
                m.idmodoPago as forma_pago_id,
                v.total_gravada as total_gravada,
                v.total_igv as total_igv,
                v.total_exonerada as total_exonerada,
                v.total_inafecta as total_inafecta,
                tpD.codigosunat as tipo_documento_codigo,

                p.nomproducto as producto,
                vd.cantidad as cantidad,
                p.preciounitario as precio_base,
                p.codigo as codigo_sunat,
                p.codigo_barras as codigo_producto,
                u.codigounidad as codigo_unidad,
                igv.codigo as tipo_igv_codigo
            FROM 
                venta v
                INNER JOIN tipo_igvs igv ON igv.id_tipo_igv = v.id_tipo_igv
                INNER JOIN empresa e ON e.idempresa = v.idempresa
                INNER JOIN clientes c ON c.idcliente = v.idcliente
                INNER JOIN venta_detalle vd ON vd.idventa = v.idventa
                INNER JOIN producto p ON p.idproducto = vd.idproducto
                INNER JOIN unidades u ON u.idunidad = p.idunidad
                INNER JOIN numserie n ON n.idnumserie = v.idnumserie  
                INNER JOIN tipodocumento tpD ON tpD.idtipodocumento = n.idtipodocumento
                INNER JOIN modopago m ON m.idmodoPago = v.idmodoPago
                INNER JOIN distritos d ON e.iddistrito = d.iddistrito
                INNER JOIN provincias pr ON pr.idprovincia = d.idprovincia
                INNER JOIN departamentos dp ON dp.iddepartamentos = pr.iddepartamento
                INNER JOIN tipo_entidad te ON te.id_tipo_entidad = c.id_tipo_entidad
            WHERE
                v.idventa = %s;
        """, [id])
        
        rows = cursor.fetchall()

    # Inicializar la lista de items vacía
    items1 = []

    # Construir la lista de items
    for row in rows:
        item = {
            "producto": row[25],
            "cantidad": row[26],
            "precio_base": row[27],
            "codigo_sunat": row[28],
            "codigo_producto": row[29],
            "codigo_unidad": row[30],
            "tipo_igv_codigo": row[31]
        }
        items1.append(item)

    # Serializar fecha y hora
    fecha_emision = custom_json_serializer(rows[0][17])  # Convertir fecha_emision
    hora_emision = custom_json_serializer(rows[0][18])   # Convertir hora_emision

    # Envíar a SUNAT
    url = "http://localhost/API_SUNAT/post.php"
    payload = {
        "empresa": {
            "ruc": rows[0][0],
            "razon_social": rows[0][1],
            "nombre_comercial": rows[0][2],
            "domicilio_fiscal": rows[0][3],
            "ubigeo": rows[0][4],
            "urbanizacion": "",
            "distrito": rows[0][5],
            "provincia": rows[0][6],
            "departamento": rows[0][7],
            "modo": rows[0][8],
            "usu_secundario_produccion_user": rows[0][9],
            "usu_secundario_produccion_password": rows[0][10]
        },
        "cliente": {
            "razon_social_nombres": rows[0][11],
            "numero_documento": rows[0][12],
            "codigo_tipo_entidad": rows[0][13],
            "cliente_direccion": rows[0][14]
        },
        "venta": {
            "serie": rows[0][15],
            "numero": rows[0][16],
            "fecha_emision": fecha_emision,
            "hora_emision": hora_emision,
            "fecha_vencimiento": "",
            "moneda_id": "1",
            "forma_pago_id": rows[0][19],
            "total_gravada": rows[0][20],
            "total_igv": rows[0][21],
            "total_exonerada": rows[0][22],
            "total_inafecta": rows[0][23],
            "tipo_documento_codigo": rows[0][24],
            "nota": "notas o comentarios"
        },
        "items": items1  # Agregar la lista de items aquí
    }

    headers = {
        'Content-Type': 'application/json'
    }

    # Convertir payload a JSON
    payload_json = json.dumps(payload, default=custom_json_serializer)

    # Enviar solicitud a SUNAT
    response = requests.request("POST", url, headers=headers, data=payload_json)


    # Manejar la respuesta
    if response.status_code == 200:
        try:
            # Obtener el contenido de la respuesta como texto
            response_text = response.text

            # Variables para almacenar los valores encontrados
            respuesta_codigo = None
            respuesta_descripcion = None
            ruta_xml = None
            ruta_cdr = None
            ruta_pdf = None

            # Buscar el valor de respuesta_sunat_codigo
            if '"respuesta_sunat_codigo":"' in response_text:
                start_index = response_text.index('"respuesta_sunat_codigo":"') + len('"respuesta_sunat_codigo":"')
                end_index = response_text.index('"', start_index)
                respuesta_codigo = response_text[start_index:end_index]
                print("Respuesta SUNAT Código:", respuesta_codigo)
            else:
                print("No se encontró respuesta_sunat_codigo en la respuesta")

            # Buscar el valor de respuesta_sunat_descripcion
            if '"respuesta_sunat_descripcion":"' in response_text:
                start_index = response_text.index('"respuesta_sunat_descripcion":"') + len('"respuesta_sunat_descripcion":"')
                end_index = response_text.index('"', start_index)
                respuesta_descripcion = response_text[start_index:end_index]
                print("Respuesta SUNAT Descripción:", respuesta_descripcion)
            else:
                print("No se encontró respuesta_sunat_descripcion en la respuesta")

            # Buscar el valor de ruta_xml
            if '"ruta_xml":"' in response_text:
                start_index = response_text.index('"ruta_xml":"') + len('"ruta_xml":"')
                end_index = response_text.index('"', start_index)
                ruta_xml = response_text[start_index:end_index]
                print("Ruta XML:", ruta_xml)
            else:
                print("No se encontró ruta_xml en la respuesta")

            # Buscar el valor de ruta_cdr
            if '"ruta_cdr":"' in response_text:
                start_index = response_text.index('"ruta_cdr":"') + len('"ruta_cdr":"')
                end_index = response_text.index('"', start_index)
                ruta_cdr = response_text[start_index:end_index]
                print("Ruta CDR:", ruta_cdr)
            else:
                print("No se encontró ruta_cdr en la respuesta")

            # Buscar el valor de ruta_pdf
            if '"ruta_pdf":"' in response_text:
                start_index = response_text.index('"ruta_pdf":"') + len('"ruta_pdf":"')
                end_index = response_text.index('"', start_index)
                ruta_pdf = response_text[start_index:end_index]
                print("Ruta PDF:", ruta_pdf)
            else:
                print("No se encontró ruta_pdf en la respuesta")

            # Crear el objeto de respuesta adecuado
            response_data = {
                'respuesta_codigo': respuesta_codigo,
                'respuesta_descripcion': respuesta_descripcion,
                'ruta_xml': ruta_xml,
                'ruta_cdr': ruta_cdr,
                'ruta_pdf': ruta_pdf
            }
            
            getVenta = Venta.objects.get(idventa=id)
            getVenta.ruta_pdf = response_data['ruta_pdf']  # Accede usando corchetes
            getVenta.ruta_cdr = response_data['ruta_cdr']  # Accede usando corchetes
            getVenta.respuesta_sunat_descripcion = response_data['respuesta_descripcion']  # Accede usando corchetes
            getVenta.respuesta_sunat_codigo = response_data['respuesta_codigo']  # Accede usando corchetes
            getVenta.save()
            
            return JsonResponse(response_data, safe=False)

        except Exception as e:
            print(f"Error al manejar la respuesta: {e}")
            print("Contenido de la respuesta:", response.text)
            return HttpResponseServerError("Error en el servidor al procesar la respuesta de SUNAT")

    else:
        print(f"Error al enviar solicitud a SUNAT: {response.status_code}")
        print("Contenido de la respuesta:", response.text)
        return HttpResponseServerError("Error en el servidor al enviar la solicitud a SUNAT")


    return HttpResponse("request")


def pdf_ticket(request):
    # Datos estáticos para el ticket
    empresa = {
        'nombre': 'Empresa XYZ',
        'direccion': '123 Calle Principal',
        'telefono': '123-456-7890'
    }
    cabecera = {
        'fecha': '2024-07-16',
        'tipo_documento': 'Factura',
        'serie': 'F001',
        'numero': '0001',
        'total_a_pagar': '100.00',
        'moneda': 'USD'
    }
    total_letras = 'Son: Cien con 00/100 USD'

    # Crear el PDF
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="ticket.pdf"'

    # Tamaño de 80 mm x 200 mm
    width = 80 * 2.83
    height = 200 * 2.83
    p = canvas.Canvas(response, pagesize=(width, height))

    # Agregar imagen
    image_path = os.path.join(settings.BASE_DIR, 'static', 'img', 'empresa', 'logo.png')
    
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No se encontró la imagen en {image_path}")

    p.drawImage(image_path, 10, height - 100, width=60, height=60)  # Ajusta posición y tamaño

    # Agregar contenido al PDF
    p.drawString(10, height - 20, f"Ticket de Venta - {empresa['nombre']}")
    p.drawString(10, height - 40, f"Dirección: {empresa['direccion']}")
    p.drawString(10, height - 60, f"Teléfono: {empresa['telefono']}")
    p.drawString(10, height - 80, f"Fecha: {cabecera['fecha']}")
    p.drawString(10, height - 100, f"Tipo de Documento: {cabecera['tipo_documento']}")
    p.drawString(10, height - 120, f"Serie: {cabecera['serie']}")
    p.drawString(10, height - 140, f"Número: {cabecera['numero']}")
    p.drawString(10, height - 160, f"Total a Pagar: {cabecera['total_a_pagar']} {cabecera['moneda']}")
    p.drawString(10, height - 180, total_letras)

    p.showPage()
    p.save()

    return response