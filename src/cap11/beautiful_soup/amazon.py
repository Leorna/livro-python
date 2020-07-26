import bs4
import requests
import time
import webbrowser


product = input('Pesquise por um produto na Amazon: ')
url = 'https://amazon.com.br'
res = requests.get(f'{url}/s?k={product}')

try:
    res.raise_for_status()
except Exception as error:
    print(f'Algo deu errado\n{error}')
else:
    print('\n----------\n')
    print(f'Pesquisando por {product}...')

    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    link_elements = soup.select('a.a-link-normal.a-text-normal')

    print('Abrindo o navegador padrão do seu sistema...')
    time.sleep(3)

    webbrowser.open(f'{url}/s?k={product}')
    for i in range(5):
        webbrowser.open(f'{url}/{link_elements[i].get("href")}')