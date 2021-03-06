from io import StringIO

import xlsxwriter
from django.http import HttpResponse

"""
    Generates excell for a defined set of fields and a model
"""


def generate_excell(fields, model_instance):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Report.xlsx'
    output = StringIO()
    workbook = xlsxwriter.Workbook(output)
    worksheet_s = workbook.add_worksheet("Locos")

    col = 0
    for field in fields:
        parts = field.split('.')
        count = 1
        dbfield = model_instance._meta.get_field(parts[0])
        while count < len(parts):
            dbfield = dbfield.related_model._meta.get_field(parts[count])
            count += 1
        worksheet_s.write_string(0, col, str(str(dbfield.verbose_name), "utf-8"))
        col += 1

    instances = model_instance.objects.all()

    row = 1
    for instance in instances:
        col = 0
        for field in fields:
            parts = field.split('.')
            count = 1
            fieldvalue = getattr(instance, parts[0])
            while count < len(parts) and fieldvalue is not None:
                fieldvalue = getattr(fieldvalue, parts[count])
                count += 1
            if fieldvalue is not None:
                if isinstance(fieldvalue, str):
                    worksheet_s.write_string(row, col, fieldvalue)
                else:
                    worksheet_s.write_string(row, col, str(str(fieldvalue), "utf-8"))
            col += 1
        row += 1

    workbook.close()
    xlsx_data = output.getvalue()
    response.write(xlsx_data)
    return response
