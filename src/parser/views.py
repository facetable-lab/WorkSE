from django.shortcuts import render

from .models import Vacancy
from .forms import FindForm


def home_view(_request):
    city = _request.GET.get('city')
    language = _request.GET.get('language')

    _filter = {}
    if city or language:
        if city:
            _filter['city__slug'] = city
        if language:
            _filter['language__slug'] = language

    _context = {
        'form': FindForm,
        'vacancy_qs': Vacancy.objects.filter(**_filter),
    }

    return render(request=_request, template_name='parser/home.html', context=_context)
