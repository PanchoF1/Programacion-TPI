def buscarPais(paises):
    buscarPais = input("Ingrese el nombre del pais a consultar: ")
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
        if buscarPais in pais["nombre"]: 
            print(f"""Los datos de {buscarPais} son: 
                Poblacion: {pais["poblacion"]} 
                Superficie: {pais["superficie"]} 
                Continente: {pais["continente"]} """)
            encontrado = True
    if not encontrado:
        print("Pais no encontrado")
    return

def filtroContinente(paises):
    buscarContinente = input("Ingrese el nombre del continente a consultar: ")
    buscarContinente = buscarContinente.title()
    buscarContinente = buscarContinente.strip()
    if buscarContinente == "":
        print("El nombre del continente no puede estar vacio")
        return
    elif len(paises) == 0:
        print("Archivo vacio")
        return
    encontrado = False
    for pais in paises:
        if buscarContinente in pais["continente"]:
            if not encontrado:
                print(f"el continente {buscarContinente} se encuentra en los paises:")
            encontrado = True
            print(f"""Pais: {pais["nombre"]}
                Poblacion: {pais["poblacion"]} 
                Superficie: {pais["superficie"]} 
                Continente: {pais["continente"]}""")
    if not encontrado:
        print("Continente no encontrado")
    return

def filtroRangoPoblacion(paises):
    pass

def filtroRangoSuperficie(paises):
    pass

def ordenarPaises(paises):
    pass

def mostrarEstadisticas(paises):
    pass

def mostrarPaises(paises):
    pass