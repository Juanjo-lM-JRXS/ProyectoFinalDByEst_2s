import datetime

class SistemaBatallasPartidas:
    print("Hola")

class Partida: #Gestion enfrentamientos
    def __init__(self, equipo1, equipo2, fecha=None):
        self.equipo1 = equipo1  # Lista de jugadores del equipo 1
        self.equipo2 = equipo2  # Lista de jugadores del equipo 2
        self.fecha = fecha or datetime.datetime.now()  # Fecha de la partida
        self.resultado = None  # Guardar el resultado de la partida (opcional)

    def establecer_resultado(self, ganador):
        """Establece qué equipo ganó la partida."""
        self.resultado = ganador

class SistemaBatallas: #Gestion partidas
    def __init__(self):
        self.historial = None  # Árbol binario para almacenar el historial

    def organizar_partida(self, equipo1, equipo2):
        partida = Partida(equipo1, equipo2)
        self._agregar_al_historial(partida)
        return partida

    def _agregar_al_historial(self, partida):
        """Agrega la partida al historial como nodo del árbol binario."""
        if self.historial is None:
            self.historial = Nodo(partida)
        else:
            self.historial.insertar(partida)

    def mostrar_historial(self):
        """Muestra el historial ordenado por fecha."""
        if self.historial:
            self.historial.recorrido_inorden()
        else:
            print("No hay partidas registradas.")

class Nodo:
    def __init__(self, partida):
        self.partida = partida
        self.izquierdo = None
        self.derecho = None

    def insertar(self, nueva_partida):
        if nueva_partida.fecha < self.partida.fecha:
            if self.izquierdo is None:
                self.izquierdo = Nodo(nueva_partida)
            else:
                self.izquierdo.insertar(nueva_partida)
        else:
            if self.derecho is None:
                self.derecho = Nodo(nueva_partida)
            else:
                self.derecho.insertar(nueva_partida)

    def recorrido_inorden(self):
        """Recorrido inorden para mostrar el historial en orden cronológico."""
        if self.izquierdo:
            self.izquierdo.recorrido_inorden()
        print(f"Fecha: {self.partida.fecha}, Equipos: {self.partida.equipo1} vs {self.partida.equipo2}, Resultado: {self.partida.resultado}")
        if self.derecho:
            self.derecho.recorrido_inorden()

sistema = SistemaBatallas()
partida = Partida()

# Crear partidas
sistema.organizar_partida(["Jugador A", "Jugador B"], ["Jugador C", "Jugador D"])
partida.establecer_resultado()
sistema.organizar_partida(["Jugador E", "Jugador F"], ["Jugador G", "Jugador H"])

# Mostrar historial
print("Historial de partidas:")
sistema.mostrar_historial()
