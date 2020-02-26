from flask import *
import json
from flask.views import View

app = Flask(__name__)


mondic = {"21/02/2020":"", "22/02/2020":""}

@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		return render_template('map5.html')
	else:
		return render_template('index.html', mondic=mondic)

@app.route('/rapport')
def rapport():
	return render_template('rapport.html')

@app.route('/map')
def map():
	return render_template('map5.html')

if __name__ == "__main__":
	app.run()