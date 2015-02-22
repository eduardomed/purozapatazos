from flask import Flask, render_template
from database import init_db, db_session
from models import Zapatazo

app = Flask(__name__)
init_db()

@app.route('/')
def main_page():
	return render_template('index.html')

@app.route('/purozapatazos')
def purozapatazos():
	return render_template('purozapatazos.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)