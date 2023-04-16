import sys
from classes import *
from array_ordered_positional_list  import *
from linked_ordered_positional_list import *

# Crear una lista vacía para almacenar los libros
libros = ArrayOrderedPositionalList()



def leer_libros(path):

    with open(path, 'r') as archivo:
        # Abrir el archivo de texto y leer cada línea
        lineas = archivo.readlines()
        # Iterar sobre las líneas del archivo y agregar cada libro a la lista
        for linea in lineas:
            # Dividir la línea en tres partes: título, autor y año de edición
            libro = parse_params(linea.split('; '))
            # Agregar el libro a la lista, ordenando por autor, título y año de edición
            libros.add(libro)
    return libros
#TODO: Implement simulation here

# Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
def media_prestamos(libros):
    suma_prestamos = 0
    for libro in libros:
        suma_prestamos += libro.prestamos_realizados
    media = suma_prestamos / len(libros)
    return media

# Eliminar los libros con mismo título y autor, dejando la versión más reciente.
libros_sin_duplicados = ArrayOrderedPositionalList()
def eliminar_duplicados(libros):
    diccionario = {}

    for libro in libros:
        clave = (libro.titulo, libro.autor)
        if clave not in diccionario:
            diccionario[clave] = libro
        else:
            libro_existente = diccionario[clave]
            if libro.anio_edicion > libro_existente.anio_edicion:
                diccionario[clave] = libro
    
    for libro in diccionario.values():
        libros_sin_duplicados.add(libro)
    return libros_sin_duplicados

def imprimir_libros(libros):
    print("Título\tAutor\tAño Edición")
    print("--------------------------------------------------")
    for libro in libros:
        print(f"{libro.titulo}\t{libro.autor}\t{libro.anio_edicion}")

def imprimir_libros_por_autor(libros, autor):
    print(f"Listado de libros del autor {autor}")
    print("Título\tAutor\tAño Edición")
    print("--------------------------------------------------")
    for libro in libros:
        if libro.autor == autor:                                            # Se puede usar if libro.autor.strip() == autor.strip(): para eliminar los espacios en blanco y saltos de línea del nombre del autor en el caso de hacer el split solo con [;]
            print(f"{libro.titulo}\t{libro.autor}\t{libro.anio_edicion}")   # Como se puede ver se útiliza [; ] para separar los campos en la base datos por eso en la línea 19 debes debes hace el split con ; 
                                                                            # libro = parse_params(linea.strip().split('; '))

def imprimir_libros_por_anio(libros, anio_edicion):
    print(f"Listado de libros editados en el año {anio_edicion}")
    print("Título\tAutor\tAño Edición")
    print("--------------------------------------------------")
    for libro in libros:
        if libro.anio_edicion == anio_edicion:
            print(f"{libro.titulo}\t{libro.autor}\t{libro.anio_edicion}")




    
def parse_params(params):
    
    titulo, autor, anio_edicion, prestamos_realizados = params[0], params[1], int(params[2]), int(params[3])
    return Libro(titulo, autor, anio_edicion, prestamos_realizados)


if __name__ == "__main__":
    # Menú principal del programa
    print("\n-----------------------")
    print("| Biblioteca XYZ |")
    print("-----------------------\n")
    print("\033[1m¡Recuerda que antes de nada debes cargar la base de datos de los libros con la opción número 1! (de normal se carga el archivo libros.txt)\n\033[0m")
    path = "libros.txt"
    print(leer_libros(path))
    print("\n")

    while True:
        print("Selecciona una opción:\n")
        print("1. Leer libros desde un archivo")
        print("2. Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.")
        print("3. Eliminar los libros con mismo título y autor, dejando la versión más reciente.")
        print("4. Visualizar en pantalla un listado tabulado de todos los libros de la biblioteca, o de los escritos por un autor o los editados en un año determinado por el usuario. Si hay varias copias y/o ediciones de un libro, se incluyen todas en el listado.")
        print("5. Salir")
        print("6. Configuración")
        opcion = input("Opción seleccionada: ")
        
        if opcion == "1":
            # Pedir al usuario que ingrese la ubicación del archivo
            path = input("Ingrese el nombre del archivo (recuerda que la ubicación de la base de datos debe estár en el mismo directorio que el programa principal): ")
            # Leer libros desde el archivo y almacenarlos en una lista
            if tipo_lista == "a":
                libros = ArrayOrderedPositionalList()

            elif tipo_lista == "l":
                libros = LinkedOrderedPositionalList()
                
            print(leer_libros(path))
            print([repr(libro) for libro in libros]) # print(list(libros))
            print("Libros leídos correctamente.")
            
        elif opcion == "2":
            # Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
            print(media_prestamos(libros))

        elif opcion == "3":
            # Eliminar los libros con mismo título y autor, dejando la versión más reciente.
            print(eliminar_duplicados(libros))
            print([repr(libro) for libro in libros_sin_duplicados])
            libros = libros_sin_duplicados  # Cambia la lista de libros original por la que no tiene duplicados

        elif opcion == "4":
            print("")
            while True:
                print("\t1. Un listado tabulado de todos los libros de la biblioteca")
                print("\t2. Un listado tabulado de todos los libros escritos por un autor")
                print("\t3. Un listado tabulado de todos los libros editados en un año determinado")
                print("\t4. Cancelar y volver al menú principal")
                print("\t5. Salir\n")
                x = input("¿Qué deseas visualizar por pantalla?: ")
                if x == "1":
                    imprimir_libros(libros)

                elif x == "2":
                    autor = input("¿De qué autor deseas visualizar los libros?: ")
                    imprimir_libros_por_autor(libros, autor)

                elif x == "3":
                    anio_edicion = int(input("¿De qué año deseas visualizar los libros?: "))
                    imprimir_libros_por_anio(libros, anio_edicion)

                elif x == "4":
                    # Salir al menú principal
                    print("")
                    break
                
                elif x == "5":
                    # Salir al menú principal
                    print("")
                    sys.exit()

                else:
                    print("")
                    print("\t\033[1;31mOpción inválida. Por favor, selecciona una opción válida.\033[0m")

        elif opcion == "5":
            # Salir del programa
            break

        elif opcion == "6":
            while True:
                cambiar = input("\t¿Quieres cambiar el tipo de lista con en el que se almacenan los libros? (De forma predeterminada se ejecutará con array_ordered_positional_list) [y/n]: ")
                if cambiar == "y":
                    tipo_lista = input("\t¿Que tipo de lista quieres, array o linked? [a/l]: ")
                    if tipo_lista == "a":
                        temp = []
                        for libro in libros:
                            temp.append(libro)
                        nueva_lista = ArrayOrderedPositionalList()
                        for libro in temp:
                            nueva_lista.add(libro)
                        libros = nueva_lista
                        break
                    elif tipo_lista == "l":
                        temp = []
                        for libro in libros:
                            temp.append(libro)
                        nueva_lista = LinkedOrderedPositionalList()
                        for libro in temp:
                            nueva_lista.add(libro)
                        break
                        libros = nueva_lista
                elif cambiar == "n":
                    break
                else:
                    print("\t\033[1;31mOpción inválida. Por favor, selecciona [y/n].\033[0m")


        else:
            # Opción inválida, mostrar mensaje de error
            print("")
            print("\033[1;31mOpción inválida. Por favor, selecciona una opción válida.\033[0m")


