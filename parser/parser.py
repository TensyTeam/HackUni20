import time
import json

import requests
from bs4 import BeautifulSoup


LINK = 'https://www.ozon.ru'
url = LINK + '/highlight/22872/?page={}'

with open('data.json', 'w') as file:
	for page in range(1, 2):
        # Перебираем страницы
		html = requests.get(url.format(page)).text

		# Парсинг
		soup = BeautifulSoup(html, 'html.parser')

		table = soup.find('div', {'class': 'widget-search-result-container'})
		books = soup.find_all('div', {'class': 'a3k5'})

		for book in books:
			try:
				name = book.find('div', {'class': 'a5w'}).find_all('a')[1].text
				price = book.find('div', {'class': 'a5w'}).find_all('a')[0].span.text
				author = book.find('div', {'class': 'a5w'}).find_all('span')[1].text
				img = book.find('div', {'class': 'a3y'}).find('img').get('src')
			except:
				continue

			req = {
				'name': name,
				'price': price,
				'author': author,
				'img': LINK + img,
			}
			data = json.dumps(req, ensure_ascii=False, indent='\t')

			print(data)

		time.sleep(1)
