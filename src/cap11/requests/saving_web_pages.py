import requests


url = 'https://automatetheboringstuff.com/files/rj.txt'

res = requests.get(url)

try:
    res.raise_for_status()
except Exception as error:
    print(f'Something went wrong: {error}')
else:
    with open('RomeoAndJuliet.txt', 'wb') as file:
        bytes_size = 10**5
        for chunk in res.iter_content(bytes_size):
            file.write(chunk)