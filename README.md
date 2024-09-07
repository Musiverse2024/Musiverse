# Musiverse
#Proyecto Integrador del modulo Innovacion en gestion de datos.

Nombre de los integrantes:
	Lucas Brocanelli
	Marco Virinni
	Emilce Robles
	Mario Arce
	Gabriela Acosta
	Jenifer De Piano
	
----------------------------------------------------------------------------------------------------------------------------------------------------

Descripcion del proyecto:

	El proyecto final consiste en el desarrollo de un programa que permite a los usuarios gestionar y reproducir música mediante una base de datos relacional. Los usuarios podrán buscar canciones por género, banda o nombre, crear playlists personalizadas, y marcar sus canciones favoritas. También incluye la funcionalidad de llevar un historial de reproducción con el horario en que se escuchó cada canción, así como la posibilidad de escuchar una canción aleatoria según el género musical preferido. El backend estará desarrollado en Python y la base de datos será gestionada con MySQL.
	
----------------------------------------------------------------------------------------------------------------------------------------------------
	
	Detalles de la Base de Datos: 


	1. Descripción General: 
La base de datos que sustenta nuestra aplicación de música está diseñada para gestionar de forma eficiente los datos relacionados con usuarios, canciones, artistas, álbumes, géneros musicales y actividades de los usuarios, como la creación de playlists y el registro de canciones favoritas. Esta base permite a los usuarios buscar música y realizar acciones como guardar canciones en sus listas de reproducción o favoritos, así como registrar el historial de reproducción, todo con un enfoque en la personalización.

	2. Tablas:
Las tablas forman la estructura principal del sistema, cada una con un propósito específico:
usuario: Almacena la información básica de los usuarios, como nombre, correo electrónico y fecha de nacimiento.
canciones: Registra los datos esenciales de cada canción, como su nombre, el álbum al que pertenece y el género.
album: Contiene los datos de los álbumes, incluyendo su nombre y la fecha de lanzamiento.
artistas: Guarda información sobre los artistas relacionados con los álbumes.
generomusical: Lista los géneros musicales disponibles en el sistema.
playlist: Administra las listas de reproducción creadas por los usuarios.
playlistcanciones: Relaciona canciones con playlists, permitiendo que una canción pertenezca a múltiples listas.
favoritos: Permite a los usuarios guardar canciones como favoritas.
historialreproduccion: Almacena el registro de las canciones reproducidas por cada usuario, incluyendo la fecha y hora de reproducción.


	3. Relaciones: 
Usuario - Playlist (1): Un usuario puede crear varias playlists, pero cada playlist pertenece únicamente a un usuario.
Playlist - Canciones (N): Una playlist puede contener varias canciones y una canción puede estar en múltiples playlists. Esta relación se gestiona a través de la tabla intermedia playlistcanciones, que enlaza las playlists con las canciones.
Usuario - Favoritos (1): Un usuario puede marcar varias canciones como favoritas, pero cada entrada en la tabla de favoritos está asociada a un solo usuario.
Canción - Álbum (1): Un álbum puede contener varias canciones, pero cada canción pertenece a un solo álbum.
Álbum - Artista (1): Un artista puede tener varios álbumes, pero cada álbum está relacionado con un único artista.
Canción - Género Musical (1): Un género musical puede agrupar varias canciones, pero cada canción pertenece a un único género.
Usuario - Historial de Reproducción (1): Un usuario puede reproducir varias canciones en diferentes momentos, registrándose cada reproducción en la tabla de historial con el usuario y la canción correspondientes.
	
	4. Conclusión:. 
Este proyecto presenta una solución funcional para la gestión de usuarios, canciones y playlists. La estructura de la base de datos permite organizar de manera eficiente las interacciones clave dentro de la aplicación, lo que facilita una experiencia de usuario personalizada. Además, el uso de herramientas accesibles como MySQL y Python asegura que el desarrollo sea manejable y esté respaldado por una amplia documentación.
A medida que el proyecto evolucione, será importante prestar atención al rendimiento, especialmente en la optimización de consultas, para garantizar un buen tiempo de respuesta.

----------------------------------------------------------------------------------------------------------------------------------------------------



	

