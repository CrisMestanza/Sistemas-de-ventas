from software.models.empresaModel import Empresa
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos


def empresa_global(request):
    try:
        empresa = Empresa.objects.first()
    except Exception:
        empresa = None
    return {'empresa_global': empresa}


def modulos_permitidos(request):
    idtipousuario = request.session.get('idtipousuario')
    es_superadmin = request.session.get('es_superadmin', False)
    if es_superadmin:
        # Super admin tiene acceso a todo — set con todos los IDs posibles
        return {'modulos_ids': set(range(1, 999))}
    if idtipousuario:
        ids = set(
            Detalletipousuarioxmodulos.objects.filter(idtipousuario=idtipousuario)
            .values_list('idmodulo_id', flat=True)
        )
        return {'modulos_ids': ids}
    return {'modulos_ids': set()}
