from flask import request, jsonify
from app import app
import pymongo
from pymongo import MongoClient
import json
import time
from gensim import corpora, models, similarities
import jieba


cluster = MongoClient("mongodb://admin:mikedroplet@67.205.189.192:27017/?authSource=admin&readPreference=primary&appname=MongoDB%20Compass&ssl=false", connect = False )
db = cluster['hackuniversity2020']
users = db['users']
books = db['books']

smile = {😂 ♥️ 🤔 🔥 🕵️ 😳 😭 👽 😱 🤘 👩‍ 🎓 }

@app.route('/top', methods=['POST'])
def save_token():
	x = request.json

	if users.find_one({'token': x['token']}):
		kind_user = users.find_one({'token': x['token']},{'_id': False})['search']
		results = books.find({'kind': kind_user},{'_id': False}).limit(10)
	else:
		user_data = {
			'id': users.count() + 1,
			'token': x['token'],
			'search': 1,
		}
		users.insert_one(user_data)

		results = books.find({'kind': 1},{'_id': False}).limit(10)

	ans = []
	for result in results:
		ans.append(result)

	return json.dumps(ans)


@app.route('/search', methods=['POST'])
def search():
	x = request.json
	results = list(books.find({}, {'_id': False}))

	#description
	texts = []
	for result in results:
		texts.append(result['description'])
	keyword = x['cont']

	texts = [jieba.lcut(text) for text in texts]
	dictionary = corpora.Dictionary(texts)
	feature_cnt = len(dictionary.token2id)
	corpus = [dictionary.doc2bow(text) for text in texts]
	tfidf = models.TfidfModel(corpus)
	kw_vector = dictionary.doc2bow(jieba.lcut(keyword))
	index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = feature_cnt)
	sim1 = index[tfidf[kw_vector]]

	#name
	texts = []
	for result in results:
		texts.append(result['name'])
	keyword = x['cont']

	texts = [jieba.lcut(text) for text in texts]
	dictionary = corpora.Dictionary(texts)
	feature_cnt = len(dictionary.token2id)
	corpus = [dictionary.doc2bow(text) for text in texts]
	tfidf = models.TfidfModel(corpus)
	kw_vector = dictionary.doc2bow(jieba.lcut(keyword))
	index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = feature_cnt)
	sim2 = index[tfidf[kw_vector]]


	#author
	texts = []
	for result in results:
		texts.append(result['author'])
	keyword = x['cont']

	texts = [jieba.lcut(text) for text in texts]
	dictionary = corpora.Dictionary(texts)
	feature_cnt = len(dictionary.token2id)
	corpus = [dictionary.doc2bow(text) for text in texts]
	tfidf = models.TfidfModel(corpus)
	kw_vector = dictionary.doc2bow(jieba.lcut(keyword))
	index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features = feature_cnt)
	sim3 = index[tfidf[kw_vector]]


	obj_with_sim = []
	for i in range(len(sim1)):
                if(sim2[i] > 0.95):
                    obj_with_sim.append([result[i], sim2[i]])
                elif(sim3[i] > 0.95):
                    obj_with_sim.append([result[i], sim3[i]])
                else:
                    obj_with_sim.append([results[i], sim1[i]])

	obj_with_sim.sort(key = lambda text: text[1], reverse = True)
	obj_with_sim = obj_with_sim[0: 10]
	obj_with_sim = [t[0] for t in obj_with_sim]

	return json.dumps(obj_with_sim)
