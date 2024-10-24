CREATE DATABASE IF NOT EXISTS musiverseDB;
USE musiverseDB;

-- Tabla de usuarios
CREATE TABLE IF NOT EXISTS Usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    apellido VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL UNIQUE,
    fecha_nacimiento DATE NOT NULL,
    nombre_usuario VARCHAR(100) NOT NULL UNIQUE,
    clave VARCHAR(255) NOT NULL, -- Se aumenta a 255 para almacenar contraseñas cifradas
    dni INT NOT NULL UNIQUE
);

-- Tabla de géneros musicales
CREATE TABLE IF NOT EXISTS GeneroMusical (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla intermedia para almacenar los géneros seleccionados por cada usuario
CREATE TABLE IF NOT EXISTS UsuarioGenero (
    id_usuario INT,
    id_genero INT,
    PRIMARY KEY (id_usuario, id_genero),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id),
    FOREIGN KEY (id_genero) REFERENCES GeneroMusical(id)
);

-- Tabla de artistas
CREATE TABLE IF NOT EXISTS Artistas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL
);

-- Tabla de álbumes
CREATE TABLE IF NOT EXISTS Album (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    fecha_lanzamiento DATE NOT NULL,
    id_artista INT,
    FOREIGN KEY (id_artista) REFERENCES Artistas(id)
);

-- Tabla de canciones
CREATE TABLE IF NOT EXISTS Canciones (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_album INT,
    id_genero INT,
    FOREIGN KEY (id_album) REFERENCES Album(id),
    FOREIGN KEY (id_genero) REFERENCES GeneroMusical(id)
);

-- Tabla de listas de reproducción (Playlists)
CREATE TABLE IF NOT EXISTS Playlist (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    id_usuario INT,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id)
);

-- Tabla de relación entre listas de reproducción y canciones (PlaylistCanciones)
CREATE TABLE IF NOT EXISTS PlaylistCanciones (
    id_playlist INT,
    id_cancion INT,
    PRIMARY KEY (id_playlist, id_cancion),
    FOREIGN KEY (id_playlist) REFERENCES Playlist(id),
    FOREIGN KEY (id_cancion) REFERENCES Canciones(id)
);



-- Tabla de historial de reproducción
CREATE TABLE IF NOT EXISTS HistorialReproduccion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_cancion INT,
    fecha_reproduccion DATETIME NOT NULL,
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id),
    FOREIGN KEY (id_cancion) REFERENCES Canciones(id)
);

-- Tabla de canciones favoritas
CREATE TABLE IF NOT EXISTS Favoritos (
    id_usuario INT,
    id_cancion INT,
    PRIMARY KEY (id_usuario, id_cancion),
    FOREIGN KEY (id_usuario) REFERENCES Usuario(id),
    FOREIGN KEY (id_cancion) REFERENCES Canciones(id)
);

-- Crea índice en la columna id_playlist
CREATE INDEX idx_playlist ON PlaylistCanciones (id_playlist);

-- Crea índice en la columna id_cancion
CREATE INDEX idx_cancion ON PlaylistCanciones (id_cancion);


-- Crea índice en la columna id_usuario
CREATE INDEX idx_usuario_favoritos ON Favoritos (id_usuario);

-- Crea índice en la columna id_cancion
CREATE INDEX idx_cancion_favoritos ON Favoritos (id_cancion);


-- Insertar géneros musicales
INSERT INTO GeneroMusical (nombre) VALUES 
('Rock'), 
('Pop'), 
('Jazz'), 
('Blues');

-- Insertar artistas
INSERT INTO Artistas (nombre) VALUES 
('The Beatles'), 
('Led Zeppelin'), 
('Miles Davis'), 
('B.B. King');

-- Insertar álbumes
INSERT INTO Album (nombre, fecha_lanzamiento, id_artista) 
VALUES 
('Abbey Road', '1969-09-26', 1),
('Led Zeppelin', '1969-01-12', 2),
('Kind of Blue', '1959-08-17', 3),
('Live at the Regal', '1965-11-21', 4);

-- Insertar canciones
INSERT INTO Canciones (nombre, id_album, id_genero) 
VALUES 
('Come Together', 1, 1),
('Something', 1, 1),
('Good Times Bad Times', 2, 1),
('Communication Breakdown', 2, 1),
('So What', 3, 3),
('Freddie Freeloader', 3, 3),
('Every Day I Have the Blues', 4, 4),
('Sweet Little Angel', 4, 4);

-- Insertar usuarios
INSERT INTO Usuario (nombre, apellido, correo_electronico, fecha_nacimiento, nombre_usuario, clave, dni) 
VALUES 
('John', 'Doe', 'john.doe@example.com', '1990-05-15', 'johndoe', '123456', 12345678),
('Jane', 'Smith', 'jane.smith@example.com', '1985-08-23', 'janesmith', 'abcdef', 87654321);

-- Insertar géneros seleccionados por los usuarios
INSERT INTO UsuarioGenero (id_usuario, id_genero) 
VALUES 
(1, 1),
(1, 2), 
(2, 3), 
(2, 4); 

-- Insertar listas de reproducción
INSERT INTO Playlist (nombre, id_usuario) 
VALUES 
('Rock Classics', 1),
('Jazz Essentials', 2);

-- Insertar canciones en las listas de reproducción
INSERT INTO PlaylistCanciones (id_playlist, id_cancion) 
VALUES 
(1, 1), -- Come Together en Rock Classics
(1, 3), -- Good Times Bad Times en Rock Classics
(2, 5), -- So What en Jazz Essentials
(2, 7); -- Every Day I Have the Blues en Jazz Essentials

-- Insertar historial de reproducción con fechas reales
INSERT INTO HistorialReproduccion (id_usuario, id_cancion, fecha_reproduccion) 
VALUES 
(1, 1, '2024-01-10 10:30:00'),  -- Usuario 1 escuchó la canción 1 el 10 de enero de 2024 a las 10:30 AM
(1, 3, '2024-01-15 14:45:00'),  -- Usuario 1 escuchó la canción 3 el 15 de enero de 2024 a las 2:45 PM
(2, 5, '2024-02-05 09:20:00'),  -- Usuario 2 escuchó la canción 5 el 5 de febrero de 2024 a las 9:20 AM
(2, 7, '2024-02-10 18:00:00');  -- Usuario 2 escuchó la canción 7 el 10 de febrero de 2024 a las 6:00 PM

-- Insertar canciones favoritas
INSERT INTO Favoritos (id_usuario, id_cancion) 
VALUES 
(1, 1), -- John Doe marcó como favorita la canción 'Come Together'
(2, 5); -- Jane Smith marcó como favorita la canción 'So What'