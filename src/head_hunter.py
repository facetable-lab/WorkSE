import requests
import codecs
from bs4 import BeautifulSoup

_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

domain = 'https://rostov.hh.ru/'

url = 'https://rostov.hh.ru/search/vacancy?text=python&area=76'

response = requests.get(url, headers=_headers)


jobs = []

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')

    main_div = soup.find('main', attrs={'class': 'vacancy-serp-content'})
    div_list = soup.find_all('div', attrs={'class': 'vacancy-serp-item__layout'})
    for div in div_list:
        title = div.find('a', attrs={'class': 'serp-item__title'})
        href = title['href']
        company = div.find('a', attrs={'class': 'bloko-link bloko-link_kind-tertiary'})
        print(company.text)
        content = 'Нет информации о компании'

# file_handler = codecs.open('head_hunter.html', 'w', 'utf-8')
# file_handler.write(str(response.text))
# file_handler.close()
