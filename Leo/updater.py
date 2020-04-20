import pymongo
import os
import pymongo

client = pymongo.MongoClient("mongodb://Admin:LesEmotions@cluster0-shard-00-00-nbixs.gcp.mongodb.net:27017,cluster0-shard-00-01-nbixs.gcp.mongodb.net:27017,cluster0-shard-00-02-nbixs.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.tweets

cols = db.collection_names(include_system_collections=False, session=None)

for col in cols :
    print("python3 recuperateur_de_données.py " + col + " " + col)
    os.system("python3 recuperateur_de_données.py " + col + " " + col)