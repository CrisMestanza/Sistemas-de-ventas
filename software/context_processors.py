from software.models.empresaModel import Empresa


def empresa_global(request):
    try:
        empresa = Empresa.objects.first()
    except Exception:
        empresa = None
    return {'empresa_global': empresa}
