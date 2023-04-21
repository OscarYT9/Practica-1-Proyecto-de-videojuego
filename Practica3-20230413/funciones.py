from classes import *
from array_ordered_positional_list  import *
from linked_ordered_positional_list import *
from main import *

#________________________________________________________________________________________________________________________________    
# Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
def media_prestamos(libros):
    """
    Calcula y devuelve la media de préstamos realizados de una lista de libros.

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        Lista de libros.

    Returns
    -------
    media : float
        Media de préstamos realizados de la lista de libros.
    """
    suma_prestamos = 0
    for libro in libros:
        suma_prestamos += libro.get_prestamos_realizados()
    media = suma_prestamos/ len(libros)

    return media

def eliminar_duplicados(libros, tipo_lista):
    """
    Elimina los libros duplicados de la lista de libros, basándose en el título y autor de cada libro y manteniendo el libro con el año de edición más reciente y el número de préstamos realizado más bajo.

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        La lista de libros a eliminar duplicados.
    tipo_lista : str
        El tipo de lista actual de los libros, que debe ser "array" o "linked".

    Returns
    -------
    libros_sin_duplicados : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        La nueva lista de libros sin duplicados, en la misma ordenación que la lista original.
    """
    if tipo_lista == "a":
        libros_sin_duplicados = ArrayOrderedPositionalList()
    elif tipo_lista == "l":
        libros_sin_duplicados = LinkedOrderedPositionalList()

    diccionario = {}

    for libro in libros:
        clave = (libro.titulo, libro.autor)
        if clave not in diccionario:
            diccionario[clave] = libro
        else:
            libro_existente = diccionario[clave]
            if libro.anio_edicion == libro_existente.anio_edicion:
                if libro.prestamos_realizados < libro_existente.prestamos_realizados:
                    diccionario[clave] = libro
            elif libro.anio_edicion > libro_existente.anio_edicion:
                diccionario[clave] = libro
    
    for libro in diccionario.values():
        libros_sin_duplicados.add(libro)
    return libros_sin_duplicados


def imprimir_libros(libros):
    """
    Imprime una tabla con el listado de todos los libros de la biblioteca, mostrando el título, autor y año de edición.

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        Lista de libros ordenada.

    Returns
    -------
    None
    """
    print(f"Listado todos los libros de la biblioteca\n")

    # Obtener el tamaño máximo de cada columna
    titulo_max = max([len(libro.get_titulo()) for libro in libros])
    autor_max = max([len(libro.get_autor()) for libro in libros])
    anio_max = max([len(str(libro.get_anio_edicion())) for libro in libros])
    
    # Imprimir la cabecera de la tabla
    print(f"{'Título':<{titulo_max}} | {'Autor':<{autor_max}} | {'Año':<{anio_max}}")
    print(f"{'-' * titulo_max}-|-{'-' * autor_max}-|-{'-' * anio_max}")
    
    # Imprimir cada libro
    for libro in libros:
        print(f"{libro.get_titulo():<{titulo_max}} | {libro.get_autor():<{autor_max}} | {libro.get_anio_edicion():<{anio_max}}")


def imprimir_libros_por_autor(libros, autor):
    """
    Imprime una tabla con los libros del autor especificado.

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        Lista de libros ordenada.
    autor : str
        Nombre del autor de los libros a imprimir.

    Returns
    -------
    None
    """
    print(f"Listado de libros del autor {autor}\n")

    # Obtener el tamaño máximo de cada columna
    titulo_max = max([len(libro.get_titulo()) for libro in libros])
    autor_max = max([len(libro.get_autor()) for libro in libros])
    anio_max = max([len(str(libro.get_anio_edicion())) for libro in libros])

    # Imprimir la cabecera de la tabla
    print(f"{'Título':<{titulo_max}} | {'Autor':<{autor_max}} | {'Año':<{anio_max}}")
    print(f"{'-' * titulo_max}-|-{'-' * autor_max}-|-{'-' * anio_max}")

    # Imprimir cada libro
    for libro in libros:
        if libro.get_autor() == autor:
            print(f"{libro.get_titulo():<{titulo_max}} | {libro.get_autor():<{autor_max}} | {libro.get_anio_edicion():<{anio_max}}")

def imprimir_libros_por_anio(libros, anio_edicion):
    """
    Imprime en pantalla una lista de libros ordenada por año de edición, incluyendo sólo los libros cuyo año
    de edición es igual al especificado por el usuario.

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        La lista de libros a imprimir.
    anio_edicion : int
        El año de edición que se utilizará como filtro para la lista de libros.

    Returns
    -------
    None
    """

    print(f"Listado de libros editados en el año {anio_edicion}\n")

    # Obtener el tamaño máximo de cada columna
    titulo_max = max([len(libro.get_titulo()) for libro in libros])
    autor_max = max([len(libro.get_autor()) for libro in libros])
    anio_max = max([len(str(libro.get_anio_edicion())) for libro in libros])

    # Imprimir la cabecera de la tabla
    print(f"{'Título':<{titulo_max}} | {'Autor':<{autor_max}} | {'Año':<{anio_max}}")
    print(f"{'-' * titulo_max}-|-{'-' * autor_max}-|-{'-' * anio_max}")
    
    # Imprimir cada libro
    for libro in libros:
        if libro.get_anio_edicion() == anio_edicion:
            print(f"{libro.get_titulo():<{titulo_max}} | {libro.get_autor():<{autor_max}} | {libro.get_anio_edicion():<{anio_max}}")

def imprimir_libros_por_anio_autor(libros, autor, anio_edicion):
    """
    Imprime en pantalla una lista de libros ordenada por año de edición, incluyendo sólo los libros cuyo año
    de edición es igual al especificado por el usuario y cuyo autor es igual al especificado por el usuario.

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        La lista de libros a imprimir.
    autor : str
        El nombre del autor que se utilizará como filtro para la lista de libros.
    anio_edicion : int
        El año de edición que se utilizará como filtro para la lista de libros.

    Returns
    -------
    None
    """
    print("")
    print(f"Listado de libros por autor y años determinados")

    # Obtener el tamaño máximo de cada columna
    titulo_max = max([len(libro.get_titulo()) for libro in libros])
    autor_max = max([len(libro.get_autor()) for libro in libros])
    anio_max = max([len(str(libro.get_anio_edicion())) for libro in libros])

    # Imprimir la cabecera de la tabla
    print(f"{'Título':<{titulo_max}} | {'Autor':<{autor_max}} | {'Año':<{anio_max}}")
    print(f"{'-' * titulo_max}-|-{'-' * autor_max}-|-{'-' * anio_max}")

    for libro in libros:
        if libro.get_autor() == autor and libro.get_anio_edicion() == anio_edicion:
            print(f"{libro.get_titulo():<{titulo_max}} | {libro.get_autor():<{autor_max}} | {libro.get_anio_edicion():<{anio_max}}")


def cambiar_tipo_lista(libros, tipo_lista):
    """
    Cambia el tipo de lista utilizada para almacenar los libros, pidiendo al usuario que elija entre "array" o "linked".

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        La lista de libros a convertir.
    tipo_lista : str
        El tipo de lista actual de los libros, que debe ser "array" o "linked".

    Returns
    -------
    nueva_lista : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        La nueva lista de libros convertida al tipo especificado por el usuario.
    tipo_lista : str
        El nuevo tipo de lista de los libros, que es "array" o "linked".
    """
    while True:
        tipo_lista = input("\t¿Que tipo de lista quieres, array o linked? [a/l]: ")
        if tipo_lista == "a":
            nueva_lista = ArrayOrderedPositionalList()
            for libro in libros:
                nueva_lista.add(libro)
            return nueva_lista, tipo_lista  # Retorna la nueva lista

        elif tipo_lista == "l":
            nueva_lista = LinkedOrderedPositionalList()
            for libro in libros:
                nueva_lista.add(libro)
            return nueva_lista, tipo_lista  # Retorna la nueva lista

        else:
            print("\t\033[1;31mOpción inválida. Por favor, selecciona [a/l].\033[0m")
#_______________________________________________________________________________________________________________________________________

# Función para imprimir el menú
def imprimir_menu():
    print("\n")
    print("                | - MENÚ PRINCIPAL - |                  ")
    print("--------------------------------------------------------")
    print("| Selecciona una opción:                               |")
    print("|                                                      |")
    print("| 1. Leer libros desde un archivo                      |")
    print("| 2. Determinar la media de préstamos por libro        |")
    print("| 3. Eliminar libros duplicados                        |")
    print("| 4. Visualizar listado de libros                      |")
    print("| 5. Salir                                             |")
    print("| 6. Configuración                                     |")
    print("|                                                      |")
    print("|------------------------------------------------------|\n")

# Función para imprimir el submenú
def imprimir_submenu():
    print("\n")
    print("\t              | - LISTADO DE LIBROS - |               ")
    print("\t------------------------------------------------------")
    print("\t| Selecciona una opción:                              |")
    print("\t|                                                     |")
    print("\t| 1. Listar todos los libros                          |")
    print("\t| 2. Listar libros de un autor determinado            |")
    print("\t| 3. Listar libros de un año determinado              |")
    print("\t| 4. Listar libros por autor y año determinado        |")
    print("\t| 5. Cancelar y volver al menú principal              |")
    print("\t| 6. Salir                                            |")
    print("\t|                                                     |")
    print("\t|-----------------------------------------------------|\n")

