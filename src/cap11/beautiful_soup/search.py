import bs4
import time
import requests
import webbrowser


url = 'http://google.com'

search = input('Digite o que deseja pesquisar: ')

res = requests.get(f'{url}/search?q={search}')

try:
    res.raise_for_status()
except Exception as error:
    print('Erro na sua pesquisa!')
    print(error)
else:
    print(f'Pesquisando por {search}...')

    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    link_elements = soup.select('div > a')
    links = link_elements[23:28]

    print('Abrindo o navegador padrão do seu sistema...')
    time.sleep(2)
    for link in links:
        webbrowser.open(url+link.get('href'))