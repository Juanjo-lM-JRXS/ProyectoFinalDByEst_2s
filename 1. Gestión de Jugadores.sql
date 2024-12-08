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

-- Inserción de la información de los jugadores:
INSERT INTO Jugadores (NombreUsuario, Nivel, Puntuación, Equipo, Inventario)
VALUES 
('GhostKiller', 20, 5000, 'SEAL Team 6', 'SMG: MP7, Secundaria: Five-Seven, Equipamiento: Flashbang, Grenade'),
('ShadowHunter', 50, 15000, 'Militia', 'Assault: M8A1, Secundaria: KAP-40, Equipamiento: Smoke Grenade, Semtex'),
('IronWolf', 10, 2000, 'Mercs', 'Sniper: DSR-50, Secundaria: B23R, Equipamiento: Sensor Grenade, Claymore'),
('NightBlade', 35, 9000, 'FBI', 'LMG: LSAT, Secundaria: Tac-45, Equipamiento: EMP Grenade, C4'),
('CrimsonHawk', 45, 13000, 'ISA', 'Shotgun: R870 MCS, Secundaria: Executioner, Equipamiento: Concussion, Trophy System'),
('SteelPhoenix', 5, 1000, 'SEAL Team 6', 'SMG: MSMC, Secundaria: Five-Seven, Equipamiento: Frag Grenade, Smoke Grenade'),
('SilentStorm', 60, 20000, 'Militia', 'Assault: AN-94, Secundaria: Five-Seven, Equipamiento: EMP Grenade, C4'),
('LoneRanger', 25, 7000, 'FBI', 'Sniper: Ballista, Secundaria: B23R, Equipamiento: Shock Charge, Claymore'),
('DarkRaven', 15, 3500, 'ISA', 'SMG: PDW-57, Secundaria: KAP-40, Equipamiento: Flashbang, Frag Grenade'),
('BlazingFury', 55, 18000, 'Militia', 'Assault: SCAR-H, Secundaria: Tac-45, Equipamiento: Smoke Grenade, Semtex'),
('SilverFang', 12, 2800, 'Mercs', 'Shotgun: M1216, Secundaria: Executioner, Equipamiento: Shock Charge, Bouncing Betty'),
('ThunderViper', 40, 11000, 'FBI', 'Sniper: XPR-50, Secundaria: B23R, Equipamiento: EMP Grenade, Claymore'),
('VenomStrike', 22, 6000, 'SEAL Team 6', 'LMG: HAMR, Secundaria: Five-Seven, Equipamiento: Sensor Grenade, Trophy System'),
('GoldenEagle', 48, 14500, 'ISA', 'Assault: Type 25, Secundaria: KAP-40, Equipamiento: Concussion, Frag Grenade'),
('PhantomWolf', 30, 8500, 'Militia', 'SMG: Vector K10, Secundaria: Tac-45, Equipamiento: EMP Grenade, Semtex'),
('CrimsonVortex', 8, 1500, 'Mercs', 'Sniper: Ballista, Secundaria: Executioner, Equipamiento: Sensor Grenade, Claymore'),
('ShadowVenom', 18, 4500, 'FBI', 'Shotgun: R870 MCS, Secundaria: KAP-40, Equipamiento: Shock Charge, C4'),
('FlameStriker', 65, 22000, 'Militia', 'Assault: M27, Secundaria: Tac-45, Equipamiento: EMP Grenade, Trophy System'),
('ArcticWolf', 33, 9500, 'SEAL Team 6', 'Sniper: DSR-50, Secundaria: Five-Seven, Equipamiento: Smoke Grenade, Frag Grenade'),
('BlackPhoenix', 20, 5200, 'ISA', 'LMG: LSAT, Secundaria: B23R, Equipamiento: Flashbang, Semtex');

-- Consultar los datos:
SELECT * FROM Jugadores;
