import os
import requests
import bs4
import time


url = 'https://xkcd.com/'
os.makedirs('xkdc', exist_ok=True)

while not url.endswith('#'):
    print(f'Downloading page {url}')
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, features='html.parser')
    img_elements = soup.select('div#comic img')

    if img_elements == []:
        print('Couldn\'t find comic image')
    else:
        comic_url = f'http:{img_elements[0].get("src")}'
        print(f'Downloading image {comic_url}')
        res = requests.get(comic_url)
        
        with open(os.path.join('xkdc', os.path.basename(comic_url)), 'wb') as image_file:
            for chunk in res.iter_content(10**5):
                image_file.write(chunk)

    prev_link = soup.select('ul.comicNav a[rel=prev]')[0]
    url = f'https://xkcd.com{prev_link.get("href")}'
    time.sleep(1.5)


print('Done!')