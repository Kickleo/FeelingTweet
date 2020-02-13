from twython import Twython
import json
import pandas

with open("twitter_credentials.json", "r") as file :
    creds = json.load(file)

python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])

query = {'q': 'le',
        'lang': 'fr',
        'result_type': 'recent',
        'count': 10,
        }

dict_ = {'user': [], 'date': [], 'text': [], 'localisation': [], 'favorite_count': []}
for status in python_tweets.search(**query)['statuses'] :
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['localisation'].append(status['coordinates'])
    dict_['favorite_count'].append(status['favorite_count'])

df = pandas.DataFrame(dict_)
df.sort_values(by='date', inplace=True, ascending=False)
df.head(10)