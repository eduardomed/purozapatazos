from database import db_session, init_db
from models import Zapatazo

### This file is for testing purposes ###

init_db()

z1 = Zapatazo(title = 'Primer Zapatazo', imglink = 'static/images/zapatazo1.jpg')
db_session.add(z1)


z2 = Zapatazo(title = 'Segundo Zapatazo', imglink = 'static/images/zapatazo2.jpg')
db_session.add(z2)


z3 = Zapatazo(title = 'Tercer Zapatazo', imglink = 'static/images/zapatazo3.jpg')
db_session.add(z3)


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








