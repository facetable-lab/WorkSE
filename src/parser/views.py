from django.shortcuts import render

from .models import Vacancy


def home_view(_request):
    _context = {
        'object_list': Vacancy.objects.all(),
    }

    return render(request=_request, template_name='home.html', context=_context)
