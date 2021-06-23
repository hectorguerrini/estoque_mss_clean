from pymongo import MongoClient

url = 'mongodb://dockerservice:dockerpw@localhost:27017/'
client = MongoClient(url, uuidRepresentation='standard')

db = client.get_database('estoque')
itensCollection = db.get_collection('itens')
