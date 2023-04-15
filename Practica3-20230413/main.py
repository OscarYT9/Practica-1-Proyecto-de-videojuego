import sys
from classes import *
from array_ordered_positional_list  import *
from linked_ordered_positional_list import *

# Crear una lista vacía para almacenar los libros
lista_libros = ArrayOrderedPositionalList()




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
            lista_libros.add(libro)

    #TODO: Implement simulation here
    # Determinar la media de préstamos por libro que realiza el servicio de la biblioteca. 
        sum=0
        for libro in lista_libros:
            libro.prestamos_realizados+= sum
        media = sum/len(lista_libros)
        print(media)

    # Eliminar los libros con mismo título y autor, dejando la versión más reciente.
        for libro in lista_libros:
            if libro[2] and libro[3]:
                lista_libros.get_element()
    

























    
def parse_params(params):
    
    titulo, nombre, anio_edicion, prestamos_realizados = params[0], params[1], int(params[2]), int(params[3])
    return Libro(titulo, nombre, anio_edicion, prestamos_realizados)

if __name__ == "__main__":
    run(sys.argv[1])