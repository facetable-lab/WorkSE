import requests
import codecs

_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}

url = 'https://rostov.hh.ru/search/vacancy?text=python&area=76'

response = requests.get(url, headers=_headers)


file_handler = codecs.open('head_hunter.html', 'w', 'utf-8')
file_handler.write(str(response.text))
file_handler.close()
