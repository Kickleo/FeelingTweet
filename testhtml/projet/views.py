from flask import *
import json
from flask.views import View

app = Flask(__name__)


with open('tweet.json','r') as tw:
	data = tw.read()

data_tw = json.loads(data)

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		return render_template('map5.html')
	else:
		return render_template('index.html', mondic=data_tw)

@app.route('/rapport')
def rapport():
	return render_template('rapport.html')

@app.route('/mapFrame')
def mapFrame():
	return render_template('map5.html')

if __name__ == "__main__":
	app.run()