from database import db_session, init_db
from models import Zapatazo

### This file is for testing purposes ###

init_db()

z1 = Zapatazo(title = 'primer-zapatazo', imglink = 'static/images/zapatazo1.jpg')
db_session.add(z1)

z2 = Zapatazo(title = 'segundo-zapatazo', imglink = 'static/images/zapatazo2.jpg')
db_session.add(z2)

z3 = Zapatazo(title = 'tercer-zapatazo', imglink = 'static/images/zapatazo3.jpg')
db_session.add(z3)

z4 = Zapatazo(title = 'cuarto-zapatazo', imglink = 'static/images/zapatazo4.jpg')
db_session.add(z4)

z5 = Zapatazo(title = 'quinto-zapatazo', imglink = 'static/images/zapatazo5.jpg')
db_session.add(z5)

z6 = Zapatazo(title = 'sexto-zapatazo', imglink = 'static/images/zapatazo6.jpg')
db_session.add(z6)

z7 = Zapatazo(title = 'septimo-zapatazo', imglink = 'static/images/zapatazo7.jpg')
db_session.add(z7)

z8 = Zapatazo(title = 'octavo-zapatazo', imglink = 'static/images/zapatazo8.jpg')
db_session.add(z8)

z9 = Zapatazo(title = 'noveno-zapatazo', imglink = 'static/images/zapatazo9.jpg')
db_session.add(z9)


db_session.commit()


### SQL, just place holder ###

# INSERT INTO zapatazos VALUES(1,'Zapatazo 1','static/images/zapatazo.jpg');
# INSERT INTO zapatazos VALUES(2,'Zapatazo 2','static/images/zapatazo.jpg');
# INSERT INTO zapatazos VALUES(3,'Zapatazo 3','static/images/zapatazo.jpg');


# CREATE TABLE zapatazos (
# 	id serial PRIMARY KEY, 
# 	title text not null,
# 	imglink text not null
# );








