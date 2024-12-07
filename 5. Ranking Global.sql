-- 5. Ranking Global:

/* Consulta y actualización del ranking global basado en la puntuación de los jugadores,
calculando las posiciones mediante un procedimiento almacenado: */

USE CallOfDutyBlackOpsII_DB;

-- Consultar el ranking global
DELIMITER //
CREATE PROCEDURE ConsultarRankingGlobal()
BEGIN
	SELECT IDJugador, NombreUsuario, Nivel, Puntuación,
    ROW_NUMBER() OVER (ORDER BY Puntuación DESC) AS PosiciónRankingGlobal
    FROM Jugadores
    ORDER BY Puntuación DESC;
END //
DELIMITER ;

CALL ConsultarRankingGlobal()