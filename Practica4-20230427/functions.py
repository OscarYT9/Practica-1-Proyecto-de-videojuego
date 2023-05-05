# Nombre del archivo: functions.py
# Autores: Óscar Vilela Rodríguez (oscar.vilela.rodriguez@udc.es), Guillermo García Engelmo (g.garcia2@udc.es)
from ABBs_posicionales.avl_tree import *
from classes import *

# Se pueden crear dos funciones pero es más eficiente crear un sola función y aprovechar el resultado del arbol offer_minim_common.
# Cuando estamos haciendo el primer if (if marker_A.key() == marker_B.key():) cogemos las actividades comunes (offer_minim_common)
# Mientras tanto si en vez de ser comunes encontramos alguna actividad no común la agregamos al add_activities y así nos ahorramos tener que recorrer dos veces los arboles
# Al final nos quedan dos arboles, offer_minim_common (actividades comunes) y add_activities (actividades comunes y no comunes).
def operations(avl_tree_1, avl_tree_2):
    """
    Combina dos árboles AVL de actividades en dos nuevos árboles AVL:
    uno que contiene todas las actividades de ambos árboles sin repetición
    y otro que contiene las actividades que tienen la menor cantidad de cupos
    entre ambos árboles.

    Parameters
    ----------
    avl_tree_1 : AVLTree
        El primer árbol AVL de actividades.
    avl_tree_2 : AVLTree
        El segundo árbol AVL de actividades.

    Returns
    -------
    Tuple[AVLTree, AVLTree]
        Una tupla que contiene dos árboles AVL:
        el primero es un árbol que contiene todas las actividades de ambos árboles sin repetición,
        y el segundo es un árbol que contiene las actividades que tienen la menor cantidad de cupos
        entre ambos árboles.
    """
    add_activities = AVL()
    offer_minim_common = AVL()
    marker_A = avl_tree_1.first()
    marker_B = avl_tree_2.first()

    while marker_A is not None and marker_B is not None:
        # Comprobamos si las claves de los nodos son iguales
        if marker_A.key() == marker_B.key():
            # Comprobamos cual de los dos tiene un coste menor (Comprobamos si un el objeto de un NodoA es menor que el de un NodoB), El marker_A.value() devuelve el valor asociado a la posición actual del marcador, en este caso un objeto Actividad 
            if marker_A.value() < marker_B.value():
                offer_minim_common[marker_A.key()] = marker_A.value()   # Metemos la actividadA comun en offer_minim_common
                add_activities[marker_A.key()] = marker_A.value()       # Aprobechamos y también agregamos la actividadA comun a add_activities
            else:
                offer_minim_common[marker_B.key()] = marker_B.value()   # Metemos la actividadA comun en offer_minim_common
                add_activities[marker_B.key()] = marker_B.value()       # Aprovechamos y también agregamos la actividadB comun a add_activities

            marker_A = avl_tree_1.after(marker_A) # Pasamos al siguiente NodoA (marcador)
            marker_B = avl_tree_2.after(marker_B) # Pasamos al siguiente NodoB (marcador)

        # Si no son iguales es que las actividades no son comunes
        elif marker_A.key() < marker_B.key():
            add_activities[marker_A.key()] = marker_A.value() 
            marker_A = avl_tree_1.after(marker_A) # Pasamos al siguiente NodoA (marcador)

        else:
            add_activities[marker_B.key()] = marker_B.value()
            marker_B = avl_tree_2.after(marker_B) # Pasamos al siguiente NodoB (marcador)

    return add_activities, offer_minim_common # Al final del todo devolvemos la tupla con los arboles

#_____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
# Funciones para imprimir los arboles

def preorder_indent_BST(T, p, d):
        """Print preorder representation of a binary subtree of T rooted at p at depth d.
           To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
        if p is not None:
            # use depth for indentation
            print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
            preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
            preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1


def print_tree(T):
    """
    Imprime un árbol binario en preorden con indentación.

    Parameters
    ----------
    T : BinaryTree
        El árbol binario a imprimir.

    Returns
    -------
    None
    """
    # Obtener la altura del árbol
    height = T.height()

    # Imprimir el árbol en orden preorden con indentación
    _print_tree(T, T.root(), height, 0)


def _print_tree(T, node, height, indent):
    """
    Imprime un subárbol binario en preorden con indentación.
    Parameters
    ----------
    T : BinaryTree
        El árbol binario que contiene el subárbol a imprimir.
    node : BinaryTreeNode
        La raíz del subárbol a imprimir.
    height : int
        La altura del subárbol a imprimir.
    indent : int
        La indentación actual del nodo.

    Returns
    -------
    None
    """
    if node is None:
        return
    else:
        # Imprimir el nodo con su respectiva indentación
        print('      ' * indent, end='')
        if T.left(node) is not None or T.right(node) is not None:
            print('\033[1;34m└── \033[0m', end='')  # Color azul para el nivel actual
        else:
            print('\033[1;34m└── \033[0m', end='')  # Color azul para el nivel actual
        # Imprime el nombre y valor del nodo con colores de texto y fondo diferentes, utilizando códigos de escape ANSI.
        print('\033[1;3{0}m{1}\033[0m'.format(height % 6 + 1, node.key()),' \033[2;50;1m\033[0.1m{0}\033[0m'.format(node.value())) # La expresión height % 6 + 1 se utiliza para determinar qué color se debe utilizar para imprimir el nodo. El color se basa en la altura del nodo en el árbol, y la expresión height % 6 devuelve un valor entre 0 y 5, que se utiliza para seleccionar uno de los seis colores disponibles (en este caso, 1, 2, 3, 4, 5, o 6). Luego, se suma 1 para asegurarse de que el valor no sea, ya que el color 0 es el Negro en la Tabla de colores (https://es.wikipedia.org/wiki/C%C3%B3digo_escape_ANSI)

        # Imprimir los subárboles izquierdo y derecho con una indentación adicional y un nivel de color diferente
        _print_tree(T, T.left(node), height - 1, indent + 1)
        _print_tree(T, T.right(node), height - 1, indent + 1)
        


def print_tree2(T):
    """
    Imprime un árbol binario con indentación y las ramas del árbol conectadas con líneas.

    Parameters
    ----------
    T : BinaryTree
        El árbol binario a imprimir.

    Returns
    -------
    None
    """
    # Obtener la altura del árbol
    height = T.height()

    # Imprimir la raíz del árbol
    _print_tree2(T, T.root(), height, 0, False)


def _print_tree2(T, node, height, indent, child):
    """
    Imprime un subárbol derecho e izquierdo con indentación adicional.
    Parameters
    ----------
    T : BinaryTree
        El árbol binario a imprimir.
    node : Position
        La posición del nodo actual.
    height : int
        La altura del nodo actual.
    indent : int
        La indentación actual.
    child : bool
        Booleano que indica si el nodo es hijo izquierdo (True) o derecho (False).

    Returns
    -------
    None
    """
    if node is None:
        return
    else:
        # Imprimir los subárboles derecho e izquierdo con una indentación adicional
        # Imprime el nodo hijo derecho con valor de child False (se usa en el bucle para identificar el nodo)
        _print_tree2(T, T.right(node), height - 1, indent + 1, False)
        
        # Cambiar el símbolo según si el nodo es un hijo izquierdo o derecho (o la raiz que tiene siempre identación 0)
        if child:
            print('         ' * indent, end='')
            print("\033[34m   └────\033[0m",'\033[1;3{0}m{1}\033[0m'.format(height % 6 + 1, node.key()), end='')
        elif indent == 0:
            print('\033[34m   ──────\033[0m', end='')
            print('\033[1;3{0}m{1}\033[0m'.format(height % 6 + 1, node.key()), end='')
        else:
            print('         ' * indent, end='')
            print("\033[34m   ┌────\033[0m",'\033[1;3{0}m{1}\033[0m'.format(height % 6 + 1, node.key()), end='')
        
        print(' \033[2;50;1m\033[0.1m{0}\033[0m'.format(node.value()))
        # Imprime el nodo hijo izquierdo con valor de child True (se usa en el bucle para identificar el nodo)
        _print_tree2(T, T.left(node), height - 1, indent + 1, True)
