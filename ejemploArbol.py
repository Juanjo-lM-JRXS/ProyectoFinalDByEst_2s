class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # Insertar un nodo en el árbol
    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierdo is None:
                nodo.izquierdo = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierdo, valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecho, valor)

    # Recorrido en orden
    def recorrido_inorden(self, nodo=None):
        if nodo is None:
            nodo = self.raiz

        if nodo.izquierdo:
            self.recorrido_inorden(nodo.izquierdo)
        print(nodo.valor, end=' ')
        if nodo.derecho:
            self.recorrido_inorden(nodo.derecho)

# Ejemplo de uso
arbol = ArbolBinario()
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(3)
arbol.insertar(7)

print("Recorrido en orden:")
arbol.recorrido_inorden()
