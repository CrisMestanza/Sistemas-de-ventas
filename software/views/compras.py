from datetime import datetime
from decimal import Decimal
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from software.models.comprasModel import Compras
from software.models.ProveedoresModel import Proveedores
from software.models.TipoclienteModel import Tipocliente
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
from software.models.LotesModel import Lotes
from software.models.empleadoModel import Empleado
from software.models.distritosModel import Distritos
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from software.models.detallecategoriaxunidadesModel import Detallecategoriaxunidades
from software.models.departamentosModel import Departamentos
from software.models.codigocorreoModel import CodigoCorreo
from software.models.clientesModel import Clientes
from django.db import connection
from openpyxl import Workbook
from openpyxl.utils import get_column_letter


import templates
# Create your views here.
from django.db.models import Sum


def compra(request):

    id2 = request.session.get('idtipousuario')
    if id2:

        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        resultados = Compras.objects.filter(estado=1).annotate(total=Sum('compradetalle__subtotal')).values(
            'idcompra', 'idproveedor', 'fechacompra', 'numcorrelativo', 'idproveedor__razonsocial', 'total'
        ).order_by(
            'idcompra', 'idproveedor', 'fechacompra'
        )

        # with connection.cursor() as cursor:
        #     cursor.execute("""
        #         SELECT `compras`.`idcompra`, `compras`.`idproveedor`, `compras`.`fechacompra`, `compras`.`numcorrelativo`, `proveedores`.`razonsocial`,
        #         SUM(`compra_detalle`.`subtotal`) AS `total`
        #         FROM `compras`
        #         LEFT OUTER JOIN `compra_detalle` ON (`compras`.`idcompra` = `compra_detalle`.`idcompra`)
        #         INNER JOIN `proveedores` ON (`compras`.`idproveedor` = `proveedores`.`idproveedor`)
        #         WHERE `compras`.`estado` = 1
        #         GROUP BY `compras`.`idcompra`, `compras`.`idproveedor`, `compras`.`numcorrelativo`, `compras`.`fechacompra`, `compras`.`estado`,
        #         `proveedores`.`razonsocial`
        #         ORDER BY `compras`.`idcompra` ASC, `compras`.`idproveedor` ASC, `compras`.`fechacompra` ASC;
        #     """)
        #     rows = cursor.fetchall()

        data = {
            'resultados': resultados,
            'permisos': permisos
        }

        return render(request, 'compras/compras.html', data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")


def eliminar(request, id):

    Compras.objects.filter(idcompra=id).update(estado=0)

    # Devuelve los datos JSON directamente sin redirigir
    return redirect('compras')


def agregar(request):
    id2 = request.session.get('idtipousuario')
    if id2:

        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        proveedores = Proveedores.objects.all()
        categorias = Categoria.objects.all()
        data = {
            'proveedores': proveedores,
            'categorias': categorias,
            'permisos': permisos
        }
        return render(request, 'compras/agregarCompras.html', data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")


def buscar(request):

    busqueda = request.POST['busqueda']

    productos = Producto.objects.all().filter(nomproducto__icontains=busqueda)
    # productos_list = [{'nomproducto': producto.nomproducto, 'preciounitario': producto.preciounitario} for producto in productos]
    productos_list = list(productos.values())
    return JsonResponse(productos_list, safe=False)


def guardar(request):
    if request.method == 'POST':
        # Obtener los datos de la compra
        numcorrelativo = request.POST.get('numcorrelativo')
        # Obtener el ID del proveedor desde el formulario
        proveedor_id = request.POST.get('proveedor')

        proveedor = Proveedores.objects.get(pk=proveedor_id)

        # get_object_or_404(Proveedores, pk=proveedor_id)  # Obtener la instancia del proveedor
        fechacompra = request.POST.get('fechDocumento')

        # Crear una instancia de CompraModel y guardar la compra
        compra = Compras.objects.create(
            numcorrelativo=numcorrelativo, idproveedor=proveedor, fechacompra=fechacompra, estado=1)

        # Obtener el ID de la compra recién creada
        id_insertado = compra.pk

        # Obtener los datos de los productos
        productos = request.POST.getlist('producto[nombre][]')
        identificadores = request.POST.getlist('producto[identificador][]')
        fecha_produccion = request.POST.getlist('producto[fecha_produccion][]')
        fecha_vencimiento = request.POST.getlist(
            'producto[fecha_vencimiento][]')
        stocks = request.POST.getlist('producto[stock][]')

        for nombre, identificadorPrimario, produccion, vencimiento, stock in zip(productos, identificadores, fecha_produccion, fecha_vencimiento, stocks):
            # Obtengo el producto
            producto_existente = Producto.objects.filter(
                nomproducto=nombre).first()

            if producto_existente:
                # Agregar stock
                nuevo_stock = producto_existente.stockactual + float(stock)
                producto_existente.stockactual = nuevo_stock
                producto_existente.save()

                compraDetalleId = CompraDetalle.objects.create(idcompra_id=id_insertado, idproducto=producto_existente, cantidad=float(
                    stock), subtotal=producto_existente.preciounitario * float(stock))

                # Agregar datos del lote
                Lotes.objects.create(
                    idcompradetalle=compraDetalleId,
                    idproducto=producto_existente,
                    identificador=identificadorPrimario,
                    fecha_produccion=produccion,
                    fecha_vencimiento=vencimiento,
                    cantidad=float(stock))

        return redirect('/compras')
    else:
        return JsonResponse({'message': 'Método no permitido'}, status=405)


def editar(request, id):
    compras = Compras.objects.get(pk=id)
    compras_fechacompra = compras.fechacompra.strftime('%Y-%m-%d')
    proveedores = Proveedores.objects.all()
    compra_detalle = CompraDetalle.objects.filter(idcompra=id)

    lotes = []
    for detalle in compra_detalle:
        # Filtrar los lotes para cada detalle de compra
        lotes_detalle = Lotes.objects.filter(
            idcompradetalle=detalle.idcompradetalle)
        # Agregar los lotes al listado general de lotes
        lotes.extend(lotes_detalle)

    data = {
        'compras': compras,
        'compras_fechacompra': compras_fechacompra,
        'proveedores': proveedores,
        'lotes': lotes
    }
    return render(request, 'compras/editarCompra.html', data)


def editado(request):
    if request.method == 'POST':
        # Obtener los datos de la compra
        numcorrelativo = request.POST['numcorrelativo']
        fechacompra = request.POST['fechDocumento']
        id_compra = request.POST['idCompra']

        # Actualizar los datos de la compra
        Compras.objects.filter(idcompra=id_compra).update(
            numcorrelativo=numcorrelativo,  fechacompra=fechacompra)

        # Obtener los datos de los productos
        productos = request.POST.getlist('producto[nombre][]')
        identificadores = request.POST.getlist('producto[identificador][]')
        fecha_produccion = request.POST.getlist('producto[fecha_produccion][]')
        fecha_vencimiento = request.POST.getlist(
            'producto[fecha_vencimiento][]')
        stocks = request.POST.getlist('producto[stock][]')
        idProductos = request.POST.getlist('producto[idproducto][]')

        for i, (nombre, identificadorPrimario, produccion, vencimiento, stock, idProducto) in enumerate(zip(productos, identificadores, fecha_produccion, fecha_vencimiento, stocks, idProductos)):
            # Si modifico un registro de la compra existente
            if idProducto:

                registro_compra = CompraDetalle.objects.get(
                    idcompra=id_compra, idproducto=idProducto)

                if registro_compra:

                    # Stock de la tabla detalle del producto relazacionado con la compra
                    cantidad_registro = registro_compra.cantidad

                    # Obtengo el producto
                    producto_registro = Producto.objects.get(
                        idproducto=idProducto)

                    # Obtengo el stock actual del producto
                    stock_actual = producto_registro.stockactual

                    # Resto el stock de producto con la cantidad de compraDetalle y sumo el nuevo stock
                    stock_actualizada = float(
                        stock_actual) - float(cantidad_registro) + float(stock)

                    precio_unitario = producto_registro.preciounitario

                    # Sumo el nuevo valor
                    producto_registro.stockactual = stock_actualizada
                    producto_registro.save()

                    # actualizo la cantidad de compraDetalle
                    registro_compra.cantidad = float(stock)
                    registro_compra.subtotal = precio_unitario*float(stock)
                    registro_compra.save()

                    # #Actualizar datos del lote como compraDetalle trae mas de 1 resultado a veces tengo que acceder a cada uno con un indice
                    compra_detalle = CompraDetalle.objects.filter(
                        idcompra=id_compra)

                    detalleCompra = compra_detalle[i]

                    # Filtrar los lotes para cada detalle de compra
                    lote = Lotes.objects.get(
                        idcompradetalle=detalleCompra.idcompradetalle)

                    lote.identificador = identificadorPrimario
                    lote.fecha_produccion = produccion
                    lote.fecha_vencimiento = vencimiento
                    lote.cantidad = stock
                    lote.save()

            # Se agrega un nuevo registro de lote
            else:
                # Obtengo el producto
                producto_existente = Producto.objects.filter(
                    nomproducto=nombre).first()

                if producto_existente:
                    # Agregar stock
                    nuevo_stock = producto_existente.stockactual + float(stock)
                    producto_existente.stockactual = nuevo_stock
                    producto_existente.save()

                    compraDetalleId = CompraDetalle.objects.create(idcompra_id=id_compra, idproducto=producto_existente, cantidad=float(
                        stock), subtotal=producto_existente.preciounitario * float(stock))

                    # Agregar datos del lote
                    Lotes.objects.create(
                        idcompradetalle=compraDetalleId,
                        idproducto=producto_existente,
                        identificador=identificadorPrimario,
                        fecha_produccion=produccion,
                        fecha_vencimiento=vencimiento,
                        cantidad=float(stock))

    return redirect('compras')


def buscarFecha(request):

    fecha_inicio = request.POST.get('fechaInicio')
    fecha_fin = request.POST.get('fechaFin')

    resultados = Compras.objects.filter(
        estado=1,
        # Filtrar por rango de fechas
        fechacompra__range=(fecha_inicio, fecha_fin)
    ).annotate(
        total=Sum('compradetalle__subtotal')
    ).values(
        'idcompra', 'idproveedor', 'fechacompra', 'numcorrelativo', 'idproveedor__razonsocial', 'total'
    ).order_by(
        'idcompra', 'idproveedor', 'fechacompra', 'idproveedor__razonsocial', 'numcorrelativo'
    )

    resultado_json = list(resultados)
    return JsonResponse(resultado_json, safe=False)


def export_compras_to_excel(request):
    # Obtener datos de compras con el total calculado
    compras = Compras.objects.filter(estado=1).annotate(
        total=Sum('compradetalle__subtotal')
    ).values(
        'idcompra', 'idproveedor__razonsocial', 'numcorrelativo', 'fechacompra', 'total'
    ).order_by(
        'idcompra', 'idproveedor', 'fechacompra'
    )

    # Crear un workbook de Excel
    workbook = Workbook()
    sheet = workbook.active
    sheet.title = "Compras"

    # Crear la fila de encabezado
    headers = ["ID", "Número Correlativo",
               "Proveedor", "Total", "Fecha de Compra"]
    sheet.append(headers)
    # Ajustar el ancho de la columna de fecha
    fecha_columna = sheet.column_dimensions['E']
    fecha_columna.width = 15  # Puedes ajustar este valor según sea necesario

    # Agregar datos de compras
    for compra in compras:
        # Formatear la fecha como cadena antes de agregarla al Excel
        fecha_compra = compra['fechacompra'].strftime("%d/%m/%Y")
        sheet.append([
            compra['idcompra'],
            compra['numcorrelativo'],
            compra['idproveedor__razonsocial'],
            compra['total'],
            fecha_compra
        ])

    # Configurar la respuesta HTTP
    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=compras.xlsx'

    # Guardar el workbook en la respuesta
    workbook.save(response)

    return response
