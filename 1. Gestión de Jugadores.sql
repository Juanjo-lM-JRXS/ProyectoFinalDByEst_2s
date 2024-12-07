-- 1. Gestión de Jugadores:

-- Administración de la información de los usuarios:

-- Creación de la base de datos:
CREATE DATABASE CallOfDutyBlackOpsII_DB;
USE CallOfDutyBlackOpsII_DB;

-- Creación de la tabla de jugadores:
CREATE TABLE Jugadores (
    IDJugador INT AUTO_INCREMENT PRIMARY KEY,
    NombreUsuario VARCHAR(50) NOT NULL UNIQUE,
    Nivel INT NOT NULL,
    Puntuación INT NOT NULL DEFAULT 0,
    Equipo VARCHAR(50) NOT NULL,
    Inventario TEXT
);

-- Inserción de registros:
INSERT INTO Jugadores (NombreUsuario, Nivel, Puntuación, Equipo, Inventario)
VALUES 
    ('ShadowHunter', 15, 1250, 'Equipo Alfa', 'AK-47, Granada, Botiquín'),
    ('SteelSniper', 22, 2150, 'Equipo Bravo', 'M14, Camuflaje, Kit de Supervivencia'),
    ('GhostKiller', 30, 3500, 'Equipo Alfa', 'Pistola Silenciada, Mina, Radar portátil'),
    ('BulletStorm', 10, 800, 'Equipo Charlie', 'Escopeta, Granada de humo, Chaleco Antibalas');

-- Consultar los datos:
SELECT * FROM Jugadores;

	



