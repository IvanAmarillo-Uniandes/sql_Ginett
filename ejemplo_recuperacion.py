
# importar la funcionalidad
from modelo.cancion import Cancion
from modelo.interprete import Interprete
from modelo.album import Album, Medio
from modelo.declarative_base import Session, engine, Base

if __name__ == '__main__':

	# iniciamos la sesión
	session = Session()
	canciones = session.query(Cancion).all()

	print('Las canciones almacenadas son:')
	for cancion in canciones:
		#imprime los titulos de las canciones y sus tiempos
		print('Titulo: ' + cancion.titulo + " (00:" + str(cancion.minutos)
			+ ":" + str(cancion.segundos) + ")")

		#imprime los interpretes
		print('Intérpretes')
		for interprete in cancion.interpretes:
			print('-' + interprete.nombre)

		# imprime los albumes en el que esta la cancion
		for album in cancion.albumes:
			print(' -- Presente en el album: ' + album.titulo)

		print('')

	print('Los álbumes almacenados en discos son:')
	albumes = session.query(Album).filter(Album.medio == Medio.DISCO).all()

	for album in albumes:
		print('Album: {} \tAño: {}'.format(album.titulo, album.ano))

	session.close()