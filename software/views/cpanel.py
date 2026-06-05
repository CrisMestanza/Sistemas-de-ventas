from datetime import datetime, date
from decimal import Decimal
from django.db import connection
from software.views.apiBusquedaRUcDni import ApisNetPe
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
import templates
from software.models.comprasModel import Compras
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
from software.models.distritosModel import Distritos
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos
from software.models.detallecategoriaxunidadesModel import Detallecategoriaxunidades
from software.models.departamentosModel import Departamentos
from software.models.codigocorreoModel import CodigoCorreo
from software.models.TipoIgvModel import TipoIgv
from software.models.clientesModel import Clientes
from software.models.cajaModel import Caja

from django.db.models import Sum
from django.db.models.functions import TruncMonth



def cpanel(request):
    id2 = request.session.get('idtipousuario')
    nombrecompleto = request.session.get('nombrecompleto')
    if id2:
        permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)

        es_superadmin = request.session.get('es_superadmin', False)
        idsucursal = request.session.get('idsucursal')

        # Ejecutar la consulta SQL para obtener los datos de ventas por mes
        with connection.cursor() as cursor:
            if es_superadmin:
                cursor.execute("""
                    SELECT
                        DATE_FORMAT(`venta`.`fechaemision`, '%Y %M') AS `mes_anio`,
                        COALESCE(SUM(`venta_detalle`.`preciosubtotal`), 0) AS `total`
                    FROM `venta`
                    INNER JOIN `venta_detalle` ON (`venta`.`idventa` = `venta_detalle`.`idventa`)
                    WHERE `venta`.`estado` = 1
                    GROUP BY `mes_anio`
                    ORDER BY `mes_anio`;
                """)
            else:
                cursor.execute("""
                    SELECT
                        DATE_FORMAT(`venta`.`fechaemision`, '%%Y %%M') AS `mes_anio`,
                        COALESCE(SUM(`venta_detalle`.`preciosubtotal`), 0) AS `total`
                    FROM `venta`
                    INNER JOIN `venta_detalle` ON (`venta`.`idventa` = `venta_detalle`.`idventa`)
                    INNER JOIN `numserie` ON (`venta`.`idnumserie` = `numserie`.`idnumserie`)
                    WHERE `venta`.`estado` = 1 AND `numserie`.`idsucursal` = %s
                    GROUP BY `mes_anio`
                    ORDER BY `mes_anio`;
                """, [idsucursal])
            rows = cursor.fetchall()

        # Calcular el total general de ventas
        total_general = sum(Decimal(str(row[1] or 0)) for row in rows)

        # Preparar datos para el gráfico de Highcharts
        chart_data = []
        for row in rows:
            total_venta = Decimal(str(row[1] or 0))
            porcentaje = (total_venta / total_general) * 100 if total_general > 0 else Decimal('0.00')
            chart_data.append({
                'name': row[0],  # mes_anio
                'y': float(total_venta),  # total de ventas
                'porcentaje': float(round(porcentaje, 2))  # porcentaje redondeado a 2 decimales
            })
            
        ultimo_registro = Caja.objects.order_by('-id_caja').first()
        
        if ultimo_registro and ultimo_registro.estado == 1:
            cerrar = "Caja está abierto"
        else:
            cerrar = None
            
        data = {
            "permisos": permisos,
            'resultados': rows,
            'chart_data': chart_data,  # Datos para el gráfico
            'nombrecompleto':nombrecompleto,
            "cerrar": cerrar
        }

        return render(request, 'cpanel.html', data)
    else:
        return HttpResponse("<h1>No tiene acceso señor</h1>")
