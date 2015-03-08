from flask import Flask, render_template, jsonify, request
from database import init_db, db_session
from models import Zapatazo

app = Flask('purozapatazos')
init_db()


@app.route('/')
def main_page():
	#TODO
	zapatazos = db_session.query(Zapatazo).limit(12)
	print "zapatazos: ", zapatazos
	return render_template('index.html', zapatazos = zapatazos)
	
@app.route('/load_more.json')
def load_more():
	offset = request.args.get('offset')
	# print "offset: ", offset
	zapatazos = db_session.query(Zapatazo).offset(offset).limit(12)
	# print "ZAPATAZO: ", zapatazos
	return jsonify(Zapatazo=[i.serialize for i in zapatazos])     

@app.route('/acerca/')
def purozapatazos():
	return render_template('acerca.html')

@app.route('/<int:the_number>/')
def unzapatazo(the_number):
	zapatazo = db_session.query(Zapatazo).filter(Zapatazo.id == the_number).one()
	# print "ZAPATAZO: ", zapatazo
	return render_template('unzapatazo.html', zapatazo = zapatazo)

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 8000)