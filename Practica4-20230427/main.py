import sys
sys.path.append('/project/home/oscaryt9/workspace/Practica4-20230427/ABBs_posicionales')
from ABBs_posicionales import *
from classes import *
from funciones import *

def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
        To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1

def read_activities(path, tree):

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
    
    name, duration, participation, total_price = params[0], int(params[1]), int(params[2]), float(params[3])
    cost = total_price/participation/duration
    return Activity(name, duration, participation, total_price, cost)


# Creamos los arboles de las empresas A y B
avl_tree_1 = AVL()
# Generamos el arbol vacio A
preorder_indent_BST(avl_tree_1,avl_tree_1.root(),0)
avl_tree_2 = AVL()
# Generamos el arbol vacio B
preorder_indent_BST(avl_tree_2,avl_tree_2.root(),0)

#_____________________________________________________________________________________________________________________________________

if __name__ == "__main__":
    
    check = input("Desea añadir sus propios archivos? (si no lo hace se cargarán los archivos predeterminados)\n [y/n]: ")
    while check != "y" and check != "n":
        check = input("\033[1;31m Valor incorrecto. Por favor, elija [y/n]: \033[0m")
    print("")

    while True:
        try:
            if check =="n":
                read_activities("actividadesA.txt", avl_tree_1)
                read_activities("actividadesB.txt", avl_tree_2)
                break
            else:
                actividadesA = input("Nombre del archivo de las actividades A (archivoA.txt): ")
                # Leer las actividades del archivo A y almacenarlas en el árbol 1
                read_activities(actividadesA, avl_tree_1)

                actividadesB = input("Nomrbre del archivo de las actividades B (archivoB.txt): ")
                # Leer las actividades del archivo B y almacenarlas en el árbol 2
                read_activities(actividadesB, avl_tree_2)
                print("")
                break
        except FileNotFoundError:
            print("\033[1;31mArchivo no encontrado. Por favor, inténtelo de nuevo.\033[0m")

    # Función sumar actividades
    avl_tree_3 = add_activities(avl_tree_1,avl_tree_2)

    # Función oferta minima comun
    avl_tree_4 = offer_minim_common(avl_tree_1,avl_tree_2)

    # Imprimir todos los arboles de Actividades
    print_out = input("Elige la forma de imprimir los arboles AVL:\n 1. Como lista desplegable \n 2. Como arbol binario \n [1/2]: ")
    while print_out !="1" and print_out !="2":
        print_out = input("\033[1;31m Valor incorrecto. Por favor, elija [1/2]: \033[0m")
    print("")

    if print_out == "1":
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

    if print_out == "2":
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
     
    #__getitem__ (pej.print(tree[1]))
    #__setitem__(pej.tree[1]="A")
    #__delitem__(del tree[1])
    #__iter__(for in in s)
    #__len__(len(s))

    #Position
    #p.key(): la clave del elemento en la posicion P
    #p. value(): .....

    #coste/participante/hora
    # 100 2 3
    # 100*3/2 =16,66 euros