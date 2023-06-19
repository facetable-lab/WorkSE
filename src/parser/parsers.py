from random import choice

import requests
from bs4 import BeautifulSoup

__all__ = ('head_hunter', 'habr_career')

_headers = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'""
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Fedora; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'""
    },
    {
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0)',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'""
    },
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 YaBrowser/23.5.0.2282 Yowser/2.5 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'""
    },
    {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'""
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/114.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'""
    },
    {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'""
    },
]


def head_hunter(url):
    _jobs = []
    _errors = ['Сайт HH']
    response = requests.get(url, headers=choice(_headers))

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')

        main_div = soup.find('main', attrs={'class': 'vacancy-serp-content'})
        if main_div:
            is_empty = main_div.find('div', attrs={'class': 'bloko-gap bloko-gap_top'})

            if not is_empty.text == 'Попробуйте другие варианты поискового запроса или уберите фильтры':
                div_list = main_div.find_all('div', attrs={'class': 'vacancy-serp-item__layout'})
                for div in div_list:
                    title = div.find('a', attrs={'class': 'serp-item__title'})
                    company = div.find('a', attrs={'class': 'bloko-link bloko-link_kind-tertiary'})

                    _jobs.append({
                        'title': title.text,
                        'url': title['href'],
                        'company': company.text,
                        'description': 'Нет информации о компании'
                    })
            else:
                _errors.append({
                    'url': url,
                    'error_msg': 'Страница пуста.'
                })
        else:
            _errors.append({
                'url': url,
                'error_msg': 'Div со списком вакансий не найден или был изменен.'
            })
    else:
        _errors.append({
            'url': url,
            'error_msg': 'Удаленный сайт не отвечает.'
        })

    return _jobs, _errors


def habr_career(url):
    _jobs = []
    _errors = ['Сайт Habr Career']

    domain = 'https://career.habr.com'
    response = requests.get(url, headers=choice(_headers))

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        main_div = soup.find('div', attrs={'class': 'section-group section-group--gap-medium'})

        if main_div:
            is_empty = main_div.find('div', attrs={'class': 'no-content'})

            if not is_empty:
                div_list = main_div.find_all('div', attrs={'class': 'vacancy-card__info'})

                for div in div_list:
                    title = div.find('a', attrs={'class': 'vacancy-card__title-link'})
                    company = div.find('a', attrs={'class': 'link-comp link-comp--appearance-dark'})

                    _jobs.append({
                        'title': title.text,
                        'url': domain + title['href'],
                        'company': company.text,
                        'description': 'Нет информации о компании'
                    })
            else:
                _errors.append({
                    'url': url,
                    'error_msg': 'Страница пуста.'
                })
        else:
            _errors.append({
                'url': url,
                'error_msg': 'Div со списком вакансий не найден или был изменен.'
            })

    else:
        _errors.append({
            'url': url,
            'error_msg': 'Удаленный сайт не отвечает.'
        })

    return _jobs, _errors


if __name__ == '__main__':
    test_url_hh = 'https://rostov.hh.ru/search/vacancy?text=python&area=76'
    test_url_habr = 'https://career.habr.com/vacancies?locations[]=c_726&q=python&type=all'

    jobs_hh, errors_hh = head_hunter(test_url_hh)
    jobs_habr, errors_habr = habr_career(test_url_habr)

    for i in jobs_hh:
        print(i)

    for i in errors_hh:
        print(i)

    for i in jobs_habr:
        print(i)

    for i in errors_habr:
        print(i)
