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
def eliminar_duplicados(libros, tipo_lista):
    diccionario = {}

    for libro in libros:
        clave = (libro.titulo, libro.autor)
        if clave not in diccionario:
            diccionario[clave] = libro
        else:
            libro_existente = diccionario[clave]
            if libro.anio_edicion > libro_existente.anio_edicion:
                if libro_existente. prestamos_realizados <= libro. prestamos_realizados:
                    del diccionario[clave]
                    diccionario[clave] = libro
                else:
                    pass
            elif libro.anio_edicion == libro_existente.anio_edicion:
                if libro. prestamos_realizados <= libro_existente. prestamos_realizados:
                    pass
                else:
                    del diccionario[clave]
                    diccionario[clave] = libro
            else:
                pass
    
    libros_sin_duplicados = None
    if tipo_lista == "a":
        libros_sin_duplicados = ArrayOrderedPositionalList()
    elif tipo_lista == "l":
        libros_sin_duplicados = LinkedOrderedPositionalList()
    
    for libro in diccionario.values():
        libros_sin_duplicados.add(libro)
    
    return libros_sin_duplicados

# La definición de "Determinar la media de préstamos por libro que realiza el servicio de la biblioteca." está incompleta y surgen varias dudas.
# Si un libro tiene el mismo título y autor, ¿cual se debe elminar?: ¿El que tenga menos prestamos? ¿El que aparezca primero en la lista?
# Todo depende del caso, en mi caso he decido eliminar el que tenga menos prestamos, suponiendo que cuantos menos prestamos tenga más nuevo será el libro

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
