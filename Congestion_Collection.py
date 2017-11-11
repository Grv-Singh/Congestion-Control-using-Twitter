import json, requests,pymongo

r = requests.get('https://traffic.longdo.com/api/json/traffic/index?callback=get')

def get(r):
	data = r.json
	save_to_mongo(data, mongo_db, mongo_db_coll, **mongo_conn_kw)
	
def save_to_mongo(data, mongo_db, mongo_db_coll, **mongo_conn_kw):

	# Connects to the MongoDB server running on
	# localhost:27017 by default

	client = pymongo.MongoClient(**mongo_conn_kw)

	# Get a reference to a particular database

	db = client[mongo_db]

	# Reference a particular collection in the database

	coll = db[mongo_db_coll]

	# Perform a bulk insert and return the IDs

	coll.insert(data)
