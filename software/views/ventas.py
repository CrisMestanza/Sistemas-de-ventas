import decimal
from datetime import datetime, date, time
from decimal import Decimal
from django.db import connection
from software.views.apiBusquedaRUcDni import ApisNetPe
from django.http import HttpResponse, JsonResponse, HttpResponseServerError
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
from django.db.models import Q, Sum
from django.db.models.functions import Trim
from openpyxl.utils import get_column_letter

from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.graphics.barcode.qr import QrCodeWidget
from reportlab.graphics.shapes import Drawing
from reportlab.graphics import renderPDF
import os
from django.conf import settings
from django.templatetags.static import static
from PIL import Image


# Create your views here.
import requests
import json


def _to_decimal(value):
    if value in (None, ''):
        return Decimal('0.00')
    return Decimal(str(value)).quantize(Decimal('0.01'))


def _to_float(value):
    return float(_to_decimal(value))


def _extract_json_response(response_text):
    decoder = json.JSONDecoder()

    for index, char in enumerate(response_text):
        if char != '{':
            continue

        try:
            parsed, _ = decoder.raw_decode(response_text[index:])
            return parsed
        except json.JSONDecodeError:
            continue

    raise ValueError('La respuesta de la API no contiene JSON valido')


def _buscar_producto_por_nombre_o_barra(valor):
    valor = str(valor or '').strip()
    if not valor:
        return None

    producto = Producto.objects.filter(
        Q(nomproducto__iexact=valor) | Q(codigo_barras__iexact=valor),
        estado=1,
    ).first()
    if producto:
        return producto

    return Producto.objects.annotate(
        nomproducto_limpio=Trim('nomproducto'),
        codigo_barras_limpio=Trim('codigo_barras'),
    ).filter(
        Q(nomproducto_limpio__iexact=valor) | Q(codigo_barras_limpio__iexact=valor),
        estado=1,
    ).first()


def _find_empresa_logo(empresa):
    logo_candidates = []
    if getattr(empresa, 'logo', None):
        logo_candidates.append(os.path.join(settings.BASE_DIR, empresa.logo))
        logo_candidates.append(os.path.join(settings.BASE_DIR, 'static', empresa.logo))
        logo_candidates.append(os.path.join(settings.BASE_DIR, 'static', 'img', 'empresa', empresa.logo))

    empresa_img_dir = os.path.join(settings.BASE_DIR, 'static', 'img', 'empresa')
    logo_candidates.append(os.path.join(empresa_img_dir, 'logo.png'))

    if os.path.isdir(empresa_img_dir):
        for filename in os.listdir(empresa_img_dir):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
                logo_candidates.append(os.path.join(empresa_img_dir, filename))

    for logo_path in logo_candidates:
        if logo_path and os.path.exists(logo_path):
            return logo_path
    return None


def _prepare_ticket_logo(logo_path):
    if not logo_path:
        return None

    cache_dir = os.path.join(settings.MEDIA_ROOT, 'tickets', 'cache')
    os.makedirs(cache_dir, exist_ok=True)
    cache_path = os.path.join(cache_dir, 'empresa_logo_ticket.png')

    try:
        if os.path.exists(cache_path) and os.path.getmtime(cache_path) >= os.path.getmtime(logo_path):
            return cache_path

        previous_max_pixels = Image.MAX_IMAGE_PIXELS
        Image.MAX_IMAGE_PIXELS = None
        try:
            with Image.open(logo_path) as image:
                image.thumbnail((600, 300), Image.LANCZOS)
                if image.mode not in ('RGB', 'RGBA'):
                    image = image.convert('RGBA')
                image.save(cache_path, format='PNG', optimize=True)
        finally:
            Image.MAX_IMAGE_PIXELS = previous_max_pixels

        return cache_path
    except Exception as e:
        print(f"No se pudo preparar el logo del ticket: {e}")
        return None


def _draw_wrapped_text(pdf, text, x, y, max_width, font_name='Helvetica', font_size=7, leading=8):
    text = str(text or '').strip()
    if not text:
        return y

    line = ''
    pdf.setFont(font_name, font_size)
    for word in text.split():
        test_line = f'{line} {word}'.strip()
        if pdf.stringWidth(test_line, font_name, font_size) <= max_width:
            line = test_line
        else:
            pdf.drawString(x, y, line)
            y -= leading
            line = word

    if line:
        pdf.drawString(x, y, line)
        y -= leading
    return y


def _draw_centered_wrapped_text(pdf, text, y, max_width, page_width, font_name='Helvetica-Bold', font_size=8, leading=9):
    text = str(text or '').strip()
    if not text:
        return y

    lines = []
    line = ''
    for word in text.split():
        test_line = f'{line} {word}'.strip()
        if pdf.stringWidth(test_line, font_name, font_size) <= max_width:
            line = test_line
        else:
            lines.append(line)
            line = word
    if line:
        lines.append(line)

    pdf.setFont(font_name, font_size)
    for line in lines:
        pdf.drawCentredString(page_width / 2, y, line)
        y -= leading
    return y


def _sunat_qr_text(venta):
    return '|'.join([
        str(venta.idempresa.ruc),
        str(venta.idnumserie.idtipodocumento.codigosunat),
        str(venta.idnumserie.numserie),
        str(venta.numcorrelativo),
        f'{_to_decimal(venta.total_igv):.2f}',
        f'{_to_decimal(venta.total_a_pagar):.2f}',
        venta.fechaemision.strftime('%Y-%m-%d'),
        str(venta.idcliente.id_tipo_entidad.codigo),
        str(venta.idcliente.numdoc),
        str(venta.respuesta_sunat_codigo or ''),
        '',
    ])


def generar_ticket_pdf_venta(venta):
    detalles = VentaDetalle.objects.filter(idventa=venta).select_related('idproducto')
    tipo_documento_codigo = venta.idnumserie.idtipodocumento.codigosunat
    tipo_documento_nombre = venta.idnumserie.idtipodocumento.nombredocumento
    carpeta_documento = {
        '01': 'facturas',
        '03': 'boletas',
    }.get(str(tipo_documento_codigo), 'otros')

    tickets_dir = os.path.join(settings.MEDIA_ROOT, 'tickets', carpeta_documento)
    os.makedirs(tickets_dir, exist_ok=True)

    nombre_archivo = (
        f'{venta.idempresa.ruc}-{tipo_documento_codigo}-'
        f'{venta.idnumserie.numserie}-{venta.numcorrelativo}.pdf'
    )
    ruta_absoluta = os.path.join(tickets_dir, nombre_archivo)
    ruta_url = f'{settings.MEDIA_URL}tickets/{carpeta_documento}/{nombre_archivo}'

    page_width = 80 * mm
    page_height = max(230 * mm, (185 + (detalles.count() * 14)) * mm)
    margin_x = 5 * mm
    y = page_height - 6 * mm
    pdf = canvas.Canvas(ruta_absoluta, pagesize=(page_width, page_height))
    pdf.setTitle(f'Ticket {venta.idnumserie.numserie}-{venta.numcorrelativo}')

    logo_path = _prepare_ticket_logo(_find_empresa_logo(venta.idempresa))
    if logo_path:
        try:
            pdf.drawImage(
                logo_path,
                (page_width - 34 * mm) / 2,
                y - 18 * mm,
                width=34 * mm,
                height=16 * mm,
                preserveAspectRatio=True,
                mask='auto',
            )
            y -= 22 * mm
        except Exception as e:
            print(f"No se pudo agregar el logo al ticket: {e}")

    y = _draw_centered_wrapped_text(pdf, venta.idempresa.razonsocial, y, page_width - 10 * mm, page_width)
    y = _draw_centered_wrapped_text(pdf, f'RUC: {venta.idempresa.ruc}', y, page_width - 10 * mm, page_width, font_size=7)
    y = _draw_centered_wrapped_text(pdf, venta.idempresa.direccion, y, page_width - 10 * mm, page_width, font_name='Helvetica', font_size=7)
    if getattr(venta.idempresa, 'telefono', None):
        y = _draw_centered_wrapped_text(pdf, f'Tel: {venta.idempresa.telefono}', y, page_width - 10 * mm, page_width, font_name='Helvetica', font_size=7)

    y -= 2 * mm
    pdf.line(margin_x, y, page_width - margin_x, y)
    y -= 5 * mm
    pdf.setFont('Helvetica-Bold', 9)
    pdf.drawCentredString(page_width / 2, y, tipo_documento_nombre.upper())
    y -= 4 * mm
    pdf.drawCentredString(page_width / 2, y, f'{venta.idnumserie.numserie}-{venta.numcorrelativo}')
    y -= 6 * mm

    pdf.setFont('Helvetica', 7)
    pdf.drawString(margin_x, y, f'Fecha: {venta.fechaemision.strftime("%d/%m/%Y")} {venta.horaemision}')
    y -= 4 * mm
    pdf.drawString(margin_x, y, f'Forma de pago: {venta.idmodoPago.modo_pago}')
    y -= 4 * mm
    pdf.drawString(margin_x, y, f'Cliente: {venta.idcliente.razonsocial}')
    y -= 4 * mm
    pdf.drawString(margin_x, y, f'Doc: {venta.idcliente.numdoc}')
    y -= 4 * mm
    y = _draw_wrapped_text(pdf, f'Dir: {venta.idcliente.direccion}', margin_x, y, page_width - 10 * mm)

    y -= 1 * mm
    pdf.line(margin_x, y, page_width - margin_x, y)
    y -= 4 * mm
    pdf.setFont('Helvetica-Bold', 6.5)
    pdf.drawString(margin_x, y, 'Cant')
    pdf.drawString(margin_x + 15 * mm, y, 'Descripcion')
    pdf.drawRightString(page_width - margin_x, y, 'Importe')
    y -= 4 * mm
    pdf.setFont('Helvetica', 6.5)

    for detalle in detalles:
        cantidad = _to_decimal(detalle.cantidad)
        precio_unitario = _to_decimal(detalle.idproducto.preciounitario)
        subtotal = _to_decimal(detalle.preciosubtotal)
        y = _draw_wrapped_text(pdf, detalle.idproducto.nomproducto, margin_x + 15 * mm, y, page_width - 30 * mm, font_size=6.5, leading=7)
        pdf.drawString(margin_x, y + 7, f'{cantidad:g}')
        pdf.drawString(margin_x + 15 * mm, y, f'P.U. {precio_unitario:.2f}')
        pdf.drawRightString(page_width - margin_x, y, f'{subtotal:.2f}')
        y -= 5 * mm

    pdf.line(margin_x, y, page_width - margin_x, y)
    y -= 5 * mm
    pdf.setFont('Helvetica', 7)
    pdf.drawRightString(page_width - margin_x - 22 * mm, y, 'Op. Gravada:')
    pdf.drawRightString(page_width - margin_x, y, f'{_to_decimal(venta.total_gravada):.2f}')
    y -= 4 * mm
    pdf.drawRightString(page_width - margin_x - 22 * mm, y, 'Op. Exonerada:')
    pdf.drawRightString(page_width - margin_x, y, f'{_to_decimal(venta.total_exonerada):.2f}')
    y -= 4 * mm
    pdf.drawRightString(page_width - margin_x - 22 * mm, y, 'IGV:')
    pdf.drawRightString(page_width - margin_x, y, f'{_to_decimal(venta.total_igv):.2f}')
    y -= 5 * mm
    pdf.setFont('Helvetica-Bold', 9)
    pdf.drawRightString(page_width - margin_x - 22 * mm, y, 'TOTAL S/:')
    pdf.drawRightString(page_width - margin_x, y, f'{_to_decimal(venta.total_a_pagar):.2f}')
    y -= 8 * mm

    qr_code = QrCodeWidget(_sunat_qr_text(venta))
    qr_bounds = qr_code.getBounds()
    qr_width = qr_bounds[2] - qr_bounds[0]
    qr_height = qr_bounds[3] - qr_bounds[1]
    qr_size = 28 * mm
    qr_drawing = Drawing(qr_size, qr_size, transform=[qr_size / qr_width, 0, 0, qr_size / qr_height, 0, 0])
    qr_drawing.add(qr_code)
    renderPDF.draw(qr_drawing, pdf, (page_width - qr_size) / 2, y - qr_size)
    y -= qr_size + 4 * mm

    pdf.setFont('Helvetica', 6.5)
    pdf.drawCentredString(page_width / 2, y, 'Representacion impresa del comprobante electronico')
    y -= 4 * mm
    pdf.drawCentredString(page_width / 2, y, 'Consulte su comprobante con el codigo QR')

    pdf.showPage()
    pdf.save()
    return ruta_url


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
            cursor.execute("""
                SELECT id_tipo_igv, codigo, tipo_igv
                FROM facsiswave.tipo_igvs
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
        busqueda = str(request.POST.get('busqueda') or '').strip()

        if not busqueda:
            return JsonResponse({
                'productos': [],
                'unidad': [],
                'producto_exacto': None,
            }, safe=False)

        productos = Producto.objects.filter(
            Q(nomproducto__icontains=busqueda) | Q(codigo_barras__icontains=busqueda),
            estado=1,
        ).order_by('nomproducto')

        producto_exacto = Producto.objects.filter(
            Q(nomproducto__iexact=busqueda) | Q(codigo_barras__iexact=busqueda),
            estado=1,
        ).first()

        producto_unidad = producto_exacto or productos.first()
        unidad = Unidades.objects.filter(
            idunidad=producto_unidad.idunidad.idunidad) if producto_unidad else Unidades.objects.none()

        unidad_list = list(unidad.values())
        productos_list = list(productos.values())
        producto_exacto_data = {
            'idproducto': producto_exacto.idproducto,
            'nomproducto': producto_exacto.nomproducto,
            'preciounitario': producto_exacto.preciounitario,
            'stockactual': producto_exacto.stockactual,
            'codigo_barras': producto_exacto.codigo_barras,
            'idunidad': producto_exacto.idunidad.idunidad,
        } if producto_exacto else None

        response_data = {
            'productos': productos_list,
            'unidad': unidad_list,
            'producto_exacto': producto_exacto_data,
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

    # ss
    serie = request.POST.get('serie')

    # Documento
    tipoDocumento = request.POST.get('tipoDocumento')
    if not tipoDocumento and serie:
        serie_documento = Numserie.objects.filter(
            idnumserie=serie
        ).select_related('idtipodocumento').first()
        if serie_documento:
            tipoDocumento = serie_documento.idtipodocumento
    print("Tipo de documento: ", tipoDocumento)

    placa = request.POST.get('placa')
    # fechDocumento = request.POST.get('fechDocumento')

    productos = [
        str(producto or '').strip()
        for producto in request.POST.getlist('producto[nombre][]')
    ]
    unidades = request.POST.getlist('producto[unidad][]')
    cantidades = request.POST.getlist('producto[cantidad][]')
    precio_unitarios = request.POST.getlist('producto[precioUnitario][]')
    sub_totales = request.POST.getlist('producto[subTotal][]')
    print(f"Productos: {productos}")
    # Tipo igv
    tipo_igv = request.POST.get('tipo_igv')

    getTipoIgv = TipoIgv.objects.get(id_tipo_igv=tipo_igv)
    subtotal_productos = sum((_to_decimal(sub_total) for sub_total in sub_totales), Decimal('0.00'))

    if not totalGravada and not totalExonerada and not totalIgv and not ventaTotal:
        if getTipoIgv.codigo == '10':
            totalGravada = subtotal_productos
            totalIgv = (subtotal_productos * Decimal('0.18')).quantize(Decimal('0.01'))
            totalExonerada = Decimal('0.00')
            ventaTotal = totalGravada + totalIgv
        elif getTipoIgv.codigo == '20':
            totalGravada = Decimal('0.00')
            totalIgv = Decimal('0.00')
            totalExonerada = subtotal_productos
            ventaTotal = subtotal_productos
        elif getTipoIgv.codigo == '30':
            totalGravada = Decimal('0.00')
            totalIgv = Decimal('0.00')
            totalExonerada = Decimal('0.00')
            ventaTotal = subtotal_productos

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
        obtener_producto = _buscar_producto_por_nombre_o_barra(nombre)

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
    print("Tipo cliente primero:", tipo_cliente.nomtipocliente)
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
                                        total_gravada=_to_decimal(totalGravada),
                                        total_igv=_to_decimal(totalIgv),
                                        total_gratuita=Decimal('0.00'),
                                        total_exonerada=_to_decimal(totalExonerada),
                                        total_inafecta=Decimal('0.00'),
                                        total_a_pagar=_to_decimal(ventaTotal),
                                        ruta_pdf='',
                                        ruta_ticket='',
                                        ruta_cdr='',
                                        ruta_xml='',
                                        respuesta_sunat_descripcion='',
                                        respuesta_sunat_codigo='',
                                        api_id=0)

    # new_list= zip(productos,unidades,cantidades,precio_unitarios,sub_totales)

    for nombre, cantidad_subtotal, sub_total in zip(productos, cantidades, sub_totales):

        obtener_producto = _buscar_producto_por_nombre_o_barra(nombre)
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

    if ultimo_registro:
        caja = Caja.objects.get(id_caja=ultimo_registro.id_caja)
        tipoTransaccion = TipoTransaccion.objects.get(id_tipo_transaccion=1)

        transaccion = Transaccion()
        transaccion.id_caja = caja
        transaccion.id_tipo_transaccion = tipoTransaccion
        transaccion.monto = _to_decimal(ventaTotal)
        transaccion.fecha = fechaNow
        transaccion.hora = hora_actual_formateada
        transaccion.save()

    venta_creada.ruta_ticket = generar_ticket_pdf_venta(venta_creada)
    venta_creada.save(update_fields=['ruta_ticket'])


    return JsonResponse({
        "mensaje": "Venta exitosa",
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
        obtener_producto = _buscar_producto_por_nombre_o_barra(nombre)

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
                obtener_producto = _buscar_producto_por_nombre_o_barra(nombre)
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
            producto = _buscar_producto_por_nombre_o_barra(nombre)
            if not producto:
                return JsonResponse({"error": f"Producto {nombre} no encontrado"})
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
    venta = Venta.objects.select_related(
        'idempresa__iddistrito__idprovincia__iddepartamento',
        'idcliente__id_tipo_entidad',
        'idnumserie__idtipodocumento',
        'idmodoPago',
        'id_tipo_igv',
    ).get(idventa=id)
    detalles = VentaDetalle.objects.filter(idventa=venta).select_related(
        'idproducto__idunidad')

    empresa = venta.idempresa
    distrito = empresa.iddistrito
    provincia = distrito.idprovincia
    departamento = provincia.iddepartamento
    tipo_igv_codigo = str(venta.id_tipo_igv.codigo)

    try:
        numero = int(str(venta.numcorrelativo).lstrip('0') or '0')
    except ValueError:
        numero = venta.numcorrelativo

    items = []
    for detalle in detalles:
        producto = detalle.idproducto
        items.append({
            "producto": producto.nomproducto,
            "cantidad": _to_float(detalle.cantidad),
            "precio_base": _to_float(producto.preciounitario),
            "codigo_sunat": producto.codigo or "-",
            "codigo_producto": producto.codigo_barras or str(producto.idproducto),
            "codigo_unidad": producto.idunidad.codigounidad,
            "tipo_igv_codigo": tipo_igv_codigo,
        })

    payload = {
        "empresa": {
            "ruc": empresa.ruc,
            "razon_social": empresa.razonsocial,
            "nombre_comercial": empresa.nombrecomercial,
            "domicilio_fiscal": empresa.direccion,
            "ubigeo": empresa.ubigueo,
            "urbanizacion": getattr(empresa, 'urbanizacion', '') or "",
            "distrito": distrito.nombredistrito,
            "provincia": provincia.nombreprovincia,
            "departamento": departamento.nombredepartamento,
            "modo": str(empresa.mododev),
            "usu_secundario_produccion_user": empresa.usersec,
            "usu_secundario_produccion_password": empresa.passwordsec,
        },
        "cliente": {
            "razon_social_nombres": venta.idcliente.razonsocial,
            "numero_documento": venta.idcliente.numdoc,
            "codigo_tipo_entidad": venta.idcliente.id_tipo_entidad.codigo,
            "cliente_direccion": venta.idcliente.direccion,
        },
        "venta": {
            "serie": venta.idnumserie.numserie,
            "numero": numero,
            "fecha_emision": custom_json_serializer(venta.fechaemision),
            "hora_emision": custom_json_serializer(venta.horaemision),
            "moneda_id": 1,
            "forma_pago_id": venta.idmodoPago.idmodoPago,
            "total_gravada": _to_float(venta.total_gravada),
            "total_igv": _to_float(venta.total_igv),
            "total_exonerada": _to_float(venta.total_exonerada),
            "total_inafecta": _to_float(venta.total_inafecta),
            "tipo_documento_codigo": venta.idnumserie.idtipodocumento.codigosunat,
            "nota": "notas o comentarios",
        },
        "items": items,
    }

    payload_debug = json.loads(json.dumps(payload, default=custom_json_serializer))
    payload_debug["empresa"]["usu_secundario_produccion_password"] = "***"
    print("Payload enviado a SUNAT:", json.dumps(
        payload_debug, ensure_ascii=False, indent=2))

    try:
        response = requests.post(
            "http://localhost/API_SUNAT/post.php",
            headers={"Content-Type": "application/json"},
            data=json.dumps(payload, default=custom_json_serializer),
            timeout=60,
        )
        response_json = _extract_json_response(response.text)
        response_data = response_json.get("data", response_json)

        respuesta_sunat_codigo = response_data.get("respuesta_sunat_codigo", "")
        respuesta_sunat_descripcion = response_data.get(
            "respuesta_sunat_descripcion", "")
        ruta_xml = response_data.get("ruta_xml", "")
        ruta_cdr = response_data.get("ruta_cdr", "")
        ruta_pdf = response_data.get("ruta_pdf", "")

        venta.respuesta_sunat_codigo = respuesta_sunat_codigo or ""
        venta.respuesta_sunat_descripcion = respuesta_sunat_descripcion or ""
        venta.ruta_xml = ruta_xml or ""
        venta.ruta_cdr = ruta_cdr or ""
        if ruta_pdf:
            venta.ruta_pdf = ruta_pdf
        venta.save(update_fields=[
            "respuesta_sunat_codigo",
            "respuesta_sunat_descripcion",
            "ruta_xml",
            "ruta_cdr",
            "ruta_pdf",
        ])

        status = 200 if response.status_code == 200 and respuesta_sunat_codigo == "0" else 400
        return JsonResponse({
            "respuesta_sunat_codigo": respuesta_sunat_codigo,
            "respuesta_sunat_descripcion": respuesta_sunat_descripcion,
            "ruta_xml": ruta_xml,
            "ruta_cdr": ruta_cdr,
            "ruta_pdf": ruta_pdf,
            "codigo_hash": response_data.get("codigo_hash", ""),
        }, status=status)

    except Exception as e:
        print("Error enviando a SUNAT:", e)
        if 'response' in locals():
            print("Contenido de la respuesta:", response.text)
        return JsonResponse({
            "error": str(e)
        }, status=500)
