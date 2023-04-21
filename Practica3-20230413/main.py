import sys
from classes import *
from array_ordered_positional_list  import *
from linked_ordered_positional_list import *
from funciones import *


def leer_libros(path, tipo_lista):
    """
    Lee los libros desde un archivo de texto y los agrega a una lista ordenada.

    Parameters
    ----------
    path : str
        La ruta al archivo de texto que contiene la información de los libros.
    tipo_lista : str
        El tipo de lista ordenada que se utilizará para almacenar los libros. Debe ser "a" para
        ArrayOrderedPositionalList o "l" para LinkedOrderedPositionalList.

    Returns
    -------
    lista_ordenada : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        La lista ordenada que contiene los libros leídos del archivo de texto.
    """

    if tipo_lista == "a":
        libros = ArrayOrderedPositionalList()

    elif tipo_lista == "l":
        libros = LinkedOrderedPositionalList()

    with open(path) as archivo:
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

def parse_params(params):
    """
    Convierte una lista de parámetros en un objeto de tipo Libro.

    Parameters
    ----------
    params : list
        Una lista con cuatro elementos que representan los parámetros de un libro. Los elementos son:
        - título (str)
        - autor (str)
        - año de edición (int)
        - número de préstamos realizados (int)

    Returns
    -------
    Libro
        Un objeto de tipo Libro con los parámetros especificados en la lista.

    """
    titulo, autor, anio_edicion, prestamos_realizados = params[0], params[1], int(params[2]), int(params[3])
    return Libro(titulo, autor, anio_edicion, prestamos_realizados)

#_______________________________________________________________________________________________________________
def opcion_cuatro():
    """
    Ofrece opciones para visualizar los libros y ejecuta la opción seleccionada por el usuario.

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        Lista de libros ordenada.
    tipo_lista : str
        Tipo de lista utilizada para ordenar los libros.

    Returns
    -------
    None
    """
    opciones = {
        '1. Todos los libros': lambda: imprimir_libros(libros),
        '2. Libros de un autor': lambda: imprimir_libros_por_autor(libros, input("¿De qué autor deseas visualizar los libros? (Apellido, Nombre): ")),
        '3. Libros de un año de edición': lambda: imprimir_libros_por_anio(libros, int(input("¿De qué año deseas visualizar los libros?: ")) ),
        '4. Listar libros por autor y año': lambda: imprimir_libros_por_anio_autor(libros, input("¿De qué autor deseas visualizar los libros? (Apellido, Nombre): "), int(input("¿De qué año deseas visualizar los libros?: "))),
        '5. Volver al menú principal': lambda: None,
    }
    questions = [        {            'type': 'list',            'name': 'opcion',            'message': '¿Qué deseas visualizar por pantalla?',            'choices': [                '1. Todos los libros',                '2. Libros de un autor',                '3. Libros de un año de edición',       '4. Listar libros por autor y año',               Separator(),                '5. Volver al menú principal'            ]
        }
    ]
    answer = prompt(questions, style=style)
    seleccion = answer['opcion']
    funcion_seleccionada = opciones[seleccion]
    funcion_seleccionada()
    print("")
    
#_______________________________________________________________________________________________________________
def configuracion(libros, tipo_lista):
    """
    Ofrece opciones de configuración y ejecuta la opción seleccionada por el usuario.

    Parameters
    ----------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        Lista de libros ordenada.
    tipo_lista : str
        Tipo de lista utilizada para ordenar los libros.

    Returns
    -------
    libros : ArrayOrderedPositionalList o LinkedOrderedPositionalList
        Lista de libros ordenada.
    tipo_lista : str
        Tipo de lista utilizada para ordenar los libros.
    """
    questions = [
        {
            'type': 'list',
            'name': 'opcion',
            'message': 'Selecciona una opción:',
            'choices': [
                '1. Cambiar tipo de lista de libros',
                Separator(),
                '2. Volver al menú principal'
            ]
        }
    ]
    answer = prompt(questions, style=style)
    seleccion = answer['opcion']
    print(seleccion)
    if seleccion == '1. Cambiar tipo de lista de libros':
        libros, tipo_lista = cambiar_tipo_lista(libros, tipo_lista)
        return libros, tipo_lista
    else:
        None

#_______________________________________________________________________________________________________________

if __name__ == "__main__":
    

#--------------------------------------------------------------------------------------------------------------

    
    print("\033[31m      _____  _____   _____   ______  ______ _____  _____\033[0m")
    print("\033[33m|       |   |_____] |_____/ |______ |_____/   |   |_____|\033[33m")
    print("\033[31m|____ __|__ |_____] |    \_ |______ |    \_ __|__ |     |\033[0m")
    
    print("\033[31m|              .--.                   .---.             |\033[0m")
    print("\033[31m|          .---|__|           .-.     |~~~|             |\033[0m")
    print("\033[33m|       .--|===|--|_          |_|     |~~~|--.          |\033[0m")
    print("\033[33m|       |  |===|  |'\     .---!~|  .--| P |--|          |\033[0m")
    print("\033[33m|       |%%| I |  |.'\    |===| |--|%%| . |  |          |\033[0m")
    print("\033[33m|       |%%| A |  |\.'\   | P | |__|  | 3 |  |          |\033[0m")
    print("\033[33m|       |  | | |  | \  \  |===| |==|  | . |  |          |\033[0m")
    print("\033[33m|       |  | | |__|  \.'\ | 2 |_|__|  |~~~|__|          |\033[0m")
    print("\033[31m|       |  |===|--|   \.'\|===|~|--|%%|~~~|--|          |\033[0m")
    print("\033[31m|       ^--^---'--^    `-'`---^-^--^--^---'--'          |\033[0m") 
    print("---------------------------------------------------------")
    print("| \033[1m¡Recuerda que puedes cambiar la base de datos de los libros con la opción número 1! (de normal se carga el archivo libros.txt)\033[0m")
    print("| \033[1m(De forma predeterminada se usa array_ordered_positional_list para almacenar los libros para cambiar su comportamiento ir a Configuración)\033[0m")
    print("|")
    print("| \x1b[1;30mHan sido implementados 2 menús, ahora debes decidir el Menú que deseas usar [1/2]\033[0m")
    print("| \x1b[1;30mEl Menú 1 está implementado solo en Python mientras que el 2 utiliza la librería de PyInquirer por lo que deberá tenerla instalada:\033[0m")
    print("| ")

    while True:
        menu = input("Menú seleccionado [1/2]: ")
        if menu=="1" or menu=="2":
            break
        else:
            # Opción inválida, mostrar mensaje de error
            print("")
            print("\033[1;31mOpción inválida. Por favor, selecciona el Menú 1 o 2.\033[0m")

    # Crear una lista vacía para almacenar los libros y definir el tipo de lista
    libros = ArrayOrderedPositionalList()
    libros_sin_duplicados = ArrayOrderedPositionalList()
    tipo_lista = "a"
    path = "libros.txt"

    libros= leer_libros(path, tipo_lista)
    print(libros)
    print("\n")
    

    # Menú principal del programa 1
    if menu == "1":
        while True:
            imprimir_menu()
            opcion = input("Opción seleccionada: ")
            
            if opcion == "1":
                while True:
                    try:
                        path = input("Ingrese el nombre del archivo con su respectiva extensión (recuerda que la ubicación de la base de datos debe estár en el mismo directorio que el programa principal): ")
                        # Leer libros desde el archivo y almacenarlos en una lista

                        libros = leer_libros(path, tipo_lista)
                        print("Libros leídos correctamente.")
                        break # salir del bucle while si no hay excepciones
                    except FileNotFoundError:
                        print("\033[1;31mArchivo no encontrado. Por favor, inténtelo de nuevo.\033[0m")

                
            elif opcion == "2":
                # Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
                print("Media: ",media_prestamos(libros))

            elif opcion == "3":
                # Eliminar los libros con mismo título y autor, dejando la versión más reciente.
                libros = eliminar_duplicados(libros, tipo_lista)
                print("Libros duplicados elminados correctamente.")
                

            elif opcion == "4":
                while True:
                    imprimir_submenu()
                    x = input("¿Qué deseas visualizar por pantalla?: ")
                    print("")
                    if x == "1":
                        imprimir_libros(libros)

                    elif x == "2":
                        autor = input("¿De qué autor deseas visualizar los libros? (Apellido, Nombre): ")
                        print("")
                        imprimir_libros_por_autor(libros, autor)

                    elif x == "3":
                        anio_edicion = int(input("¿De qué año deseas visualizar los libros?: "))
                        print("")
                        imprimir_libros_por_anio(libros, anio_edicion)
                    
                    elif x == "4":
                        autor = input("¿De qué autor deseas visualizar los libros? (Apellido, Nombre): ")
                        anio_edicion = int(input("¿De qué año deseas visualizar los libros?: "))
                        imprimir_libros_por_anio_autor(libros, autor, anio_edicion)
                        print("")                             

                    elif x == "5":
                        # Salir al menú principal
                        print("")
                        break
                    
                    elif x == "6":
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
                libros, tipo_lista = cambiar_tipo_lista(libros, tipo_lista)

            else:
                # Opción inválida, mostrar mensaje de error
                print("")
                print("\033[1;31mOpción inválida. Por favor, selecciona una opción válida.\033[0m")




    # Menú principal del programa 2
    elif menu == "2":
        print("\033[1;31m¡IMPORTANTE!: Muevete con las flechas de dirección y selecciona una opción con ENTER\033[0m")
        print("\033[1;31mde lo contrario el Menú podría dar errores (no afecta a los resultados obtenidos)\033[0m")
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
                    {'name': '1. Cargar base de datos de libros'},
                    {'name': '2. Determinar media de préstamos por libro'},
                    {'name': '3. Eliminar duplicados'},
                    {'name': '4. Visualizar libros'},
                    {'name': '5. Salir'},
                    {'name': '6. Configuración'},
                    Separator('-----------------------')
                ]
            }
        ]

        while True:
            try:
                # Mostrar el menú y obtener la opción seleccionada
                respuesta = prompt(questions, style=style)
                opcion_seleccionada = respuesta['opcion']

                # Salir del programa si el usuario selecciona la opción "Salir"

                if opcion_seleccionada == "1. Cargar base de datos de libros":
                    # Pedir al usuario que ingrese la ubicación del archivo
                    while True:
                        try:
                            path = input("Ingrese el nombre del archivo con su respectiva extensión (recuerda que la ubicación de la base de datos debe estár en el mismo directorio que el programa principal): ")
                            # Leer libros desde el archivo y almacenarlos en una lista

                            libros = leer_libros(path, tipo_lista)
                            print("Libros leídos correctamente.")
                            break # salir del bucle while si no hay excepciones
                        except FileNotFoundError:
                            print("\033[1;31mArchivo no encontrado. Por favor, inténtelo de nuevo.\033[0m")


                elif opcion_seleccionada == "2. Determinar media de préstamos por libro":
                    # Determinar la media de préstamos por libro que realiza el servicio de la biblioteca.
                    print("Media: ",media_prestamos(libros))
                    
                elif opcion_seleccionada == "3. Eliminar duplicados":
                    libros = eliminar_duplicados(libros, tipo_lista)
                    print("Libros duplicados elminados correctamente.")

                elif opcion_seleccionada == "4. Visualizar libros":
                    opcion_cuatro()

                elif opcion_seleccionada == "5. Salir":
                    print("¡Hasta luego!")
                    break

                elif respuesta['opcion'] == '6. Configuración':
                    libros, tipo_lista = configuracion(libros, tipo_lista)
            
            # El modulo da error si interactuas con las opciones o el separador con el raton (devuelve un diccionario vacio).
            # https://github.com/CITGuru/PyInquirer/issues/57
            
            except KeyError:
                print("\033[1;31m¡Usa solo las flechas de dirección!\033[0m")
            except TypeError as e:
                error_msg = str(e)
                if 'w keys)' in error_msg:
                    error_msg = error_msg.split('w keys)')[0] + '!'
                continue
