#----------------------------------------------------------------------------------------------------------------------
import json
#----------------------------------------------------------------------------------------------------------------------
#Guardar en una variable el nombre del archivo del inventario
Ruta_datos_inventario = "inventario.json"

#Aqui se van a guardar todos lo prestamos
Ruta_datos_prestamos = "prestamos.json"
#----------------------------------------------------------------------------------------------------------------------
#Funcion para cargar los datos del inventario
def cargar_datos(ruta):
    try:
        with open(ruta, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
#----------------------------------------------------------------------------------------------------------------------
#Funcion para guardar los datos en el archivo json indicado en 'ruta' 
def guardar_datos(ruta, datos):
    with open(ruta, "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
#----------------------------------------------------------------------------------------------------------------------
#Funcion para registrar los prestamos que se hagan en la biblioteca
def prestamo():
    inventario = cargar_datos(Ruta_datos_inventario)  #Cargamos el inventario para verificar que el libro exista
    prestamos = cargar_datos(Ruta_datos_prestamos)     #Cargamos los prestamos ya registrados

    print("===== Registrar Prestamo =====")

    if not inventario:
        print("La Biblioteca esta vacia, no hay libros para prestar")
        return

    ID_libro = input("Ingrese el ID del libro a prestar: ").strip()

    #Comparacion EXACTA 
    libro_encontrado = None
    for item in inventario:
        if item.get("ID") == ID_libro:
            libro_encontrado = item
            break

    if libro_encontrado is None:
        print("❌ERROR, NO EXISTE UN LIBRO CON ESE ID EXACTO❌")
        return  #Cortamos la funcion aqui, no seguimos pidiendo mas datos

    if libro_encontrado.get("Cantidad", 0) <= 0:
        print("❌No hay ejemplares disponibles de este libro❌")
        return

    #El titulo lo tomamos del inventario, no se le vuelve a preguntar al usuario
    titulo_libro = libro_encontrado.get("Titulo")

    usuario = input("Ingrese el nombre del usuario que solicita el prestamo: ").strip()
    fecha = input("Ingrese la fecha del prestamo (DD/MM/AAAA): ").strip()

    if not usuario or not fecha:
        print("❌ERROR, DEBE INGRESAR USUARIO Y FECHA❌")
        return

    Nuevo_prestamo = {
        "ID": ID_libro,
        "Titulo": titulo_libro,
        "Usuario": usuario,
        "Fecha": fecha
    }

    prestamos.append(Nuevo_prestamo)
    libro_encontrado["Cantidad"] -= 1  #Restamos un ejemplar disponible en el inventario

    guardar_datos(Ruta_datos_prestamos, prestamos)
    guardar_datos(Ruta_datos_inventario, inventario)

    print(f"✅ Prestamo registrado: '{titulo_libro}' (ID: {ID_libro}) a nombre de {usuario}")
#----------------------------------------------------------------------------------------------------------------------


