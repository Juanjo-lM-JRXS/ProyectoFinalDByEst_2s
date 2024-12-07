

inventario = {}

def agregarProducto(id, nombre, cantidad):
    
    if id in inventario:
      print(f"el producto con id {id} ya existe")
    else:
      inventario[id] = {
          
          'nombre' : nombre,
          'cantidad' : cantidad,
    
      }

      print(f"el producto {nombre} ha sido agregado correctamente")

def consultar_producto(id):
   if id in inventario:
      producto = inventario[id]
      print(f"ID: {id}, nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
   else:
      print(f"el producto con id {id} no existe en el inventario") 


def actualizar_producto(id, nueva_cantidad):
   if id in inventario:
      inventario[id]['cantidad'] = nueva_cantidad
      print(f"producto con id {id} fue actualizado correctamente con la nueva cantidad {nueva_cantidad}") 
   else:
      print(f"el producto con id {id} no existe en el inventario")
      
    
def eliminar_producto(id):
   if id in inventario:
      del inventario[id]
      print(f"producto con id {id} eliminado correctamente")
   else:
      print(f"el producto con id {id} no existe en el inventario")


def listar_producto():
   if inventario:
      for id, producto in inventario.items():
         print(f" id: {id} nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}")
   else:
      print("el inventario esta vacio")

print("")
agregarProducto("MZ01","Rifle de Asalto", 1)
print("")
agregarProducto("ME401","Escopeta", 2)
print("")
consultar_producto("ME401")
print("")
consultar_producto("MZ01")
print("")
actualizar_producto("MZ01",11)
print("")
eliminar_producto("MZ01")
print("")
listar_producto()

