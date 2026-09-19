def devolucion():
codigo=input("Ingrese el codigo del producto: ")
for producto in productos:
    if producto["codigo"]==codigo:
        cantidad=int(input("ingrese la cuantos productos desea devolver: "))
        producto["cantidad"]+=cantidad
        print("Devolucion realizado con exito")
    else:
        print("Producto no encontrado")

            
