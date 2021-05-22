from pymongo import MongoClient



client = MongoClient('localhost', 27017)



print(client.list_database_names())






db = client.test_database



import datetime

post = {"author": "Mike", "text": "My first blog post!", 
	"tags": ["mongodb", "python", "pymongo"], 
	"date": datetime.datetime.utcnow()}


posts = db.posts



post_id = posts.insert_one(post).inserted_id

print(post_id)

