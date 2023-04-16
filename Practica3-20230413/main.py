import sys
from classes import *
from array_ordered_positional_list  import *
from linked_ordered_positional_list import *

# Crear una lista vacía para almacenar los libros
libros = ArrayOrderedPositionalList()




def run(path):
    """
    Ejecuta la simulación de combate entre los personajes leídos desde el archivo especificado.
    
    Parameters
    ----------
    path : str
        ruta del archivo que contiene los parámetros de los personajes
    
    Returns
    -------    
    None
    """

    with open(path, 'r') as archivo:
        # Abrir el archivo de texto y leer cada línea
        lineas = archivo.readlines()
        # Iterar sobre las líneas del archivo y agregar cada libro a la lista
        for linea in lineas:
            # Dividir la línea en tres partes: título, autor y año de edición
            libro = parse_params(linea.strip().split(';'))
            # Agregar el libro a la lista, ordenando por autor, título y año de edición
            libros.add(libro)

    def leer_libros(path):

        with open(path, 'r') as archivo:
            # Abrir el archivo de texto y leer cada línea
            lineas = archivo.readlines()
            # Iterar sobre las líneas del archivo y agregar cada libro a la lista
            for linea in lineas:
                # Dividir la línea en tres partes: título, autor y año de edición
                libro = parse_params(linea.strip().split(';'))
                # Agregar el libro a la lista, ordenando por autor, título y año de edición
                libros.add(libro)
        return libros
    #TODO: Implement simulation here
    
    # Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
    def media_prestamos(libros):

        sum=0
        for libro in libros:
            libro.prestamos_realizados+= sum
        media = sum/len(libros)
        return media

    # Eliminar los libros con mismo título y autor, dejando la versión más reciente.
    
    def eliminar_duplicados(libros):
        libros_sin_duplicados = ArrayOrderedPositionalList()
        diccionario = {}

        for libro in libros:
            clave = (libro.titulo, libro.autor)
            if clave not in diccionario:
                diccionario[clave] = libro
            else:
                libro_existente = diccionario[clave]
                if libro.fecha_publicacion > libro_existente.fecha_publicacion:
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
            if libro.autor == autor:
                print(f"{libro.titulo}\t{libro.autor}\t{libro.anio_edicion}")

    def imprimir_libros_por_anio(libros, anio):
        print(f"Listado de libros editados en el año {anio}")
        print("Título\tAutor\tAño Edición")
        print("--------------------------------------------------")
        for libro in libros:
            if libro.anio == anio:
                print(f"{libro.titulo}\t{libro.autor}\t{libro.anio_edicion}")
   

    # Menú principal del programa
    while True:
        print("¿Qué quieres hacer?")
        print("1. Leer libros desde un archivo")
        print("2. Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.")
        print("3. Eliminar los libros con mismo título y autor, dejando la versión más reciente.")
        print("4. Visualizar en pantalla un listado tabulado de todos los libros de la biblioteca, o de los escritos por  un autor o los editados en un año determinado por el usuario. Si hay varias copias y/o ediciones de un libro, se incluyen todas en el listado.")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            # Pedir al usuario que ingrese la ubicación del archivo
            path = input("Ingrese la ubicación del archivo: ")
            # Leer libros desde el archivo y almacenarlos en una lista
            print(leer_libros(path))
            print("Libros leídos correctamente.")
            
        elif opcion == "2":
            # Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
            print(media_prestamos(libros))

        elif opcion == "3":
            # Eliminar los libros con mismo título y autor, dejando la versión más reciente.
            print(eliminar_duplicados(libros))

        elif opcion == "4":
            print("")
            while True:
                print("1. Un listado tabulado de todos los libros de la biblioteca")
                print("2. Un listado tabulado de todos los libros escritos por un autor")
                print("3. Un listado tabulado de todos los libros editados en un año determinado")
                print("4. Cancelar y volver al menú principal")
                x = input("¿Qué deseas visualizar por pantalla?")
                if x == "1":
                    imprimir_libros(libros)

                elif x == "2":
                    autor = input("¿De qué autor deseas visualizar los libros?: ")
                    imprimir_libros_por_autor(libros, autor)

                elif x == "3":
                    anio = input("¿De qué año deseas visualizar los libros?: ")
                    imprimir_libros_por_anio(libros, anio)

                elif x == "4":
                    # Salir al menú principal
                    print("")
                    break
                
                else:
                    print("")
                    print("Opción inválida. Por favor, selecciona una opción válida.")

        elif opcion == "5":
            # Salir del programa
            break
        else:
            # Opción inválida, mostrar mensaje de error
            print("")
            print("Opción inválida. Por favor, selecciona una opción válida.")



    
def parse_params(params):
    
    titulo, nombre, anio_edicion, prestamos_realizados = params[0], params[1], int(params[2]), int(params[3])
    return Libro(titulo, nombre, anio_edicion, prestamos_realizados)

if __name__ == "__main__":
    run(sys.argv[1])