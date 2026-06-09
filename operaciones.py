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
    if len(paises) == 0:
        print("Archivo vacío")
        return
    try:
        min_pob = int(input("Ingrese la poblacion minima: "))
        max_pob = int(input("Ingrese la poblacion maxima: "))
        if min_pob < 0 or max_pob < 0:
            print("Error: Los rangos de poblacion no pueden ser negativos.")
            return
        if min_pob > max_pob:
            print("Error: La poblacion minima no puede ser mayor que la maxima.")
            return
        encontrado = False
        for pais in paises:
            if min_pob <= pais["poblacion"] <= max_pob:
                if not encontrado:
                    print(f"\nPaises con poblacion entre {min_pob:,} y {max_pob:,} habitantes:")
                encontrado = True
                print(f"""Pais: {pais["nombre"]}
                Poblacion: {pais["poblacion"]} 
                Superficie: {pais["superficie"]} 
                Continente: {pais["continente"]}""")
        if not encontrado:
            print("No se encontraron paises en ese rango de poblacion.")
    except ValueError:
        print("Error: Debe ingresar valores numericos enteros validos.")

def filtroRangoSuperficie(paises):
    if len(paises) == 0:
        print("Archivo vacío")
        return
    try:
        min_sup = int(input("Ingrese la superficie minima (km²): "))
        max_sup = int(input("Ingrese la superficie maxima (km²): "))
        if min_sup < 0 or max_sup < 0:
            print("Error: Los rangos de superficie no pueden ser negativos.")
            return
        if min_sup > max_sup:
            print("Error: La superficie minima no puede ser mayor que la maxima.")
            return
        encontrado = False
        for pais in paises:
            if min_sup <= pais["superficie"] <= max_sup:
                if not encontrado:
                    print(f"\nPaíses con superficie entre {min_sup:,} y {max_sup:,} km²:")
                encontrado = True
                print(f"""Pais: {pais["nombre"]}
                Poblacion: {pais["poblacion"]} 
                Superficie: {pais["superficie"]} 
                Continente: {pais["continente"]}""")
        if not encontrado:
            print("No se encontraron paises en ese rango de superficie.")
    except ValueError:
        print("Error: Debe ingresar valores numericos enteros validos.")

def ordenarPaises(paises):
    if len(paises) == 0:
        print("Archivo vacio")
        return
    print("\nCriterios de ordenamiento:")
    print("1. Nombre")
    print("2. Poblacion")
    print("3. Superficie")
    try:
        opc_criterio = int(input("Seleccione un criterio (1-3): "))
        if opc_criterio == 1:
            criterio = "nombre"
        elif opc_criterio == 2:
            criterio = "poblacion"
        elif opc_criterio == 3:
            criterio = "superficie"
        else:
            print("Opción de criterio inválida.")
            return
        print("\nSentido de ordenamiento:")
        print("1. Ascendente")
        print("2. Descendente")
        opc_sentido = int(input("Seleccione el sentido (1-2): "))        
        if opc_sentido == 1:
            ascendente = True
        elif opc_sentido == 2:
            ascendente = False
        else:
            print("Opcion de sentido invalida.")
            return
        if criterio == "nombre":
            paises_ordenados = sorted(paises, key=lambda x: x["nombre"].lower(), reverse=not ascendente)
        else:
            paises_ordenados = sorted(paises, key=lambda x: x[criterio], reverse=not ascendente)
        print(f"\n--- Lista de Paises Ordenados por {criterio.title()} ---")
        for pais in paises_ordenados:
            print(f"País: {pais['nombre']} | Población: {pais['poblacion']:,} | Superficie: {pais['superficie']:,} km² | Continente: {pais['continente']}")
    except ValueError:
        print("Error: Debe ingresar opciones numericas validas.")

def mostrarEstadisticas(paises):
    if len(paises) == 0:
        print("Archivo vacio. No se pueden calcular estadisticas.")
        return
    pais_mayor_pob = paises[0]
    pais_menor_pob = paises[0]    
    suma_poblacion = 0
    suma_superficie = 0
    conteo_continentes = {}
    for pais in paises:
        if pais["poblacion"] > pais_mayor_pob["poblacion"]:
            pais_mayor_pob = pais
        if pais["poblacion"] < pais_menor_pob["poblacion"]:
            pais_menor_pob = pais
        suma_poblacion += pais["poblacion"]
        suma_superficie += pais["superficie"]
        cont = pais["continente"].strip().title()
        if cont in conteo_continentes:
            conteo_continentes[cont] += 1
        else:
            conteo_continentes[cont] = 1
    total_paises = len(paises)
    promedio_pob = suma_poblacion / total_paises
    promedio_sup = suma_superficie / total_paises
    print("\n" + "="*45)
    print("         REPORTE ESTADÍSTICO INTEGRAL        ")
    print("="*45)
    print(f"• Pais con MAYOR poblacion: {pais_mayor_pob['nombre']} ({pais_mayor_pob['poblacion']:,} hab.)")
    print(f"• Pais con MENOR poblacion: {pais_menor_pob['nombre']} ({pais_menor_pob['poblacion']:,} hab.)")
    print(f"• Promedio de poblacion:    {promedio_pob:,.2f} hab.")
    print(f"• Promedio de superficie:   {promedio_sup:,.2f} km²")
    print("-"*45)
    print("• Cantidad de paises por continente:")
    for continente, cantidad in conteo_continentes.items():
        print(f"  - {continente}: {cantidad} pais(es)")
    print("="*45)

def mostrarPaises(paises):
    if len(paises) == 0:
        print("No hay paises cargados.")
        return
    print("\n--- Todos los Paises Registrados ---")
    for pais in paises:
        print(f"• {pais['nombre']} (Pob: {pais['poblacion']:,} | Sup: {pais['superficie']:,} km² | Cont: {pais['continente']})")