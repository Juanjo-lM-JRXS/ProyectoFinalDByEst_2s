-- 7. Consultas y Análisis:

-- Consultas SQL para:
-- Obtener los 10 jugadores con mayor puntuación:

USE CallOfDutyBlackOpsII_DB;

SELECT IDJugador, NombreUsuario, Puntuación, Nivel, Equipo
FROM Jugadores
ORDER BY Puntuación DESC
LIMIT 10;

-- Verificar el inventario de un jugador específico:

SELECT IDJugador, NombreUsuario, Inventario
FROM Jugadores
WHERE IDJugador = '22';

-- Listar todas las partidas de un jugador en un rango de fechas:


