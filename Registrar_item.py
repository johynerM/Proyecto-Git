import json
Ruta_datos = "inventario.json" #Le asignamos una variable al archivo json
def cargar_datos():
    try:
        with open(Ruta_datos, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def guardar_datos(datos):
    with open(Ruta_datos,"w", encoding="utf-8") as archivo:
        json.dump(datos,archivo, indent=4, ensure_ascii=False)
def registro():
        items= cargar_datos() #Revisamos si hay un json antes y lo leemos
        nombre_libro=input("Ingrese el Titulo del producto que desea registrar: ").strip()
        ID_libro = input("Ingres el codigo del libro: ").strip()
        if not ID_libro: #Con esto le damos un ID unico para que no se repita nunca ni halla errores
            ID_libro = str(len(items)+1)
        else:
            if any(item.get("ID") == ID_libro for item in items):
                print("❌ERROR, YA HAY UN LIBRO CON ESTE ID❌")
        autor= input("Ingresa el nombre del autor del libro: ").strip()
        categoria = input("Ingresa de que categoria es el libro: ").strip()
        cant= int(input("Ingresa la cantidad de libros que deses registrar: "))
        ubicacion=input("En que estanteria se encuentra: ").strip()
        Nuevo_item = {
            "ID": ID_libro,
            "Titulo": nombre_libro,
            "Autor": autor,
            "Categoria": categoria,
            "Cantidad": cant,
            "Ubicacion": ubicacion
        }
        items.append(Nuevo_item)
        guardar_datos(items) # Escribimos el nuevo registro en el json
        print(f"el libro {nombre_libro} fue registrado correctamente con el ID {ID_libro}")