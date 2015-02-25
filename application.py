from flask import Flask, render_template
from database import init_db, db_session
from models import Zapatazo

app = Flask(__name__)
init_db()

@app.route('/')
def main_page():
	#TODO
	#Agarrar la info de las fotos y pasarlas al html
	#Como agarrar un cierto numero de entradas en vez de todos?

	zapatazos = db_session.query(Zapatazo).all()
	print "zapatazos: ", zapatazos
	return render_template('index.html', zapatazos = zapatazos)
	


@app.route('/purozapatazos')
def purozapatazos():
	return render_template('purozapatazos.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)