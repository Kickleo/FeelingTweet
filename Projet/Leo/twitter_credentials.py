import json

credentials = {}
credentials['CONSUMER_KEY'] = 'byLgF6D4jMOstVEzCfHhwWk46'
credentials['CONSUMER_SECRET'] = 'EM9xsoauCKmNthC66aFz49gkbVpLWxzplQdtC0RmJtbtLgLA6D'
credentials['ACCESS_TOKEN'] = '2234843953-lpTeqSMMZVGKyt4UtDxLg5KSkIigPItnOVYi0Yu'
credentials['ACCESS_SECRET'] = 'IxwJNswdVSxAmQafZ4TSosW0I3SatmgBfpyiRiTwCrU2h'

with open("twitter_credentials.json", "w") as file :
    json.dump(credentials, file)