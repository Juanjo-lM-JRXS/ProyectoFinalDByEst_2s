def menu_principal():
    while True:
        print("\n*************************** Menú Principal ***************************")
        print("1) Gestión de Jugadores")
        print("2) Gestión de Mapas")
        print("3) Gestión de Inventarios")
        print("4) Sistema de Batallas y Partidas")
        print("5) Ranking Global")
        print("6) Equipos y Estadísticas")
        print("7) Consultas y Análisis")
        print("8) Salir")
        opcion = input("Ingrese una opción válida: ")

        if opcion == "1":
            gestion_jugadores()
        elif opcion == "2":
            gestion_mapas()
        elif opcion == "3":
            gestion_inventarios()
        elif opcion == "8":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestion_jugadores():
    jugadores = {}
    while True:
        print("\n*************************** Gestión de Jugadores ***************************")
        print("1) Registrar nuevo jugador")
        print("2) Modificar datos de jugador")
        print("3) Eliminar jugador")
        print("4) Consultar datos de jugador")
        print("5) Regresar al menú principal")
        opcion = input("Ingrese una opción válida: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre de usuario: ")
            nivel = input("Ingrese el nivel inicial (Ej: 1-10): ")
            puntuacion = input("Ingrese la puntuación inicial: ")
            equipo = input("Ingrese el equipo del jugador: ")
            jugadores[nombre] = {"nivel": nivel, "puntuacion": puntuacion, "equipo": equipo, "inventario": []}
            print(f"Jugador '{nombre}' registrado con éxito.")
        elif opcion == "4":
            nombre = input("Ingrese el nombre de usuario a consultar: ")
            if nombre in jugadores:
                print("\n------------------------------------")
                print(f"Usuario: {nombre}")
                print(f"Nivel: {jugadores[nombre]['nivel']}")
                print(f"Puntuación: {jugadores[nombre]['puntuacion']}")
                print(f"Equipo: {jugadores[nombre]['equipo']}")
                print(f"Inventario: {', '.join(jugadores[nombre]['inventario']) if jugadores[nombre]['inventario'] else 'Vacío'}")
                print("------------------------------------")
            else:
                print("Jugador no encontrado.")
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestion_mapas():
    mapas = {
        "Mapa Urbano": ["Centro Comercial", "Callejón", "Azotea"],
        "Zona Desértica": ["Campamento", "Cañón", "Punto de Control"]
    }
    while True:
        print("\n*************************** Gestión de Mapas ***************************")
        print("1) Ver mapas disponibles")
        print("2) Consultar ubicaciones en un mapa")
        print("3) Agregar conexión entre ubicaciones")
        print("4) Regresar al menú principal")
        opcion = input("Ingrese una opción válida: ")

        if opcion == "1":
            print("Mapas disponibles:")
            for mapa in mapas.keys():
                print(f"- {mapa}")
        elif opcion == "2":
            mapa = input("Ingrese el nombre del mapa: ")
            if mapa in mapas:
                print(f"Ubicaciones en {mapa}: {', '.join(mapas[mapa])}")
            else:
                print("Mapa no encontrado.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

def gestion_inventarios():
    inventarios = {}
    while True:
        print("\n*************************** Gestión de Inventarios ***************************")
        print("1) Añadir arma al inventario")
        print("2) Eliminar arma del inventario")
        print("3) Consultar inventario de un jugador")
        print("4) Regresar al menú principal")
        opcion = input("Ingrese una opción válida: ")

        if opcion == "1":
            jugador = input("Ingrese el nombre del jugador: ")
            if jugador not in inventarios:
                inventarios[jugador] = []
            arma = input("Ingrese el nombre del arma: ")
            inventarios[jugador].append(arma)
            print(f"Arma '{arma}' añadida al inventario de '{jugador}'.")
        elif opcion == "3":
            jugador = input("Ingrese el nombre del jugador: ")
            if jugador in inventarios:
                print("\n------------------------------------")
                print(f"Inventario de {jugador}:")
                for i, arma in enumerate(inventarios[jugador], start=1):
                    print(f"{i}) {arma}")
                print("------------------------------------")
            else:
                print("Jugador no encontrado o inventario vacío.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Iniciar el programa
menu_principal()
