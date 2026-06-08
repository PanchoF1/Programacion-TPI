import csv
ruta_archivo = "paises.csv"
def lectorCsv (ruta_archivo):
    try:
        with open (ruta_archivo, "r", encoding="utf8") as archivo:
            lector = csv.DictReader(archivo)
            paises = []
            for fila in lector:
                pais = {"nombre": fila["nombre"], "poblacion": int(fila["poblacion"]), "superficie": int(fila["superficie"]), "continente": fila["continente"]}
                paises.append(pais)
        return paises
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no se encontro")
    except KeyError:
        print("Error: Revise los encabezados")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")