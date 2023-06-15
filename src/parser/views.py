from django.shortcuts import render

from .models import Vacancy


def home_view(_request):
    _context = {
        'vacancy_qs': Vacancy.objects.all(),
    }

    return render(request=_request, template_name='parser/home.html', context=_context)
