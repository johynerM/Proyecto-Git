from Registrar_item import cargar_datos, guardar_datos
def devolucion():
    items = cargar_datos()
    codigo = input("Ingrese el ID del producto: ").strip()
    for producto in items:
        if producto["ID"] == codigo:
            print(f"Producto encontrado: {producto['Titulo']}")
            cantidad = int(input("Ingrese cuantos productos desea devolver: "))
            if cantidad > 0:
                producto["Cantidad"] += cantidad
                guardar_datos(items)
                print("Devolucion realizada con exito")
            else:
                print("La cantidad debe ser mayor que cero")
            break
    else:

        print("Producto no encontrado")


            
