from flask import *
import json
from flask.views import View

app = Flask(__name__)


mondic = {"21/02/2020":"", "22/02/2020":""}

@app.route('/', methods=['GET','POST'])
def index():
	map = 'templates/map5.html'

	if request.method == 'POST':
		return render_template('map5.html')
	else:
		return render_template('index.html', mondic=mondic , map=map)

@app.route('/rapport')
def rapport():
	return render_template('rapport.html')

if __name__ == "__main__":
	app.run()