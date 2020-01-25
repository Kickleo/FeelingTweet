from twython import Twython
import json
import os
from dotenv import load_dotenv
load_dotenv()

with open("twitter_credentials.json", "r") as file:
    creds = json.load(file)


python_tweets = Twython(creds['CONSUMER_KEY'], creds['CONSUMER_SECRET'])


query = {'q': 'amour'+" -filter:retweets",
        'result_type': 'mixed',
        'count': 100,
        'lang': 'fr',
        }
import pandas as pd
a=['s']
dict_ = {'user': [], 'date': [], 'text': [], 'favorite_count': [],'user_loc' : [],'emotion': []}
for status in python_tweets.search(**query)['statuses']:
    
    dict_['user'].append(status['user']['screen_name'])
    dict_['date'].append(status['created_at'])
    dict_['text'].append(status['text'])
    dict_['favorite_count'].append(status['favorite_count'])
    dict_['user_loc'].append(status['user']['location'])
    dict_['emotion'].append(0)
df = pd.DataFrame(dict_)
df.sort_values(by='favorite_count', inplace=True, ascending=False)
df.head(5)

import psycopg2
from sqlalchemy import create_engine

connection = psycopg2.connect(user = os.getenv('user'),
password = os.getenv('password'),
host = os.getenv('host'),
port = os.getenv('port'),
database = os.getenv('database'))

cursor = connection.cursor()
cursor.execute("SELECT version();")
record = cursor.fetchone()



from sqlalchemy import create_engine
engine = create_engine(os.getenv('URI'))
df.to_sql('table_name', engine,if_exists = 'replace')   
data1=pd.read_sql('SELECT * FROM table_name', engine) 





import pandas as pd


from collections import Counter
import ast

tweets = data1
tweets.head()
list=[]
for entry in tweets.text:
 list.append(entry)




counter_hashtags = Counter(list)
counter_hashtags.most_common(20)

dico1={}

print(tweets)
b={}

from pyFeel import Feel
i=0
c=""
for index, row in tweets.iterrows():
 

    c=Feel(row.text)
    d=c.emotions()
    dico1=row
    
    if d['positivity']>=0.5:
      tweets.loc[index,'emotion']='1'
    if d['joy']>=0.5:
   
        tweets.loc[index,'emotion']='2'
    if d['sadness']>=0.5:
 
      tweets.loc[index,'emotion']='3'
    if d['fear']>=0.5:
 
      tweets.loc[index,'emotion']='4'
    if d['angry']>=0.5:
    
      tweets.loc[index,'emotion']='5'
    if d['surprise']>=0.5:
 
      tweets.loc[index,'emotion']='6'
    if d['disgust']>=0.5:

      tweets.loc[index,'emotion']='7'




from geopy.geocoders import Nominatim
import gmplot

geolocator = Nominatim()

liste1y=1000
liste1x=-1000
#coordonné chaumont
liste2y=-1000
liste2x=1000
a=0
b=0
import folium

m= folium.Map(location=[b,a],zoo_start=12)
tooltip = 'Click here for more info'
logoIcon=folium.features.CustomIcon('sad.png',icon_size=(50,50))
popup=''

icon=''
coordinates = {'latitude': [], 'longitude': []}






for index, row in tweets.iterrows():
    try:
        location = geolocator.geocode(row['user_loc'])
        print(row['user_loc'])
        if location:

            a=location.longitude
            b=location.latitude
            print(row['emotion'])
            if b <= liste1y  and a>=liste1x and b>= liste2y and a<=liste2x  : 
             if row['emotion']=='1':
              print("ok")
              logoIcon=folium.features.CustomIcon('happy.png',icon_size=(50,50))
              folium.Marker([b,a],
                            popup='<strong>location one</strong>',
                            tooltip=tooltip,
                            icon=logoIcon).add_to(m)
             if row['emotion']=='2':
              logoIcon=folium.features.CustomIcon('joy.png',icon_size=(50,50))
              folium.Marker([b,a],
                            popup='<strong>location one</strong>',
                            tooltip=tooltip,
                            icon=logoIcon).add_to(m)
             if row['emotion']=='3':
              logoIcon=folium.features.CustomIcon('sadness.png',icon_size=(50,50))
              folium.Marker([b,a],
                            popup='<strong>location one</strong>',
                            tooltip=tooltip,
                            icon=logoIcon).add_to(m)
             if row['emotion']=='4':
              logoIcon=folium.features.CustomIcon('fear.png',icon_size=(50,50))
              folium.Marker([b,a],
                            popup='<strong>location one</strong>',
                            tooltip=tooltip,
                            icon=logoIcon).add_to(m)
             if row['emotion']=='5':
              logoIcon=folium.features.CustomIcon('angry.png',icon_size=(50,50))
              folium.Marker([b,a],
                            popup='<strong>location one</strong>',
                            tooltip=tooltip,
                            icon=logoIcon).add_to(m)
             if row['emotion']=='6':
              logoIcon=folium.features.CustomIcon('surprise.png',icon_size=(50,50))
              folium.Marker([b,a],
                            popup='<strong>location one</strong>',
                            tooltip=tooltip,
                            icon=logoIcon).add_to(m)
             if row['emotion']=='7':
              logoIcon=folium.features.CustomIcon('digust.png',icon_size=(50,50))
              folium.Marker([b,a],
                            popup='<strong>location one</strong>',
                            tooltip=tooltip,
                            icon=logoIcon).add_to(m)                                                        

        coordinates['latitude'].append(location.latitude)
        coordinates['longitude'].append(location.longitude)
    except:
        pass
    
gmap = gmplot.GoogleMapPlotter(30, 0, 3)

gmap.heatmap(coordinates['latitude'], coordinates['longitude'], radius=20)

m.save('map5.html')
