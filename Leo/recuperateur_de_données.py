from twython import Twython
import json
import os.path
import sys
import random
import pymongo



client = pymongo.MongoClient("mongodb://Admin:LesEmotions@cluster0-shard-00-00-nbixs.gcp.mongodb.net:27017,cluster0-shard-00-01-nbixs.gcp.mongodb.net:27017,cluster0-shard-00-02-nbixs.gcp.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.business
names = ['Kitchen','Animal','State', 'Tastey', 'Big','City','Fish', 'Pizza','Goat', 'Salty','Sandwich','Lazy', 'Fun']
company_type = ['LLC','Inc','Company','Corporation']
company_cuisine = ['Pizza', 'Bar Food', 'Fast Food', 'Italian', 'Mexican', 'American', 'Sushi Bar', 'Vegetarian']
for x in range(1, 501):
    business = {
        'name' : names[random.randint(0, (len(names)-1))] + ' ' + names[random.randint(0, (len(names)-1))]  + ' ' + company_type[random.randint(0, (len(company_type)-1))],
        'rating' : random.randint(1, 5),
        'cuisine' : company_cuisine[random.randint(0, (len(company_cuisine)-1))] 
    }
    result=db.reviews.insert_one(business)

print('Created {0} of 500 as {1}'.format(x,result.inserted_id))
print('finished creating 500 business reviews')



# python_tweets = Twython("byLgF6D4jMOstVEzCfHhwWk46", "EM9xsoauCKmNthC66aFz49gkbVpLWxzplQdtC0RmJtbtLgLA6D", "2234843953-lpTeqSMMZVGKyt4UtDxLg5KSkIigPItnOVYi0Yu", "IxwJNswdVSxAmQafZ4TSosW0I3SatmgBfpyiRiTwCrU2h")


# quer = ""
# i = 0
# for oui in sys.argv :
#     if (oui != sys.argv[0]) :
#         quer += oui + " OR " 
# while os.path.isfile("donnees"+str(i)+".json") :
#     i += 1
#     print("donnees"+str(i)+".json")

# quer = quer[0:-4]

# print(quer)

# with open("donnees"+str(i)+".json", "w") as donnees :
#     json.dump(python_tweets.search(q=quer , lang='fr', result_type='mixed', count=10, geocode = "46.858808,2.436929,800km"), donnees, sort_keys=True, indent=4)


# """'le OR la OR l OR je OR tu OR il OR nous OR vous OR ils OR elle OR elles OR ça OR opinion OR oui OR non OR pourquoi OR pense OR penser OR expression OR exprimer OR exprime OR montre OR prouve OR prouver OR montrer'"""