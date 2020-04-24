from flask import *
import json
from flask.views import View
import subprocess

app = Flask(__name__)

mondic={"Coronavirus",
"Confinement",
"E32020",
"Fillon",
"Football",
"Macron",
"MoisDesDroitsDeLaFemme"};

@app.route('/', methods=['GET','POST'])
def index():
	if request.method == 'POST':
		
		theme = request.form.get('themes')

		subprocess.run(["python3 tweetmap.py "+str(theme)+" "+str(theme)],shell=True)

		return render_template('index.html', mondic=mondic)

	else:
		return render_template('index.html', mondic=mondic)

@app.route('/rapport')
def rapport():
	return render_template('rapport.html')

@app.route('/mapFrame')
def mapFrame():
	return render_template('twitter.html')

if __name__ == "__main__":
	app.run()