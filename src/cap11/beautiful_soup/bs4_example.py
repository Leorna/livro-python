import bs4
import requests


url = 'http://nostarch.com'

res = requests.get(url)

try:
    res.raise_for_status()
except Exception as error:
    print(f'Something went wrong: {error}')
else:
    nostarch_soup = bs4.BeautifulSoup(res.text, features='html.parser')
    print(type(nostarch_soup)) 


with open('example.html') as example_file:
    example_soup = bs4.BeautifulSoup(example_file, features='html.parser')
    print(type(example_soup))