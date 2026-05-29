from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Sum, Value, DecimalField
from django.db.models.functions import Coalesce
from decimal import Decimal, ROUND_HALF_UP

from software.models.VentaModel import Venta
from software.models.comprasModel import Compras
from software.models.detalletipousuarioxmodulosModel import Detalletipousuarioxmodulos

from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment
from openpyxl.utils import get_column_letter

from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm


def _get_registros_val(fecha_inicio, fecha_fin, operacion):
    ventas = []
    compras = []

    if operacion in ('todos', 'ventas'):
        qs = Venta.objects.filter(estado=1).select_related(
            'idnumserie__idtipodocumento'
        ).annotate(
            total_cant=Coalesce(Sum('ventadetalle__cantidad'), Value(0), output_field=DecimalField()),
            total_monto=Coalesce(Sum('ventadetalle__preciosubtotal'), Value(0), output_field=DecimalField()),
        )
        if fecha_inicio:
            qs = qs.filter(fechaemision__gte=fecha_inicio)
        if fecha_fin:
            qs = qs.filter(fechaemision__lte=fecha_fin)
        for v in qs:
            cant = v.total_cant or Decimal('0')
            total = v.total_monto or Decimal('0')
            unit = (total / cant).quantize(Decimal('0.01'), ROUND_HALF_UP) if cant else Decimal('0')
            ventas.append({
                'fecha': v.fechaemision,
                'tipo_doc': v.idnumserie.idtipodocumento.nombredocumento,
                'serie_numero': f"{v.idnumserie.numserie}-{v.numcorrelativo}",
                'operacion': 'Venta',
                'ent_cant': None, 'ent_unit': None, 'ent_total': None,
                'sal_cant': cant, 'sal_unit': unit, 'sal_total': total,
            })

    if operacion in ('todos', 'compras'):
        qs = Compras.objects.filter(estado=1).annotate(
            total_cant=Sum('compradetalle__cantidad'),
            total_monto=Sum('compradetalle__subtotal'),
        )
        if fecha_inicio:
            qs = qs.filter(fechacompra__gte=fecha_inicio)
        if fecha_fin:
            qs = qs.filter(fechacompra__lte=fecha_fin)
        for c in qs:
            cant = Decimal(str(c.total_cant or 0))
            total = Decimal(str(c.total_monto or 0))
            unit = (total / cant).quantize(Decimal('0.01'), ROUND_HALF_UP) if cant else Decimal('0')
            compras.append({
                'fecha': c.fechacompra,
                'tipo_doc': 'Comprobante',
                'serie_numero': c.numcorrelativo,
                'operacion': 'Compra',
                'ent_cant': cant, 'ent_unit': unit, 'ent_total': total,
                'sal_cant': None, 'sal_unit': None, 'sal_total': None,
            })

    # Compras (0) antes que Ventas (1) en el mismo día
    return sorted(ventas + compras, key=lambda x: (x['fecha'], 0 if x['operacion'] == 'Compra' else 1))


def _fmt(cant, unit, total):
    if cant is None:
        return '-'
    return f"{int(cant)} / S/{unit} / S/{total:,.2f}"


def registro_valorizado(request):
    id2 = request.session.get('idtipousuario')
    if not id2:
        return render(request, 'errors/error.html')

    permisos = Detalletipousuarioxmodulos.objects.filter(idtipousuario=id2)
    fecha_inicio = request.GET.get('fecha_inicio') or None
    fecha_fin    = request.GET.get('fecha_fin') or None
    operacion    = request.GET.get('operacion', 'todos')

    registros = _get_registros_val(fecha_inicio, fecha_fin, operacion)

    total_ent = sum(r['ent_total'] or Decimal('0') for r in registros)
    total_sal = sum(r['sal_total'] or Decimal('0') for r in registros)

    return render(request, 'registroValorizado/registroValorizado.html', {
        'permisos': permisos,
        'registros': registros,
        'fecha_inicio': fecha_inicio or '',
        'fecha_fin':    fecha_fin or '',
        'operacion':    operacion,
        'total_ent':    total_ent,
        'total_sal':    total_sal,
        'nombrecompleto': request.session.get('nombrecompleto'),
    })


def export_valorizado_excel(request):
    fecha_inicio = request.GET.get('fecha_inicio') or None
    fecha_fin    = request.GET.get('fecha_fin') or None
    operacion    = request.GET.get('operacion', 'todos')
    registros    = _get_registros_val(fecha_inicio, fecha_fin, operacion)

    wb = Workbook()
    ws = wb.active
    ws.title = "Registro Valorizado"

    h_fill = PatternFill(start_color="1F4E79", end_color="1F4E79", fill_type="solid")
    h_font = Font(color="FFFFFF", bold=True)
    center = Alignment(horizontal="center", vertical="center", wrap_text=True)

    headers = ["#", "Fecha", "Tipo Doc.", "Serie/Número", "Operación",
               "Ent. Cant", "Ent. Unit (S/)", "Ent. Total (S/)",
               "Sal. Cant", "Sal. Unit (S/)", "Sal. Total (S/)"]
    ws.append(headers)
    for cell in ws[1]:
        cell.fill = h_fill
        cell.font = h_font
        cell.alignment = center

    widths = [4, 13, 20, 16, 11, 10, 14, 14, 10, 14, 14]
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w

    green = PatternFill(start_color="E2EFDA", end_color="E2EFDA", fill_type="solid")
    red   = PatternFill(start_color="FCE4D6", end_color="FCE4D6", fill_type="solid")

    for idx, r in enumerate(registros, 1):
        row = [
            idx,
            r['fecha'].strftime('%d/%m/%Y'),
            r['tipo_doc'],
            r['serie_numero'],
            r['operacion'],
            int(r['ent_cant']) if r['ent_cant'] is not None else '-',
            float(r['ent_unit']) if r['ent_unit'] is not None else '-',
            float(r['ent_total']) if r['ent_total'] is not None else '-',
            int(r['sal_cant']) if r['sal_cant'] is not None else '-',
            float(r['sal_unit']) if r['sal_unit'] is not None else '-',
            float(r['sal_total']) if r['sal_total'] is not None else '-',
        ]
        ws.append(row)
        fill = green if r['operacion'] == 'Compra' else red
        for col in range(6, 12):
            ws.cell(ws.max_row, col).fill = fill

    response = HttpResponse(
        content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )
    response['Content-Disposition'] = 'attachment; filename=registro_valorizado.xlsx'
    wb.save(response)
    return response


def export_valorizado_pdf(request):
    fecha_inicio = request.GET.get('fecha_inicio') or None
    fecha_fin    = request.GET.get('fecha_fin') or None
    operacion    = request.GET.get('operacion', 'todos')
    registros    = _get_registros_val(fecha_inicio, fecha_fin, operacion)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=registro_valorizado.pdf'

    doc = SimpleDocTemplate(response, pagesize=landscape(A4),
                            leftMargin=1*cm, rightMargin=1*cm,
                            topMargin=1.5*cm, bottomMargin=1.5*cm)
    styles = getSampleStyleSheet()
    elements = []
    elements.append(Paragraph("<b>Registro Valorizado</b>", styles['Title']))
    if fecha_inicio or fecha_fin:
        elements.append(Paragraph(
            f"Período: {fecha_inicio or '—'} al {fecha_fin or '—'}", styles['Normal']))
    elements.append(Spacer(1, 0.4*cm))

    data = [["#", "Fecha", "Tipo Doc.", "Serie/Nro", "Operación",
             "Ent.\nCant", "Ent.\nUnit S/", "Ent.\nTotal S/",
             "Sal.\nCant", "Sal.\nUnit S/", "Sal.\nTotal S/"]]

    for idx, r in enumerate(registros, 1):
        data.append([
            str(idx),
            r['fecha'].strftime('%d/%m/%Y'),
            r['tipo_doc'],
            r['serie_numero'],
            r['operacion'],
            str(int(r['ent_cant'])) if r['ent_cant'] is not None else '-',
            f"{r['ent_unit']:,.2f}" if r['ent_unit'] is not None else '-',
            f"{r['ent_total']:,.2f}" if r['ent_total'] is not None else '-',
            str(int(r['sal_cant'])) if r['sal_cant'] is not None else '-',
            f"{r['sal_unit']:,.2f}" if r['sal_unit'] is not None else '-',
            f"{r['sal_total']:,.2f}" if r['sal_total'] is not None else '-',
        ])

    total_ent = sum(r['ent_total'] or Decimal('0') for r in registros)
    total_sal = sum(r['sal_total'] or Decimal('0') for r in registros)
    data.append(["", "", "", "", "TOTAL", "", "", f"{total_ent:,.2f}",
                 "", "", f"{total_sal:,.2f}"])

    cw = [0.8*cm, 2.2*cm, 3.8*cm, 3*cm, 2*cm,
          1.5*cm, 2.2*cm, 2.5*cm, 1.5*cm, 2.2*cm, 2.5*cm]
    table = Table(data, colWidths=cw, repeatRows=1)
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#1F4E79')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, -1), 7.5),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('ROWBACKGROUNDS', (0, 1), (-1, -2), [colors.white, colors.HexColor('#F2F2F2')]),
        ('FONTNAME', (0, -1), (-1, -1), 'Helvetica-Bold'),
        ('BACKGROUND', (0, -1), (-1, -1), colors.HexColor('#D9E1F2')),
        ('GRID', (0, 0), (-1, -1), 0.4, colors.HexColor('#CCCCCC')),
        ('ROWHEIGHT', (0, 0), (-1, -1), 16),
    ]))
    elements.append(table)
    doc.build(elements)
    return response
