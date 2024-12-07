Equipos = {}

Equipos["A"] = {"jugador1","jugador2","jugador 3"}
Equipos["B"] = {"jugador4","jugador5","jugador7"}

Equipos ["C"] = "jugador6"
print("")
print("los equipos totales son los siguientes ", Equipos)
print("")
print("la clasificacion del grupo A es ", Equipos.get("A"))
print("")
print("la clasificacion del grupoo B es ", Equipos.get("B"))
print("")
print("la clasificacion del grupoo C es ", Equipos.get("C"))
print("")



del Equipos["C"]
print("el equipo C ha sido eliminado")
print("")



Equipos["B"] = [{"jugador4","jugador5","jugador6"}]

print("la actualizacion del equipo B quedo ", Equipos.get("B"))
print("")

print("los equipos totales son los siguientes ", Equipos)
print("")



