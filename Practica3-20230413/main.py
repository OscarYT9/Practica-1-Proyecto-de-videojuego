import sys
from classes import *
from array_ordered_positional_list  import *
from linked_ordered_positional_list import *



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

# Función para imprimir el menú
def imprimir_menu():
    print("\n--------------------------------------------------------")
    print("|                MENÚ PRINCIPAL                        |")
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
    print("\n\t---------------------------------------------------------------")
    print("\t|                LISTADO DE LIBROS                            |")
    print("\t---------------------------------------------------------------")
    print("\t| Selecciona una opción:                                      |")
    print("\t|                                                             |")
    print("\t| 1. Listar todos los libros                                  |")
    print("\t| 2. Listar libros de un autor determinado (Apellido, Nombre) |")
    print("\t| 3. Listar libros de un año determinado                      |")
    print("\t| 4. Cancelar y volver al menú principal                      |")
    print("\t| 5. Salir                                                    |")
    print("\t|                                                             |")
    print("\t|-------------------------------------------------------------|\n")

    
def parse_params(params):
    
    titulo, autor, anio_edicion, prestamos_realizados = params[0], params[1], int(params[2]), int(params[3])
    return Libro(titulo, autor, anio_edicion, prestamos_realizados)


if __name__ == "__main__":

        
    # Crear una lista vacía para almacenar los libros
    libros = ArrayOrderedPositionalList()
    libros_sin_duplicados = ArrayOrderedPositionalList()
    tipo_lista = "a"
    path = "libros.txt"
    libros=leer_libros(path)

    from PyInquirer import prompt, Separator
    from pprint import pprint
    
    # Funciones
    def cargar_base_de_datos():
        # Código para cargar la base de datos de libros
        while True:
            try:
                path = input("Ingrese el nombre del archivo con su respectiva extensión (recuerda que la ubicación de la base de datos debe estár en el mismo directorio que el programa principal): ")
                # Leer libros desde el archivo y almacenarlos en una lista
                if tipo_lista == "a":
                    libros = ArrayOrderedPositionalList()

                elif tipo_lista == "l":
                    libros = LinkedOrderedPositionalList()

                print(leer_libros(path))
                print([repr(libro) for libro in libros]) # print(list(libros))
                print("Libros leídos correctamente.")
                break # salir del bucle while si no hay excepciones
            except FileNotFoundError:
                print("\033[1;31mArchivo no encontrado. Por favor, inténtelo de nuevo.\033[0m")

    def eliminar_duplicados():
            if tipo_lista == "a":
                libros_sin_duplicados = ArrayOrderedPositionalList()

            elif tipo_lista == "l":
                libros_sin_duplicados = LinkedOrderedPositionalList()
        
            # Eliminar los libros con mismo título y autor, dejando la versión más reciente.
            print(eliminar_duplicados(libros))
            libros = libros_sin_duplicados               # Cambia la lista de libros original por la que no tiene duplicados
            print([repr(libro) for libro in libros])     ### EL ERROR CREO QUE ES CULPA DE ESTA LISTA (SE AGREGAN MAS ELEMENTOS CUANTO MAS LO EJECUTES)

    # Función que define las opciones del menú
    def opcion_cuatro():
        opciones = {
            '1. Todos los libros': imprimir_libros,
            '2. Libros de un autor': lambda: imprimir_libros_por_autor(libros, input("¿De qué autor deseas visualizar los libros?: ")),
            '3. Libros de un año de edición': lambda: imprimir_libros_por_anio(libros, int(input("¿De qué año deseas visualizar los libros?: ")) ),
            '4. Volver al menú principal': lambda: None,
        }
        questions = [        {            'type': 'list',            'name': 'opcion',            'message': '¿Qué deseas visualizar por pantalla?',            'choices': [                '1. Todos los libros',                '2. Libros de un autor',                '3. Libros de un año de edición',                Separator(),                '4. Volver al menú principal'            ]
            }
        ]
        answer = prompt(questions, style=style)
        seleccion = answer['opcion']
        funcion_seleccionada = opciones[seleccion]
        funcion_seleccionada()

    from PyInquirer import prompt, style_from_dict, Token, Separator

    # Define el estilo de la interfaz de usuario
    style = style_from_dict({
        Token.Separator: '#6C6C6C',
        Token.QuestionMark: '#FF9D00 bold',
        Token.Selected: '#5F819D',
        Token.Pointer: '#FF9D00 bold',
        Token.Instruction: '',  # sin color - por defecto
        Token.Answer: '#5F819D bold',
        Token.Question: '',
    })
    # Preguntas para el menú
    questions = [
        {
            'type': 'list',
            'name': 'opcion',
            'message': 'Selecciona una opción:',
            'choices': [
                Separator('--- Opciones del programa ---'),
                {
                    'name': '1. Cargar base de datos de libros',
                    'value': cargar_base_de_datos
                },
                {
                    'name': '2. Determinar media de préstamos por libro',
                    'value': media_prestamos(libros)
                },
                {
                    'name': '3. Eliminar duplicados',
                    'value': eliminar_duplicados
                },
                {
                    'name': '4. Visualizar libros',
                    'value': opcion_cuatro
                },
                {
                    'name': '5. Salir',
                    'value': 'Salir'
                },
                Separator('-----------------------')
            ]
        }
    ]

    while True:
        # Mostrar el menú y obtener la opción seleccionada
        respuesta = prompt(questions, style=style)
        opcion_seleccionada = respuesta['opcion']

        # Salir del programa si el usuario selecciona la opción "Salir"
        if opcion_seleccionada == "Salir":
            print("¡Hasta luego!")
            break
        elif opcion_seleccionada == cargar_base_de_datos:
            cargar_base_de_datos()

        elif opcion_seleccionada == media_prestamos(libros):
            print(media_prestamos(libros))
            
        elif opcion_seleccionada == eliminar_duplicados:
            eliminar_duplicados()

        elif opcion_seleccionada == opcion_cuatro:
            opcion_cuatro()
        

    #--------------------------------------------------------------------------------------------------------------

    # Menú principal del programa 2
    print("\n-----------------------")
    print("| Biblioteca XYZ      |")
    print("-----------------------\n")
    print("\033[1m¡Recuerda que antes de nada debes cargar la base de datos de los libros con la opción número 1! (de normal se carga el archivo libros.txt)\033[0m")
    print("\033[1m(De forma predeterminada se usa array_ordered_positional_list para almacenar los libros para cambiar su comportamiento ir a Configuración)\n\033[0m")
    
    # Crear una lista vacía para almacenar los libros
    libros = ArrayOrderedPositionalList()
    libros_sin_duplicados = ArrayOrderedPositionalList()
    tipo_lista = "a"
    path = "libros.txt"

    print(leer_libros(path))
    print("\n")
    
    while True:
        imprimir_menu()
        opcion = input("Opción seleccionada: ")
        
        if opcion == "1":
            # Pedir al usuario que ingrese la ubicación del archivo
            while True:
                try:
                    path = input("Ingrese el nombre del archivo con su respectiva extensión (recuerda que la ubicación de la base de datos debe estár en el mismo directorio que el programa principal): ")
                    # Leer libros desde el archivo y almacenarlos en una lista
                    if tipo_lista == "a":
                        libros = ArrayOrderedPositionalList()

                    elif tipo_lista == "l":
                        libros = LinkedOrderedPositionalList()

                    print(leer_libros(path))
                    print([repr(libro) for libro in libros]) # print(list(libros))
                    print("Libros leídos correctamente.")
                    break # salir del bucle while si no hay excepciones
                except FileNotFoundError:
                    print("\033[1;31mArchivo no encontrado. Por favor, inténtelo de nuevo.\033[0m")
            
        elif opcion == "2":
            # Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
            print(media_prestamos(libros))

        elif opcion == "3":
            if tipo_lista == "a":
                libros_sin_duplicados = ArrayOrderedPositionalList()

            elif tipo_lista == "l":
                libros_sin_duplicados = LinkedOrderedPositionalList()
        
            # Eliminar los libros con mismo título y autor, dejando la versión más reciente.
            print(eliminar_duplicados(libros))
            libros = libros_sin_duplicados               # Cambia la lista de libros original por la que no tiene duplicados
            print([repr(libro) for libro in libros])     ### EL ERROR CREO QUE ES CULPA DE ESTA LISTA (SE AGREGAN MAS ELEMENTOS CUANTO MAS LO EJECUTES)
            

        elif opcion == "4":
            while True:
                imprimir_submenu()
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

                        nueva_lista = ArrayOrderedPositionalList()
                        for libro in libros:
                            nueva_lista.add(libro)
                        libros = nueva_lista
                        break

                    elif tipo_lista == "l":

                        nueva_lista = LinkedOrderedPositionalList()
                        for libro in libros:
                            nueva_lista.add(libro)
                        libros = nueva_lista
                        break
                    
                elif cambiar == "n":
                    break
                else:
                    print("\t\033[1;31mOpción inválida. Por favor, selecciona [y/n].\033[0m")


        else:
            # Opción inválida, mostrar mensaje de error
            print("")
            print("\033[1;31mOpción inválida. Por favor, selecciona una opción válida.\033[0m")


# EL PROGRAMA TIENE UN ERROR, si le das a Configuración (cambias a linked)> Eliminar libros duplicados >Determinar media de préstamos por libro comprobarás que da 8.375 cuando debería dar 8.5