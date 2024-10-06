-- 1. Listar canciones por género (Consulta con JOIN)
SELECT Canciones.nombre AS 'Canción', GeneroMusical.nombre AS 'Género'
FROM Canciones
JOIN GeneroMusical ON Canciones.id_genero = GeneroMusical.id
WHERE GeneroMusical.nombre = 'Rock';  

-- 2. Listar canciones favoritas con nombre de las canciones y autores/bandas (Consulta con JOIN)
SELECT Canciones.nombre AS 'Canción', Artistas.nombre AS 'Artista/Banda'
FROM Favoritos
JOIN Canciones ON Favoritos.id_cancion = Canciones.id
JOIN Album ON Canciones.id_album = Album.id
JOIN Artistas ON Album.id_artista = Artistas.id
WHERE Favoritos.id_usuario = 1;  

-- 3. Agregar una canción a favoritos (INSERT en Favoritos)
INSERT INTO Favoritos (id_usuario, id_cancion)
VALUES (1, 2);  

-- 4. Eliminar una canción de favoritos (DELETE en Favoritos)
DELETE FROM Favoritos
WHERE id_usuario = 1 AND id_cancion = 2;  

-- 5. Actualizar nombre de una lista de reproducción (UPDATE en Playlist)
UPDATE Playlist
SET nombre = 'Nuevos Clásicos del Rock'
WHERE id = 1;  

-- 6. Listar todas las canciones de un álbum con su artista (Consulta con JOIN)
SELECT Canciones.nombre AS 'Canción', Album.nombre AS 'Álbum', Artistas.nombre AS 'Artista/Banda'
FROM Canciones
JOIN Album ON Canciones.id_album = Album.id
JOIN Artistas ON Album.id_artista = Artistas.id
WHERE Album.id = 1; 

-- 7. Agregar una canción a la playlist del usuario (INSERT en PlaylistCanciones)
INSERT INTO PlaylistCanciones (id_playlist, id_cancion)
VALUES (1, 2);  -- '1' es por el id de la playlist y '2' por el id de la canción como ejemplo

-- 8. Eliminar una canción de la playlist del usuario (DELETE en PlaylistCanciones)
DELETE FROM PlaylistCanciones
WHERE id_playlist = 1 AND id_cancion = 2;  

-- 9. Actualizar los datos de un usuario (UPDATE en Usuario)
UPDATE Usuario
SET nombre = 'Juan', apellido = 'Perez', correo_electronico = 'juan.perez@example.com'
WHERE id = 1; 

-- 10. Listar todas las playlists de un usuario (Consulta con JOIN)
SELECT Playlist.nombre AS 'Playlist'
FROM Playlist
JOIN Usuario ON Playlist.id_usuario = Usuario.id
WHERE Usuario.nombre_usuario = 'janesmith'; 

-- 11. Buscar canciones por artista/banda (Consulta con JOIN)
SELECT Canciones.nombre AS 'Canción', Artistas.nombre AS 'Artista/Banda'
FROM Canciones
JOIN Album ON Canciones.id_album = Album.id
JOIN Artistas ON Album.id_artista = Artistas.id
WHERE Artistas.nombre = 'The Beatles'; 