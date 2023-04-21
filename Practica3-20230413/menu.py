from classes import *
from array_ordered_positional_list  import *
from linked_ordered_positional_list import *
from main import *

    
# Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
def media_prestamos(libros):
    print(libros)
    print([repr(libro) for libro in libros])
    suma_prestamos = 0
    for libro in libros:
        suma_prestamos += libro.prestamos_realizados
    media = suma_prestamos/ len(libros)
    print(suma_prestamos)
    print(len(libros))
    return media

# Eliminar los libros con mismo título y autor, dejando la versión más reciente.
def eliminar_duplicados(libros):
    libro = libros.first()

    while libros.after(libro) == None:
        if libros.after(libro).get_titulo() == libro.get_titulo() and \
            libros.after(libro).get_autor() == libro.get_autor():
            libros.delete(libros.after(libro))

        else: libro = libros.after(libro)

    return libros
"""    if tipo_lista == "a":
        libros_sin_duplicados = ArrayOrderedPositionalList()
    elif tipo_lista == "l":
        libros_sin_duplicados = LinkedOrderedPositionalList()

    

    for libro in libros:
        clave = (libro.get_titulo(), libro.get_autor())
        if clave not in diccionario:
            diccionario[clave] = libro
        else:
            libro_existente = diccionario[clave]
            if libro.get_anio_edicion() == libro_existente.get_anio_edicion():
                if libro.get_prestamos_realizados() < libro_existente.get_prestamos_realizados():
                    diccionario[clave] = libro
            elif libro.get_anio_edicion() > libro_existente.get_anio_edicion():
                diccionario[clave] = libro
    
    for libro in diccionario.values():
        libros_sin_duplicados.add(libro)
    return libros_sin_duplicados
"""
    
# La definición de "Determinar la media de préstamos por libro que realiza el servicio de la biblioteca." está incompleta y surgen varias dudas.
# Si un libro tiene el mismo título y autor, ¿cual se debe elminar?: ¿El que tenga menos prestamos? ¿El que aparezca primero en la lista?
# Todo depende del caso, en mi caso he decido eliminar el que tenga menos prestamos, suponiendo que cuantos menos prestamos tenga más nuevo será el libro

def imprimir_libros(libros):
    print(f"Listado todos los libros de la biblioteca\n")

    # Obtener el tamaño máximo de cada columna
    titulo_max = max([len(libro.titulo) for libro in libros])
    autor_max = max([len(libro.autor) for libro in libros])
    anio_max = max([len(str(libro.anio_edicion)) for libro in libros])
    
    # Imprimir la cabecera de la tabla
    print(f"{'Título':<{titulo_max}} | {'Autor':<{autor_max}} | {'Año':<{anio_max}}")
    print(f"{'-' * titulo_max}-|-{'-' * autor_max}-|-{'-' * anio_max}")
    
    # Imprimir cada libro
    for libro in libros:
        print(f"{libro.titulo:<{titulo_max}} | {libro.autor:<{autor_max}} | {libro.anio_edicion:<{anio_max}}")


def imprimir_libros_por_autor(libros, autor):
    print(f"Listado de libros del autor {autor}\n")

    # Obtener el tamaño máximo de cada columna
    titulo_max = max([len(libro.titulo) for libro in libros])
    autor_max = max([len(libro.autor) for libro in libros])
    anio_max = max([len(str(libro.anio_edicion)) for libro in libros])

    # Imprimir la cabecera de la tabla
    print(f"{'Título':<{titulo_max}} | {'Autor':<{autor_max}} | {'Año':<{anio_max}}")
    print(f"{'-' * titulo_max}-|-{'-' * autor_max}-|-{'-' * anio_max}")

    # Imprimir cada libro
    for libro in libros:
        if libro.autor == autor:
            print(f"{libro.titulo:<{titulo_max}} | {libro.autor:<{autor_max}} | {libro.anio_edicion:<{anio_max}}")

# Como se puede ver se útiliza [; ] para separar los campos en la base datos por eso en la línea 19 debes debes hace el split con ; 
# libro = parse_params(linea.strip().split('; '))
# Se puede usar if libro.autor.strip() == autor.strip(): para eliminar los espacios en blanco y saltos de línea del nombre del autor en el caso de hacer el split solo con [;]

def imprimir_libros_por_anio(libros, anio_edicion):
    print(f"Listado de libros editados en el año {anio_edicion}\n")

    # Obtener el tamaño máximo de cada columna
    titulo_max = max([len(libro.titulo) for libro in libros])
    autor_max = max([len(libro.autor) for libro in libros])
    anio_max = max([len(str(libro.anio_edicion)) for libro in libros])

    # Imprimir la cabecera de la tabla
    print(f"{'Título':<{titulo_max}} | {'Autor':<{autor_max}} | {'Año':<{anio_max}}")
    print(f"{'-' * titulo_max}-|-{'-' * autor_max}-|-{'-' * anio_max}")
    
    # Imprimir cada libro
    for libro in libros:
        if libro.anio_edicion == anio_edicion:
            print(f"{libro.titulo:<{titulo_max}} | {libro.autor:<{autor_max}} | {libro.anio_edicion:<{anio_max}}")

def imprimir_libros_por_anio_autor(libros, autor, anio_edicion):
    print("")
    print(f"Listado de libros por autor y años determinados")

    # Obtener el tamaño máximo de cada columna
    titulo_max = max([len(libro.titulo) for libro in libros])
    autor_max = max([len(libro.autor) for libro in libros])
    anio_max = max([len(str(libro.anio_edicion)) for libro in libros])

    # Imprimir la cabecera de la tabla
    print(f"{'Título':<{titulo_max}} | {'Autor':<{autor_max}} | {'Año':<{anio_max}}")
    print(f"{'-' * titulo_max}-|-{'-' * autor_max}-|-{'-' * anio_max}")

    for libro in libros:
        if libro.autor == autor and libro.anio_edicion == anio_edicion:
            print(f"{libro.titulo:<{titulo_max}} | {libro.autor:<{autor_max}} | {libro.anio_edicion:<{anio_max}}")


def cambiar_tipo_lista(libros, tipo_lista):
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
