import json
from pymongo import MongoClient

cluster = MongoClient("mongodb://admin:mikedroplet@67.205.189.192:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false", connect = False )
db = cluster['hackuniversity2020']
books = db['books']

def next_id(name):
	try:
		db_filter = {'id': True, '_id': False}
		id = db[name].find({}, db_filter).sort('id', -1)[0]['id'] + 1
	except:
		id = 1

	return id

with open('data.json', 'r') as file:
	book_id = next_id('books')

	for i in file:
		book = json.loads(i)
		book['id'] = book_id

		books.insert_one(book)

		book_id += 1

	print(book_id)