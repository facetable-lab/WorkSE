import os, sys

from django.db import DatabaseError

project = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(project)
os.environ['DJANGO_SETTINGS_MODULE'] = 'work_search_engine.settings'

import django

django.setup()

from parser.models import Vacancy, City, Language
from parser.parsers import *

_parsers = (
    (head_hunter, 'https://rostov.hh.ru/search/vacancy?text=python&salary=&area=76&ored_clusters=true'),
    (habr_career, 'https://career.habr.com/vacancies?locations[]=c_726&q=python&type=all'),
)

_city = City.objects.get(slug='rostov-na-donu')
_language = Language.objects.get(slug='python')

jobs, errors = [], []

for func, url in _parsers:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    vacancy = Vacancy(**job, city=_city, language=_language)
    print(vacancy.company)

    try:
        vacancy.save()
    except DatabaseError:
        pass

# for i in jobs:
#     print(i)
#
# for i in errors:
#     print(i)
