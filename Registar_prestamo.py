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


