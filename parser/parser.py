import time
import json

import requests
from bs4 import BeautifulSoup


KINDS = ('luchshie_knigi_fentezi', 'knigi_fantastika_luchshee', 'knigi_detektivy', 'luchshie_knigi_uzhasov', 'knigi_o_puteshestvijah', 'knigi_pro_popadancev', 'luchshie_detskie_knigi', 'luchshie_knigi_po_psixologii', 'luchshie_knigi_osnovannye_na_realnyh_sobytijah', 'knigi_c_otricatelnymi_glavnymi_gerojami')
LINK = 'https://knigopoisk.org'
url = LINK + '/ratings/{}'
url2 = LINK + '/bookslist/{}'

with open('data.json', 'w') as file:
	for kind_id, kind in enumerate(KINDS):
		print('-' * 100)

        # Перебираем страницы
		html = requests.get(url.format(kind)).text
		print(url.format(kind))

		# Парсинг
		soup = BeautifulSoup(html, 'html.parser')

		# kind = soup.find('h1').text.split('«')[1].split('»')[0]
		# print(kind)

		table = soup.find('div', {'id': 'new-quotes'})

		try:
			books = table.find_all('div', {'class': 'main-list-item'})
		except:
			html = requests.get(url2.format(kind)).text
			print(url2.format(kind))

			soup = BeautifulSoup(html, 'html.parser')
			table = soup.find('div', {'class': 'block-table__cell pdl-30'})
			books = table.find_all('div', {'class': 'main-list-item'})

		for book in books:
			try:
				title = book.find('div', {'class': 'main-list-item-right-1__left'}).text.strip()
				name = title.split('\n')[0]
				author = title.split('\n')[1]
				src = book.find('div', {'class': 'main-list-item-right-1__left'}).find('a').get('href')
				img = book.find('div', {'class': 'main-list-item__left'}).find('img').get('src')
				rating = float(book.find('span', {'class': 'rating'}).text)
				description = book.find('div', {'class': 'main-list-item-right-description'}).text
			except:
				continue

			req = {
				'name': name,
				'author': author,
				'link': src,
				'img': LINK + img,
				'rating': rating,
				'description': description,
				'kind': kind_id + 1,
			}
			data = json.dumps(req, ensure_ascii=False, indent='\t')

			print(data, file=file)

		time.sleep(1)
