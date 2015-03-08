from sqlalchemy import Column, Integer, Text
from database import Base

class Zapatazo(Base):
	__tablename__ = 'zapatazos'
	id = Column(Integer, primary_key=True)
	# title = Column(Text, unique=True)
	imglink = Column(Text, unique=True)

	def __repr__(self):
		return '<Zapatazo %r>' % (self.id)

	@property 
	def serialize(self):
		return {
       			'id' : self.id,
       			'imglink' : self.imglink
       		   }


