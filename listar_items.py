import json

ruta_datos = "inventario.json"

def cargar_datos():
    try:
        with open(ruta_datos, "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def listar():
    inventario = cargar_datos()
    print("\n=======Lista de items de inventario=======")

    if not inventario:
        print("La bibliotace no tiene items regigstrados")
        return

    for item in inventario:
      print(f"ID: {item.get('ID', 'N/A')} | "
              f"Título: {item.get('Titulo', 'N/A')} | "
              f"Autor: {item.get('Autor', 'N/A')} | "
              f"Categoría: {item.get('Categoria', 'N/A')} | "
              f"Cantidad: {item.get('Cantidad', 0)} | "
              f"Ubicación: {item.get('Ubicacion', 'N/A')}")
    print("==============================================================")