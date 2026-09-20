import json
Ruta_datos = "inventario.json"
def cargar_datos(): #Leemos el archivo json
    try:
        with open(Ruta_datos,"r",encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return[]
def buscar(): #Comenzamos la funcionalidad de buscar
    inventario = cargar_datos()
    print("===== Buscar Libros en la Biblioteca =====")
    if not inventario:
        print("La Biblioteca esta vacia")
        return
    print("1. Buscar por ID\n2. Buscar por Titulo\n3. Buscar por categoria")
    opcion=input("Ingrese la opcion deseada: ")
    resultados=[]
    if opcion == "1":
        modo = input("Ingrese el ID del libro: ")
        resultados = [item for item in inventario if str(item.get("ID")) == modo] #Hacemos compresion de listas para recorrer y guardar dependiendo la condicion 
    elif opcion == "2":
        modo = input("Ingrese el Titulo del libro: ")
        resultados= [item for item in inventario if modo in str(item.get("Titulo" ,""))]
    elif opcion == "3":
        modo = input("Ingresa la categoria: ")
        resultados = [item for item in inventario if modo in str(item.het("Categoria",""))]
    else:
        print("Opcion no valida")
        return
    if resultados:
        print(f"encontramos {len(resultados)} resultados: ") #Un pequeño resumen de lo que encontramos en la busquedad
        for item in resultados:
            print(f"ID: {item.get("ID")} | Titulo: {item.get("Titulo")} | Autor: {item.get("Autor")}")
    else:
        print("No se encontraron ninguno")    
        