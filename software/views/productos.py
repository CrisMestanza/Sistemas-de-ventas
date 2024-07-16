
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


def editado(request):
    idproducto2 = request.POST.get('idproducto2')
    categoria = request.POST.get('categoria2')
    unidad = request.POST.get('unidad2')
    nombreProducto = request.POST.get('nombreProducto2')
    descripcionProducto = request.POST.get('descripcionProducto2')
    precioProducto2 = request.POST.get('precioProducto2')
    stockProducto = request.POST.get('stockProducto2')
    precioCompraPost = request.POST.get('precioCompra2')

    categoriaId = Categoria.objects.get(idcategoria=categoria)
    unidadId = Unidades.objects.get(idunidad=unidad)
    
    precioCompraPost2 = float(precioCompraPost.replace(',', '.'))
    precioProducto3 = float(precioProducto2.replace(',', '.'))
    Producto.objects.filter(idproducto=idproducto2).update(idcategoria=categoria,
                                                           idunidad=unidadId,
                                                           nomproducto=nombreProducto,
                                                           descripcion=descripcionProducto, 
                                                           preciounitario=precioProducto3,
                                                           precioCompra=precioCompraPost2,
                                                           stockactual=stockProducto, 
                                                           estado=1)
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