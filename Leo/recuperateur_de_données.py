from twython import Twython
import json
import os.path
import sys
import random
import pymongo
import re

client = pymongo.MongoClient("mongodb://Admin:LesEmotions@cluster0-shard-00-00-nbixs.gcp.mongodb.net:27017,cluster0-shard-00-01-nbixs.gcp.mongodb.net:27017,cluster0-shard-00-02-nbixs.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.tweets
col = db[sys.argv[1]]

# nom_col = sys.argv[1]

# print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
# print('finished creating 500 business reviews')



python_tweets = Twython("byLgF6D4jMOstVEzCfHhwWk46", "EM9xsoauCKmNthC66aFz49gkbVpLWxzplQdtC0RmJtbtLgLA6D", "2234843953-lpTeqSMMZVGKyt4UtDxLg5KSkIigPItnOVYi0Yu", "IxwJNswdVSxAmQafZ4TSosW0I3SatmgBfpyiRiTwCrU2h")


quer = ""
for oui in sys.argv[2 : ] :
    quer += str(oui) + " OR " 

quer = quer[0:-4]

dict_ = python_tweets.search(q=quer , lang='fr', result_type='mixed', count=10000)

i = 0
while (i < len(dict_["statuses"])) :
    if ("retweeted_status" in dict_["statuses"][i]) :
        
        if ((re.search(".*,.*", dict_["statuses"][i]["retweeted_status"]["user"]["location"]) is not None) and (col.count_documents({"_id" : dict_["statuses"][i]["retweeted_status"]["id_str"]}) == 0)) :
            print(col.count_documents({"id_" : dict_["statuses"][i]["retweeted_status"]["id_str"]}))
            print("\n" + dict_["statuses"][i]["retweeted_status"]["user"]["location"])
            print(dict_["statuses"][i]["retweeted_status"]["text"])
            print(dict_["statuses"][i]["retweeted_status"]["created_at"])
            print("https://twitter.com/i/web/status/" + dict_["statuses"][i]["retweeted_status"]["id_str"])
            print(dict_["statuses"][i]["retweeted_status"]["id_str"] + "\n")
            print(quer)
            tweet = {
                'location' : dict_["statuses"][i]["retweeted_status"]["user"]["location"],
                'text' : dict_["statuses"][i]["retweeted_status"]["text"],
                'date' : dict_["statuses"][i]["retweeted_status"]["created_at"],
                'url' : "https://twitter.com/i/web/status/" + dict_["statuses"][i]["retweeted_status"]["id_str"],
                '_id' : dict_["statuses"][i]["retweeted_status"]["id_str"]
            }
            result = col.insert_one(tweet)
            # print(i)
            # print("CECI EST UN retweet")
            # print(dict_["statuses"][i]["retweeted_status"]["user"]["location"])
            # print(dict_["statuses"][i]["retweeted_status"]["text"])
            # print("https://twitter.com/i/web/status/" + dict_["statuses"][i]["retweeted_status"]["id_str"])
        # else :
        #     print("Nique bien ta mère")
        #     print(dict_["statuses"][i]["retweeted_status"]["text"])
        #     print("https://twitter.com/i/web/status/" + dict_["statuses"][i]["retweeted_status"]["id_str"])
        # for key in dict_["statuses"][i]["retweeted_status"] :
        #     print(key)

    else :
        if ((re.search(".*,.*", dict_["statuses"][i]["user"]["location"]) is not None) and (col.count_documents({"_id" : dict_["statuses"][i]["id_str"]}) == 0)) :
            print(col.count_documents({"id_" : dict_["statuses"][i]["id_str"]}))
            print("\n" + dict_["statuses"][i]["user"]["location"])
            print(dict_["statuses"][i]["text"])
            print(dict_["statuses"][i]["created_at"])
            print("https://twitter.com/i/web/status/" + dict_["statuses"][i]["id_str"])
            print(dict_["statuses"][i]["id_str"] + "\n")
            print(quer)
            tweet = {
                'location' : dict_["statuses"][i]["user"]["location"],
                'text' : dict_["statuses"][i]["text"],
                'date' : dict_["statuses"][i]["created_at"],
                'url' : "https://twitter.com/i/web/status/" + dict_["statuses"][i]["id_str"],
                '_id' : dict_["statuses"][i]["id_str"]
            }
            result = col.insert_one(tweet)
            # print(i)
            # print("CECI EST UN tweet")
            # print(dict_["statuses"][i]["user"]["location"])
            # print(dict_["statuses"][i]["text"])
            # print("https://twitter.com/i/web/status/" + dict_["statuses"][i]["id_str"])
        # else :
        #     print("Nique bien ta mère")
        #     print(dict_["statuses"][i]["text"])
        #     print("https://twitter.com/i/web/status/" + dict_["statuses"][i]["id_str"])      
        # for key in dict_["statuses"][i] :
        #     print(key)

    i = i + 1


# col.rename(nom_col)
