from flask import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	mondic = {'Montpellier':'', 'Nice':''}
	if request.method == 'POST':
		return render_template('map5.html')
	else:
		return render_template('index.html', mondic=mondic)

@app.route('/rapport')
def rapport():
	return render_template('rapport.html')

if __name__ == "__main__":
    app.run()