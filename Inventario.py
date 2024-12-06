inventario = {}

def agregarProducto(id, nombre, cantidad, precio):
    
    if id in inventario:
      print(f"el producto con id {id} ya existe")
    else:
      inventario[id] = {
          
          'nombre' : nombre,
          'cantidad' : cantidad,
          'precio' : precio
      }

      print(f"el producto {nombre} ha sido agregado correctamente")

def consultar_producto(id):
   if id in inventario:
      producto = inventario[id]
      print(f"ID: {id}, nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio: {producto['precio']}")
   else:
      print(f"el producto con id {id} no existe en el inventario") 


def actualizar_producto(id, nueva_cantidad, nuevo_precio):
   if id in inventario:
      inventario[id]['cantidad'] = nueva_cantidad
      inventario[id]['precio'] = nuevo_precio
      print(f"producto con id {id} fue actualizado correctamente") 
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
         print(f" id: {id} nombre: {producto['nombre']}, Cantidad: {producto['cantidad']}, Precio{producto['precio']}")
   else:
      print("el inventario esta vacio")