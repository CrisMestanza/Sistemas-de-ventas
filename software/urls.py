from django.urls import path

from .views import login 
from .views import categorias
from .views import configuracion
from .views import compras
from .views import productos
from .views import unidades
from .views import usuarios
from .views import ventas
from .views import permisos
from .views import cpanel
from .views import tipoUsuarios
from .views import numeroserie
from .views import cerrarcaja
from .views import registroCaja
from .views import transaccion

urlpatterns = [
    #login
    path('', login.index, name="index"),
    path('login', login.login, name="login"),
    path('logout', login.logout, name="logout"),
    path('caja', login.caja, name="caja"),
    
    #Usuarios
    path('usuarios', usuarios.usuarios, name="usuarios"),
    path('usuarios/agregar', usuarios.agregar, name="usuarioAgregar"),
    path('usuarios/editar', usuarios.editar, name="usuarioEditar"),
    path('usuarios/eliminar/<int:id>', usuarios.eliminar, name="usuarioEliminar"),
    
    # compras
    path('compras', compras.compra, name="compras"),
    path('compras/eliminar/<int:id>', compras.eliminar, name="eliminarCompras"),
    path('compras/agregar', compras.agregar, name="agregarCompras"),
    path('compras/buscar', compras.buscar, name="buscarCompras"),
    path('compras/guardar', compras.guardar, name="guardarCompras"),
    path('compras/editar/<int:id>', compras.editar, name="editarCompras"),
    path('compras/editado', compras.editado, name="compraEditada"),
    path('compras/buscarFecha', compras.buscarFecha, name="buscarFecha"),
    path('compras/export/', compras.export_compras_to_excel, name='export_compras_to_excel'),
    
    #Unidades
    path('unidades', unidades.unidades, name="unidades"),
    path('unidades/activo/<int:id>', unidades.activo, name="unidadesActivo"),
    path('unidades/desactivo/<int:id>', unidades.desactivo, name="unidadesDesactivo"),
    
    # ventas
    path('ventas', ventas.ventas, name="ventas"),
    path('ventas/venta', ventas.agregar, name="agregarVenta"),
    path('ventas/serie', ventas.buscarSerie, name="buscarSerie"),
    path('ventas/buscarprodcuto', ventas.buscarProducto, name="buscarProducto"),
    path('ventas/buscarRuc', ventas.ruc, name="buscarRuc"),
    path('ventas/buscarDni', ventas.dni, name="buscarDni"),
    path('ventas/guardarVenta', ventas.guardarVenta, name="guardarVenta"),
    path('ventas/eliminarVentas/<int:id>', ventas.eliminarVentas, name="eliminarVentas"),
    path('ventas/editar/<int:id>', ventas.editarVenta, name="editarVenta"),
    path('ventas/guardarEditar', ventas.guardarEditar, name="guardarEditar"),
    path('ventas/buscarFechaVentas', ventas.buscarFechaVentas, name="buscarFechaVentas"),
    path('ventas/enviarSunat/<int:id>', ventas.enviarSunat, name='enviarSunat'),
    path('compras/export', ventas.export_to_excel_ventas, name='export_to_excel_ventas'),

    #categorias
    path('categorias', categorias.categorias, name="categorias"),
    path('categorias/agregar', categorias.agregar, name="agregarCategorias"),
    path('categorias/editar', categorias.editar, name="editarCategorias"),
    path('categorias/eliminarCategoria/<int:id>', categorias.eliminar, name="categoriasEliminar"),
    
    #Permisos
    path('permisos', permisos.permisos, name="permisos"),
    path('permisos/agregaPermiso', permisos.agregaPermiso, name="agregaPermiso"),
    path('permisos/eliminarPermiso/<int:id>', permisos.eliminarPermiso, name="eliminarPermiso"),
     
    #productos
    path('productos', productos.productos, name="productos"),
    path('productos/agregar', productos.agregar, name="productosAgregar"),
    path('productos/editar', productos.editado, name="productosEditado"),
    path('productos/eliminarProducto/<int:idproducto>', productos.eliminar, name="eliminarProducto"),
    
    #Lotes
    path('productos/verLotes/<int:id>', productos.verLotes, name="verLotes"),
    path('productos/editarLote', productos.editarLote, name="editarLote"),
    
    #configuracion
    path('configuracion', configuracion.configuracion, name="configuracion"),
    path('configuracion/buscarProvincias', configuracion.buscarProvincias, name="buscarProvincias"),
    path('configuracion/buscarDistritos', configuracion.buscarDistritos, name="buscarDistritos"),
    path('configuracion/ubigueo', configuracion.ubigueo, name="ubigueo"),
    path('configuracion/editarEmpresa', configuracion.editarEmpresa, name="editarEmpresa"),
    path('configuracion/produccion/<int:id>', configuracion.produccion, name="produccion"),
    path('configuracion/desarrollo/<int:id>', configuracion.desarrollo, name="desarrollo"),

    #cpanel
    path('cpanel', cpanel.cpanel, name="cpanel"),

    
    #Tipo usuarios
    path('tipousuarios', tipoUsuarios.tipoUsuarios, name="tipoUsuarios"),
    path('tipousuarios/agregar', tipoUsuarios.tipousuariosAgregar, name="tipousuariosAgregar"),
    path('tipousuarios/editar', tipoUsuarios.tipousuariosEditar, name="tipousuariosEditar"),
    path('tipousuarios/eliminar/<int:id>', tipoUsuarios.tipousuariosEliminar, name="tipousuariosEliminar"),

    #Número de serie
    path('numeroserie', numeroserie.numeroserie, name="numeroserie"),
    path('numeroserie/agregar', numeroserie.numeroserieAgregar, name="numeroserieAgregar"),
    path('numeroserie/editar', numeroserie.numeroserieEditar, name="numeroserieEditar"),
    path('numeroserie/eliminar/<int:id>', numeroserie.numeroserieEliminar, name="numeroserieEliminar"),
    
    #Cerrar caja
    path('cerrarcaja', cerrarcaja.cerrarcaja, name="cerrarcaja"),
    path('cerrarcaja/finalizarCaja', cerrarcaja.finalizarCaja, name="finalizarCaja"),
    
    #REGISTROS DE CAJA
    path('cajas', registroCaja.mostrar_caja, name="MostrarCajas"),
    
    #TRANSACCIONES
    path('transacciones', transaccion.mostrar_Transaccion, name="MostrarTransaccion"),
    path('transacciones/agregar', transaccion.agregar_Transaccion, name="transaccionAgregar"),
    path('transacciones/editar', transaccion.editar_Transaccion, name="transaccionEditar"),


    path('generar_ticket/', ventas.pdf_ticket, name='generar_ticket'),

]
