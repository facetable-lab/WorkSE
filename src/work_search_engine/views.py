from django.shortcuts import render
import datetime


def home(_request):
    _context = {
        'date': datetime.datetime.now().date(),
        'name': 'Дмитрий Игнатенко'
    }

    return render(request=_request, template_name='home.html', context=_context)
