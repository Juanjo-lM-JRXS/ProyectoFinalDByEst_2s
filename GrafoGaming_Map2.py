
class Graph:

    def __init__(self):
        self.graph = {}

    def add_edge(self,nodo,arista):
        if nodo not in self.graph:
            self.graph[nodo] =[]
        if arista not in self.graph:
            self.graph[arista] = []
        
        if arista not in self.graph[nodo]:
            self.graph[nodo].append(arista)
        if nodo not in self.graph[arista]:
            self.graph[arista].append(nodo)
    
    def get_connections(self,nodo):
        return self.graph.get(nodo,[])
    
    def up_edge(self,nodo,old_arista,new_arista):
        if nodo in self.graph and old_arista in self.graph[nodo]:
            self.graph[nodo].remove(old_arista)
            self.graph[nodo].append(new_arista)

    def delete_nodo(self,nodo):
        if nodo in self.graph:
            del self.graph[nodo]
            for connections in self.graph.values():
                if nodo in connections:
                    connections.remove(nodo)
    
    def get_allConnections(self):
        return self.graph

G = Graph()

G.add_edge("Team","LD")
G.add_edge("Team","C")
G.add_edge("Team","LI")
G.add_edge("Team","CA")

print("todas las rutas", G.get_allConnections())
print("")
print("la ruta lateral izquierda : ordinaria & ¡Peligrosa!", G.get_connections("LI"))
print("")
print("la ruta Central : Efectiva y ¡Peligrosa!",G.get_connections("C"))
print("")
print("la ruta lateral Derecha : ordinaria, Segura & poco efectiva", G.get_connections("LD"))
print("")
print("la ruta lateral Central Arriba : Efectiva, +Rango, -Movimiento", G.get_connections("CA"))