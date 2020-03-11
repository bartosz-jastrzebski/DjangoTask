from django.http import HttpResponse
from .templatetags.accounts_tags import is_allowed, bizzfuzz
from .models import User
import csv


def csv_report(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="report.csv"'

    writer = csv.writer(response)
    writer.writerow(['Username', 'Birthday', 'Eligible', 'Random Number', 'BizzFuzz'])
    for user in User.objects.all():
        writer.writerow([
            user.username, 
            user.birthday,
            is_allowed(user),
            user.number,
            bizzfuzz(user.number)
        ])
    return response