from flask import request, jsonify
from app import app
import pymongo
from pymongo import MongoClient
import json
import time


cluster = MongoClient("mongodb://admin:mikedroplet@67.205.189.192:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false", connect = False )
db = cluster['hackuniversity2020']
users = db['users']

@app.route('/search', methods=['POST'])
def post():
	results = users.find({})
	ans = []
	for result in results:
		ans.append(result)
	return json.dumps(ans)
