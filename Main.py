#LINEA PRINCIPAL VISUALIZACION USER

print("========================================")
print("Bienvenido a la Biblioteca Comunitaria Horizonte ")
print("========================================")
while True:
    print("========================================")
    print("1. Registrar ítem\n2. Listar ítems\n3. Buscar ítem\n4. Registrar préstamo\n5. Registrar Devolucion\n6.Salir")
    opcion = int(input("Ingresa la opción que deseas ejecutar: "))
    if opcion == 1:
        from Registrar_item import registro
        registro()
    elif opcion == 2:
        from Listar_item import listar
        listar()
    elif opcion == 3:
        from Buscar_item import buscar
        buscar()
    elif opcion == 4:
        from Registar_prestamo import prestamo
        prestamo()
    elif opcion == 5:
        from Registrar_devolución import devolucion
        devolucion()
    elif opcion==6:
        print("Buen dia, gracias por visitarnos😁")
        break