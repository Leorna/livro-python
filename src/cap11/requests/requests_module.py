import requests
import os

url = 'https://automatetheboringstuff.com/filess/rj.txt'
res = requests.get(url)

try:
    res.raise_for_status()
except Exception as error:
    print(f'Status code: {res.status_code}')
    print(f'There was a problem: {error}')
else:
    print(f'Status code: {res.status_code}')
    print(type(res))
    print(len(res.text))
    print(res.text[:250])
