from pymongo import MongoClient



client = MongoClient('localhost', 27017)

db = client.test_database



collection = db.test_collection

print(collection)
"""
Collection(Database(
MongoClient(host=['localhost:27017'], document_class=dict, 
tz_aware=False, connect=True), 'test_database'), 'test_collection')
"""



