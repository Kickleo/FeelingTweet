from flask import *
import json
from flask.views import View
import subprocess

app = Flask(__name__)


with open('tweet.json','r') as tw:
	data = tw.read()

data_tw = json.loads(data)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		with open('tweet.json','r') as tw:
			data = tw.read()
		subprocess.run(["python3 twitter.py"],shell=True)
		data_tw2 = json.loads(data)

		return render_template('index.html', mondic=data_tw2)

	else:
		return render_template('index.html', mondic=data_tw)

@app.route('/rapport')
def rapport():
	return render_template('rapport.html')

@app.route('/mapFrame')
def mapFrame():
	return render_template('twitter.html')

if __name__ == "__main__":
	app.run()