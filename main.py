from datos import lectorCsv, actualizarPais, agregarPais
from operaciones import buscarPais, filtroContinente, filtroRangoPoblacion, filtroRangoSuperficie, ordenarPaises, mostrarEstadisticas, mostrarPaises
paises = lectorCsv("paises.csv")
opcion = 0
while opcion != 10:
    print("""\nMenu: 
        1. Agregar un pais 
        2. Actualizar pais
        3. Buscar pais 
        4. Filtrar por continente
        5. Filtrar por rango de poblacion
        6. Filtrar por rango de superficie
        7. Ordenar paises
        8. Mostrar estadisticas
        9. Ver todos los paises
        10. Salir""")
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1: agregarPais (paises)
        elif opcion == 2: actualizarPais (paises)
        elif opcion == 3: buscarPais(paises)
        elif opcion == 4: filtroContinente(paises)
        elif opcion == 5: filtroRangoPoblacion(paises)
        elif opcion == 6: filtroRangoSuperficie(paises)
        elif opcion == 7: ordenarPaises(paises)
        elif opcion == 8: mostrarEstadisticas(paises)
        elif opcion == 9: mostrarPaises(paises)
        elif opcion == 10: 
            print("Saliendo del programa...")
            break
        else: print("Opcion no valida")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")