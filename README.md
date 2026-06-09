# Gestión de Datos de Países en Python

## Descripción
Trabajo Integrador de Programacion 1. Simulador de gestion de datos de paises con python, utilizando un csv para guardar los paises y poder ordenar, filtrar, añadir y actualizar los paises.
## Requisitos
Tener Visual Studio Code u otro editor de texto y tener python instalado en su ultima version
## Instrucciones de uso
1. Clonar el repositorio: git clone https://github.com/PanchoF1/Programacion-TPI
2. Entrar a la carpeta: cd Programacion-TPI
3. Ejecutar: python main.py
4. Menu en la terminal
## Funcionalidades
Sus funcionalidades son: Añadir pais, Actualizar datos (poblacion y superficie) del pais, filtrar los paises por continente, superficie y poblacion, mostrar los paises ordenandolos de ascendencia o descendencia ya sea por orden alfabeto, poblacion o superficie y mostrarlos por como estan ordenados en el archivo csv
## Ejemplos de uso
### Agregar un país
1. Ingrese nombre del pais
2. Ingrese su poblacion
3. Ingrese su superficie
4. Ingrese su continente
5. Se agrega al archivo csv y a la lista de diccionarios
### Buscar un país
1. Ingrese el nombre del pais a buscar
2. Busca pais por nombre o abreviado (argentina o arg)
3. Mostrar pais con datos
### Filtrar por continente
1. Ingrese que continente desea buscar
2. Busca continente por nombre o abreviado (america o am)
3. Mostrar Paises con datos que sean del continente buscado
### Ordenar países
1. Ingresar si ordenar por nombre, poblacion o superficie
2. Ingresar si mostrar de nombre ascendente o descendente
3. Mostrar los paises con datos con el orden ingresado
### Estadísticas
1. Muestra las siguientes estadisticas:
• Pais con MAYOR poblacion
• Pais con MENOR poblacion
• Promedio de poblacion
• Promedio de superficie
• Cantidad de paises por continente:

## Integrantes
- Francisco Adams
- Uriel Alvarez Rey
### Participación
Uriel:
- Crear el CSV con el dataset base (minimo 10 paises)
- Funcion que lee el CSV y devuelve la lista de diccionarios
- Funcion para agregar un pais (con validaciones, sin campos vacios)
- Funcion para actualizar poblacion y superficie
- Funcion para buscar por nombre (parcial y exacta)
- Menu principal en main.py con todas las opciones armadas

Francisco:
- Filtros por continente, rango de poblacion, rango de superficie
- Ordenamientos por nombre, poblacion, superficie (asc/desc)
- Estadisticas completas
- Validaciones de los filtros

## Links