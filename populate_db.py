from database import db_session, init_db
from models import Zapatazo

init_db()

#z1 = Zapatazo(title = 'Prueba')
#db_session.add(z1)


z2 = Zapatazo(title = 'Prueba 2')
db_session.add(z2)


z3 = Zapatazo(title = 'Prueba 3')
db_session.add(z3)


db_session.commit()









