from flask import Flask, render_template, jsonify, request
from database import init_db, db_session
from models import Zapatazo

app = Flask(__name__)
init_db()


@app.route('/')
def main_page():
	#TODO

	zapatazos = db_session.query(Zapatazo).limit(3)
	# print "zapatazos: ", zapatazos
	return render_template('index.html', zapatazos = zapatazos)
	
@app.route('/load_more.json')
def load_more():
	#return JSON object? or return the new query?

	offset = request.args.get('offset', '')
	print "offset: ", offset
	zapatazos = db_session.query(Zapatazo).offset(offset).limit(3)
	print "ZAPATAZO: ", zapatazos
	return jsonify(Zapatazo=[i.serialize for i in zapatazos])     

@app.route('/purozapatazos/')
def purozapatazos():
	return render_template('purozapatazos.html')

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)