from datos import lectorCsv, actualizarPais, agregarPais, buscarPais
paises = lectorCsv("paises.csv")
opcion = 0
while opcion != 5:
    print("""\nMenu: 
        1. Agregar un pais 
        2. Actualizar pais
        3. Buscar pais 
        4. Ver paises
        5. Salir""")
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1: agregarPais (paises)
        elif opcion == 2: actualizarPais (paises)
        elif opcion == 3: buscarPais(paises)
        elif opcion == 4: print(paises)
        elif opcion == 5: 
            print("Saliendo del programa...")
            break
        else: print("Opcion no valida")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")