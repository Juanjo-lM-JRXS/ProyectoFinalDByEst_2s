-- 1. Gestión de Jugadores:

-- Operaciones CRUD (CLAE) con Storaged Procedures (Procedimientos Almacenados):

USE CallOfDutyBlackOpsII_DB;

-- 1. Registro de nuevos jugadores:
DELIMITER //
CREATE PROCEDURE RegistrarJugadorNuevo(
    IN J_NombreUsuario VARCHAR(50),
    IN J_Nivel INT,
    IN J_Puntuacion INT,
    IN J_Equipo VARCHAR(50),
    IN J_Inventario TEXT
)
BEGIN
    INSERT INTO Jugadores (NombreUsuario, Nivel, Puntuación, Equipo, Inventario)
    VALUES (J_NombreUsuario, J_Nivel, J_Puntuación, J_Equipo, J_Inventario);
END //
DELIMITER ;

CALL RegistrarJugadorNuevo('DismalSkull', 616, 999999, 'Metalheads', 'M16, Granada, Escudo Táctico');

-- 2. Consulta de un jugador de manera individual:
DELIMITER //
CREATE PROCEDURE ConsultarJugadorÚnico (
    IN J_ID INT
)
BEGIN
    SELECT * FROM Jugadores WHERE IDJugador = J_ID;
END //
DELIMITER ;

CALL ConsultarJugadorÚnico('21');

-- 2.1. Consulta de todos los jugadores actuales:
DELIMITER //
CREATE PROCEDURE ConsultarListaJugadores (
)
BEGIN
    SELECT * FROM Jugadores;
END //
DELIMITER ;

CALL ConsultarListaJugadores();

-- 3. Modificación de la información de un jugador
DELIMITER //
CREATE PROCEDURE ModificarInformaciónJugador (
    IN J_ID INT,
    IN J_NombreUsuario VARCHAR(50),
    IN J_Nivel INT,
    IN J_Puntuacion INT,
    IN J_Equipo VARCHAR(50),
    IN J_Inventario TEXT
)
BEGIN
    UPDATE Jugadores SET IDJugador = J_ID WHERE IDJugador = J_ID;
    UPDATE Jugadores SET NombreUsuario = J_NombreUsuario WHERE IDJugador = J_ID;
    UPDATE Jugadores SET Nivel = J_Nivel WHERE IDJugador = J_ID;
    UPDATE Jugadores SET Puntuación = J_Puntuacion WHERE IDJugador = J_ID;
    UPDATE Jugadores SET Equipo = J_Equipo WHERE IDJugador = J_ID;
    UPDATE Jugadores SET Inventario = J_Inventario WHERE IDJugador = J_ID;
END //
DELIMITER ;

CALL ModificarInformaciónJugador(1, 'Corpsegrinder', 700, 100000, 'Metalheads', 'AK-47, Botiquín Mejorado, Mina Antipersonal');


-- 4. Supresión de un jugador en concreto
DELIMITER //
CREATE PROCEDURE EliminarJugadorEspecífico (
    IN J_ID INT
)
BEGIN
    DELETE FROM Jugadores WHERE IDJugador = J_ID;
END //
DELIMITER ;

CALL EliminarJugadorEspecífico(4);