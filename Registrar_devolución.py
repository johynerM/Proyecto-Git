import json
def devolucion():
 codigo=input("Ingrese el codigo del producto: ")
 for producto in inventario:
    if producto["codigo"]==codigo:
        cantidad=int(input("ingrese la cuantos productos desea devolver: "))
        producto["cantidad"]+=cantidad
        print("Devolucion realizado con exito")
        with open("inventario.json", "w") as archivo:
            json.dump(inventario, archivo, indent=4)
        break
    else:
        print("Producto no encontrado")


            
