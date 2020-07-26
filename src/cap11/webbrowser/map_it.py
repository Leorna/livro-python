# Obter um endereço a partir dos argumentos da linha de comando ou do clipboard (área de transferência)
# Abrir o navegador web com a página do Google Maps para o endereço

import webbrowser
import pyperclip
import sys


url = 'https://google.com/maps/place/'

if len(sys.argv) > 1:
    address = ' '.join(sys.argv[1:])
else:
    address = pyperclip.paste()

webbrowser.open(f'{url}{address}')
