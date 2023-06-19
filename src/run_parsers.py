from parser.parsers import *

_parsers = (
    (head_hunter, 'https://rostov.hh.ru/search/vacancy?text=python&salary=&area=76&ored_clusters=true'),
    (habr_career, 'https://career.habr.com/vacancies?locations[]=c_726&q=python&type=all'),
)

jobs, errors = [], []

for func, url in _parsers:
    j, e = func(url)
    jobs += j
    errors += e

for i in jobs:
    print(i)

for i in errors:
    print(i)

