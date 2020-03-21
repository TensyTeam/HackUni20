from flask import request, jsonify
from app import app
import pymongo
from pymongo import MongoClient
import json
import time


cluster = MongoClient("mongodb://admin:mikedroplet@67.205.189.192:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false", connect = False )
db = cluster['hackuniversity2020']
users = db['users']
books = db['books']

@app.route('/top', methods=['POST'])
def save_token():
	x = request.json

	if users.find_one({'token': x['token']}):
		results = books.find({}).limit(3)
	else:
		user_data = {
			'id': users.count() + 1,
			'token': x['token'],
			'search': [],
		}
		users.insert_one(user_data)

		results = books.find({}).limit(3)

	ans = []
	for result in results:
		ans.append(result)

	return json.dumps(ans)


@app.route('/search', methods=['POST'])
def search():
	x = request.json

	results = books.find({})
	ans = []
	for result in results:
		ans.append(result)
	return json.dumps(ans)
