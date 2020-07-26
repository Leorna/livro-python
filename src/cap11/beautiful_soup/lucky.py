'''
Abre resultados mais importantes da pesquisa no navegador padrão
O conteúdo a ser pesquisado deve ser passado em linha de comando
Exemplo: python search.py paçoca
'''

import requests
import bs4
import webbrowser
import sys
import time


search = ' '.join(sys.argv[1:])

print(f'Googling {search}...')

url = 'http://google.com/search?q=' + search

res = requests.get(url)

try:
    res.raise_for_status()
except Exception as error:
    print(error)
else:
    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    link_elements = soup.select('div > a')
    links_to_be_open = link_elements[23:28]
    
    print('Opening default browser...')
    time.sleep(3)
    for link in links_to_be_open:
        webbrowser.open('http://google.com'+link.get('href'))