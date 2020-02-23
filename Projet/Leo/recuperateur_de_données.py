from twython import Twython
import json

python_tweets = Twython("byLgF6D4jMOstVEzCfHhwWk46", "EM9xsoauCKmNthC66aFz49gkbVpLWxzplQdtC0RmJtbtLgLA6D", "2234843953-lpTeqSMMZVGKyt4UtDxLg5KSkIigPItnOVYi0Yu", "IxwJNswdVSxAmQafZ4TSosW0I3SatmgBfpyiRiTwCrU2h")

with open("donnees.json", "w") as donnees :
    json.dump(python_tweets.search(q='le OR la OR l OR je OR tu OR il OR nous OR vous OR ils OR elle OR elles OR ça', lang='fr', result_type='recent', count=10), donnees, sort_keys=True, indent=4)