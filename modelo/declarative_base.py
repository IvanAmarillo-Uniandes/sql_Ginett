# crea el motor de la base
# crea el objeto sesion (con el que abrimos y cerramos sesiones para consultar la info)
# crea el objeto base

# importamos funcionalidad necesaria
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///aplicacion.sqlite')
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()
