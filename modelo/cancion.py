
# importar la funcionalidad
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base

class Cancion(Base):
	# nombre de la tabla
	__tablename__ = 'cancion'

	# atributos
	id = Column(Integer, primary_key=True)
	titulo = Column(String)
	minutos = Column(Integer)
	segundos = Column(Integer)
	compositor = Column(String)
	albumes = relationship('Album', secondary='album_cancion')
	interpretes = relationship('Interprete', cascade='all, delete, delete-orphan')

class AlbumCancion(Base):

	# nomre de la table
	__tablename__='album_cancion'

	# atributos
	cancion_id = Column(Integer, ForeignKey('cancion.id'), primary_key=True)
	album_id = Column(Integer, ForeignKey('album.id'), primary_key=True)
