from pymongo import MongoClient



client1 = MongoClient()
client2 = MongoClient('localhost', 27017)

#db = client.test_database



print(client1.list_database_names())
print(client2.list_database_names())

