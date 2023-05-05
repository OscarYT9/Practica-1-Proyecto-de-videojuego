import os
import sys

# Obtener la ruta del archivo actual
current_dir = os.path.dirname(os.path.abspath(__file__))

# Agregar el directorio que contiene los módulos al sys.path
module_dir = os.path.join(current_dir, "ABBs_posicionales")
sys.path.append(module_dir)

from ABBs_posicionales.avl_tree import *
from classes import *
from funciones import *
#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


def read_activities(path, tree):
    """
    Lee el archivo de texto en la ruta especificada y agrega cada actividad al árbol binario.

    Parameters
    ----------
    path : str
        La ruta del archivo de texto que contiene las actividades.
    tree : BinarySearchTree
        El árbol binario en el que se agregarán las actividades.

    Returns
    -------
    None
    """

    with open(path) as archive:
        # Abrir el archivo de texto y leer cada línea
        lines = archive.readlines()
        # Iterar sobre las líneas del archivo y agregar cada actividad al arbol
        for line in range(1, len(lines)):
            # Dividir la línea en tres partes: título, autor y año de edición
            activity = parse_params(lines[line].strip().split(';'))
            # Agregar el libro a la lista, ordenando por autor, título y año de edición
            tree[activity.get_name()] = activity

#TODO: Implement simulation here

def parse_params(params):
    """
    Parsea los parámetros de una actividad y calcula el costo por participante.

    Parameters
    ----------
    params : List[str]
        Una lista que contiene los parámetros de una actividad en el siguiente orden:
        [nombre, duración, participantes, precio_total].

    Returns
    -------
    Activity
        Una instancia de la clase Activity que representa la actividad parseada,
        incluyendo el costo por participante.
    """
    
    name, duration, participation, total_price_activity = params[0], int(params[1]), int(params[2]), float(params[3])
    cost_per_participate = total_price_activity/participation/duration
    return Activity(name, duration, participation, total_price_activity, cost_per_participate)


# Creamos los arboles de las empresas A y B
avl_tree_1 = AVL()
avl_tree_2 = AVL()

#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

if __name__ == "__main__":
    # Preguntamos al usuario si quiere añadir sus propios archivos
    check = input("Desea añadir sus propios archivos? (si no lo hace se cargarán los archivos predeterminados)\n [y/n]: ")
    while check != "y" and check != "n":
        check = input("\033[1;31m Valor incorrecto. Por favor, elija [y/n]: \033[0m")
    print("")

    # Leemos las actividades A , B y las volcamos en los arboles correspondientes
    while True:
        try:
            if check =="n":
                read_activities("actividadesA.txt", avl_tree_1)
                read_activities("actividadesB.txt", avl_tree_2)
                break
            else:
                activitiesA = input("Nombre del archivo de las actividades A (archivoA.txt): ")
                # Leer las actividades del archivo A y almacenarlas en el árbol 1
                read_activities(activitiesA, avl_tree_1)

                activitiesB = input("Nomrbre del archivo de las actividades B (archivoB.txt): ")
                # Leer las actividades del archivo B y almacenarlas en el árbol 2
                read_activities(activitiesB, avl_tree_2)
                print("")
                break
        except FileNotFoundError:
            print("\033[1;31mArchivo no encontrado. Por favor, inténtelo de nuevo.\033[0m")

    # Función sumar actividades y oferta mínima comun
    avl_tree_3, avl_tree_4 = operations(avl_tree_1,avl_tree_2)


    # Imprimir todos los arboles de Actividades
    print_out = input("Elige la forma de imprimir los arboles AVL:\n 1. Con la función preorder_indent_BST \n 2. Como lista desplegable \n 3. Como arbol binario \n [1/2/3]: ")
    while print_out !="1" and print_out !="2" and print_out !="3":
        print_out = input("\033[1;31m Valor incorrecto. Por favor, elija [1/2/3]: \033[0m")
    print("")

    if print_out == "1":
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades empresa A")
        preorder_indent_BST(avl_tree_1,avl_tree_1.root(),0)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades empresa B")
        preorder_indent_BST(avl_tree_2,avl_tree_2.root(),0)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Suma de Actividades A+B (manteniendo la de menor coste)")
        preorder_indent_BST(avl_tree_3,avl_tree_3.root(),0)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades comunes (manteniendo la de menor coste)")
        preorder_indent_BST(avl_tree_4,avl_tree_4.root(),0)

    if print_out == "2":
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades empresa A")
        print_tree(avl_tree_1)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades empresa B")
        print_tree(avl_tree_2)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Suma de Actividades A+B (manteniendo la de menor coste)")
        print_tree(avl_tree_3)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades comunes (manteniendo la de menor coste)")
        print_tree(avl_tree_4)

    if print_out == "3":
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades empresa A")
        print_tree2(avl_tree_1)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades empresa B")
        print_tree2(avl_tree_2)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Suma de Actividades A+B (manteniendo la de menor coste)")
        print_tree2(avl_tree_3)
        print("___________________________________________________________________________________________________________________________________________________")
        print("Actividades comunes (manteniendo la de menor coste)")
        print_tree2(avl_tree_4)


    print("___________________________________________________________________________________________________________________________________________________")
     
    