
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
from software.models.LotesModel import Lotes
from software.models.TipousuarioModel import Tipousuario
from software.models.TipodocumentoModel import Tipodocumento
from software.models.TipoclienteModel import Tipocliente
from software.models.ProvinciasModel import Provincias
from software.models.ProveedoresModel import Proveedores
from software.models.NumserieModel import Numserie
from software.models.ModulosModel import Modulos
from software.models.empresaModel import Empresa
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
import re


# Create your views here.

def productos(request):
    id2 = request.session.get('idtipousuario')
    if id2:
        
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
        productos= Producto.objects.filter(estado=1)
        categoria = Categoria.objects.filter(estado=1)
        unidades = Unidades.objects.filter(estado=1)
        data = {
            'productos': productos,
            'categorias':categoria,
            'unidades': unidades,
            'permisos': permisos
        }
        return render(request, 'productos/productos.html',data)

def agregar(request):
    categoria = request.POST.get('categoria')
    nombreProducto = request.POST.get('nombreProducto')
    descripcionProducto = request.POST.get('descripcionProducto')
    precioCompraPost = request.POST.get('precioCompra')
    precioProducto = request.POST.get('precioProducto')
    stockProducto = request.POST.get('stockProducto')
    codigo1 = request.POST.get('codigo')
    codigo_barras1 =  request.POST.get('codigo_barras')
    unidad = request.POST.get('unidad')
    
    unidadId = Unidades.objects.get(idunidad=unidad)
    categoriaId = Categoria.objects.get(idcategoria=categoria)
    
    precioCompraPost2 = float(precioCompraPost.replace(',','.'))
    precioProducto2 = float(precioProducto.replace(',','.'))

    Producto.objects.create(idcategoria=categoriaId,
                            idunidad=unidadId,
                            nomproducto=nombreProducto,
                            descripcion=descripcionProducto, 
                            preciounitario=precioProducto2, 
                            stockactual=stockProducto, estado=1,
                            codigo=codigo1,
                            precioCompra=precioCompraPost2,
                            codigo_barras=codigo_barras1
                            )
    return redirect('productos')


def agregar_desde_compra(request):
    if request.method != 'POST':
        return JsonResponse({'error': 'Método no permitido'}, status=405)
    try:
        categoria_id = request.POST.get('categoria')
        unidad_id = request.POST.get('unidad')
        nombre = request.POST.get('nombreProducto', '').strip()
        descripcion = request.POST.get('descripcionProducto', '')
        precio_compra = float((request.POST.get('precioCompra') or '0').replace(',', '.'))
        precio_venta = float((request.POST.get('precioProducto') or '0').replace(',', '.'))
        stock = request.POST.get('stockProducto') or 0
        codigo = request.POST.get('codigo', '')
        codigo_barras = request.POST.get('codigo_barras', '')

        categoria = Categoria.objects.get(idcategoria=categoria_id)
        unidad = Unidades.objects.get(idunidad=unidad_id)

        producto = Producto.objects.create(
            idcategoria=categoria,
            idunidad=unidad,
            nomproducto=nombre,
            descripcion=descripcion,
            preciounitario=precio_venta,
            precioCompra=precio_compra,
            stockactual=stock,
            estado=1,
            codigo=codigo,
            codigo_barras=codigo_barras,
        )
        return JsonResponse({'nombre': producto.nomproducto, 'precio': float(producto.preciounitario)})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def editado(request):
    def _normalizar_fk_id(valor):
        if valor in (None, ''):
            return None
        valor_str = str(valor).strip()
        if valor_str.isdigit():
            return int(valor_str)
        match = re.search(r'\((\d+)\)', valor_str)
        if match:
            return int(match.group(1))
        return None

    idproducto2 = request.POST.get('idproducto2')
    if not idproducto2:
        return redirect('productos')

    campos_actualizar = {}

    categoria = _normalizar_fk_id(request.POST.get('categoria2'))
    if categoria is not None:
        campos_actualizar['idcategoria_id'] = categoria

    unidad = _normalizar_fk_id(request.POST.get('unidad2'))
    if unidad is not None:
        campos_actualizar['idunidad_id'] = unidad

    if 'nombreProducto2' in request.POST:
        campos_actualizar['nomproducto'] = request.POST.get('nombreProducto2')

    if 'descripcionProducto2' in request.POST:
        campos_actualizar['descripcion'] = request.POST.get('descripcionProducto2')

    precio_producto = request.POST.get('precioProducto2')
    if precio_producto not in (None, ''):
        campos_actualizar['preciounitario'] = float(precio_producto.replace(',', '.'))

    precio_compra = request.POST.get('precioCompra2')
    if precio_compra not in (None, ''):
        campos_actualizar['precioCompra'] = float(precio_compra.replace(',', '.'))

    stock_producto = request.POST.get('stockProducto2')
    if stock_producto not in (None, ''):
        campos_actualizar['stockactual'] = stock_producto

    if campos_actualizar:
        Producto.objects.filter(idproducto=idproducto2).update(**campos_actualizar)

    return redirect('productos')

def eliminar(request, idproducto):
    producto = Producto.objects.get(idproducto= idproducto)
    producto.estado = 0
    producto.save()
    return redirect('productos')

def verLotes(request, id):
    getLotes =  Lotes.objects.filter(idproducto=id)
    lotes_list = list(getLotes.values())
    return JsonResponse(lotes_list,safe=False)

def editarLote(request):
    if request.method == 'POST':
        jaja = request.POST.getlist('lo[jaja][]')
        producciones = request.POST.getlist('lote[fecha_produccion][]')
        vencimientos = request.POST.getlist('lote[fecha_vencimiento][]')
        identificadores = request.POST.getlist('lote[identificador][]')
        cantidades = request.POST.getlist('lote[cantidad][]')
        print(jaja)
        print(producciones)
        if(producciones):
            print(producciones)
        else:
            print("None")
            
        for produccion,vencimiento, identificador, cantidad in zip(producciones,vencimientos,identificadores,cantidades):
            if produccion:
                print(produccion)
            else:
                print("None")
            print(identificador)
            print(cantidad)
            print(vencimiento)
        # Procesa los datos según sea necesario
        # ...

    return HttpResponse("<h1>Hola</h1>")
