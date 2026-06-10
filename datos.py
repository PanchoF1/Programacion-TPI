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

def guardarCsv (paises, ruta_archivo):
    try:
        with open (ruta_archivo, "w", encoding="utf8") as archivo:
            campos = ["nombre", "poblacion", "superficie", "continente"]
            escritor = csv.DictWriter(archivo, fieldnames=campos)
            escritor.writeheader()
            for pais in paises:
                escritor.writerow(pais)
    except FileNotFoundError:
        print(f"Error: El archivo {ruta_archivo} no se encontro")
    except KeyError:
        print("Error: Revise los encabezados")
    except Exception as e:
        print(f"Ocurrio un error inesperado: {e}")

def agregarPais (paises):
    nuevopais = input("Ingrese el nombre del pais: ")
    nuevopais = nuevopais.title().strip()
    if nuevopais == "":
        print ("El nombre del pais no puede estar vacio")
        return
    for pais in paises:
        if pais["nombre"].title().strip() == nuevopais:
            print ("El pais ya esta ingresado")
            return
    try:
        poblacion = int(input(f"Ingrese la poblacion de {nuevopais}: "))
        superficie = int(input(f"Ingrese la superficie de {nuevopais}: "))
        continente = input(f"Ingrese el continente de {nuevopais}: ")
        continente = continente.title().strip()
        if poblacion < 0 or superficie < 0:
            raise ValueError("Los valores no pueden ser negativos")
        if continente == "":
            print ("El nombre del continente no puede estar vacio")
            return
        else:
            pais = {"nombre": nuevopais, "poblacion": poblacion, "superficie": superficie, "continente": continente}
            paises.append(pais)
            guardarCsv (paises, ruta_archivo)
            print(f"El pais {nuevopais} fue agregado correctamente")
    except ValueError as e:
        print(e)
        return

def actualizarPais (paises):
    try:
        try:
            buscarPais = input("Ingrese el nombre del pais a modificar: ")
            buscarPais = buscarPais.title()
            buscarPais = buscarPais.strip()
            if buscarPais == "":
                print("El nombre del pais no puede estar vacio")
                return
            elif len(paises) == 0:
                print("Archivo vacio")
                return
            encontrado = False
            for pais in paises:
                if pais["nombre"].title().strip() == buscarPais:
                    try:
                        poblacion = int(input(f"Ingrese la poblacion de {buscarPais}: "))
                        superficie = int(input(f"Ingrese la superficie de {buscarPais}: "))
                        if poblacion < 0 or superficie < 0:
                            raise ValueError("Los valores no pueden ser negativos")
                        pais["poblacion"] = poblacion
                        pais["superficie"] = superficie
                        guardarCsv (paises, ruta_archivo)
                        print("Nuevos valores cargados")
                        encontrado = True
                    except ValueError as e:
                        print(e)
                        return
            if not encontrado:
                print("Pais no encontrado")
                return
        except ValueError as e:
            print(e)
            return
    except Exception as e:
        print(e)