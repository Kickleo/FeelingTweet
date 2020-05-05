import folium
import pandas as pd
import os
from twython import Twython
import csv
from pyFeel import Feel
import json
import nltk
import numpy as np





region = os.path.join('arrondissement.json')




with open('datatweets.json','r') as tw:
	data = tw.read()

data_tw = json.loads(data)

data_emotions={}

with open('emotion.csv','w',newline='') as emocsv :
	fieldname = ['Region','Emotion']
	emo_writer = csv.DictWriter(emocsv, fieldnames=fieldname)
	emo_writer.writeheader()


	for tw in data_tw :
		F_tw = Feel(tw.get('text'))
		emo_tw = F_tw.emotions()
		pos_tw = emo_tw['positivity']
		geo_tw1 = tw.get('location')
		geo_tw2 = geo_tw1.split(",")[0]

		
		if geo_tw2 not in data_emotions : 
			data_emotions[geo_tw2]=pos_tw;
		else :
			data_emotions[geo_tw2]=(data_emotions[geo_tw2]+pos_tw)/2

	for geo in data_emotions : 
		emo_writer.writerow({'Region' : geo , 'Emotion' : data_emotions[geo] })



emotion_data = os.path.join('emotion.csv')
region_data = pd.read_csv(emotion_data)



m = folium.Map(location=[46.5,2],zoom_start=6)



m.choropleth(
	geo_data=region,
	name='choropleth',
	data=region_data,
	columns=['Region','Emotion'],
	key_on='feature.properties.nom',
	fill_color='RdYlBu',
	nan_fill_color='white',
	fill_opacity=0.5,
	line_opacity=0.3,
	legend_name='Emotion',
	smooth_factor=0
	)
folium.LayerControl().add_to(m)



m.save('twitter.html')