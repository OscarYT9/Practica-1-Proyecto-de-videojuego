import sys
sys.path.append('/project/home/oscaryt9/workspace/Practica4-20230427/ABBs_posicionales')
from ABBs_posicionales.avl_tree import *
from classes import *


#Función eliminar duplicados y dejar la actividad con menor coste
#Función sumar actividades
#Recorre el arbol(A) y el arbol(B) y devuelve las actividades que al menos esten en una de las empresas, llama a la funcion eliminar duplicados y almacena las actividades resultantes en un arbol C
def add_activities(avl_tree_1, avl_tree_2):
    avl_tree_3 = offer_minim_common(avl_tree_1, avl_tree_2)

    for activity in avl_tree_1:
        if activity not in avl_tree_3:
            avl_tree_3[activity] = avl_tree_1[activity]

    for activity in avl_tree_2:
        if activity not in avl_tree_3:
            avl_tree_3[activity] = avl_tree_2[activity]

    return avl_tree_3

#Función oferta mínima común
#Recorre el arbol(A) y el arbol(B) y devuelve las actividades que esten en ambas empresas y llama a la funcion eliminar duplicados y almacena las actividades resultantes en un arbol D
def offer_minim_common(avl_tree_1, avl_tree_2):
    avl_tree_3 = AVL()
    for activity in avl_tree_1:
        if activity in avl_tree_2:
            if (avl_tree_1[activity].get_cost()) < (avl_tree_2[activity].get_cost()):
                avl_tree_3[activity] = avl_tree_1[activity]
            else:
                avl_tree_3[activity] = avl_tree_2[activity]
    return avl_tree_3


# Funciones para imprimir los arboles
def print_tree(T):
    # Obtener la altura del árbol
    height = T.height()

    # Imprimir el árbol en orden preorden con indentación
    _print_tree(T, T.root(), height, 0)


def _print_tree(T, node, height, indent):
    if node is None:
        return
    else:
        # Imprimir el nodo con su respectiva indentación
        print('      ' * indent, end='')
        if T.left(node) is not None or T.right(node) is not None:
            print('\033[1;34m└── \033[0m', end='')  # Color azul para el nivel actual
        else:
            print('\033[1;34m└── \033[0m', end='')  # Color azul para el nivel actual
        print('\033[1;3{0}m{1}\033[0m'.format(height % 6 + 1, node.key()),' \033[2;50;1m\033[0.1m{0}\033[0m'.format(node.value()))

        # Imprimir los subárboles izquierdo y derecho con una indentación adicional y un nivel de color diferente
        _print_tree(T, T.left(node), height - 1, indent + 1)
        _print_tree(T, T.right(node), height - 1, indent + 1)
        


def print_tree2(T):
    # Obtener la altura del árbol
    height = T.height()

    # Imprimir la raíz del árbol
    _print_tree2(T, T.root(), height, 0, False)


def _print_tree2(T, node, height, indent, child):
    if node is None:
        return
    else:
        # Imprimir los subárboles derecho e izquierdo con una indentación adicional
        _print_tree2(T, T.right(node), height - 1, indent + 1, False)
        
        # Cambiar el símbolo según si el nodo es un hijo izquierdo o derecho
        if child:
            print('         ' * indent, end='')
            print("\033[34m   └────\033[0m",'\033[1;3{0}m{1}\033[0m'.format(height % 6 + 1, node.key()), end='')
        else:
            print('         ' * indent, end='')
            print("\033[34m   ┌────\033[0m",'\033[1;3{0}m{1}\033[0m'.format(height % 6 + 1, node.key()), end='')
        
        print(' \033[2;50;1m\033[0.1m{0}\033[0m'.format(node.value()))
        _print_tree2(T, T.left(node), height - 1, indent + 1, True)
