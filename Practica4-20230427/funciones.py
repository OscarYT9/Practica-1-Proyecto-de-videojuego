import sys
sys.path.append('/project/home/oscaryt9/workspace/Practica4-20230427/ABBs_posicionales')
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
                add_activities[marker_B.key()] = marker_B.value()       # Aprobechamos y también agregamos la actividadB comun a add_activities

            marker_A = avl_tree_1.after(marker_A) # Pasamos al siguiente NodoA (marcador)
            marker_B = avl_tree_2.after(marker_B) # Pasamos al siguiente NodoB (marcador)

        # Si no son iguales es que las actividades no son comunes
        elif marker_A.key() < marker_B.key():
            add_activities[marker_A.key()] = marker_A.value() 
            marker_A = avl_tree_1.after(marker_A) # Pasamos al siguiente NodoA (marcador)

        else:
            add_activities[marker_B.key()] = marker_B.value()
            marker_B = avl_tree_2.after(marker_B) # Pasamos al siguiente NodoB (marcador)

    # Agregar las actividades restantes de avl_tree_1, si las hay
    while marker_A is not None:
        add_activities[marker_A.key()] = marker_A.value() # Metemos la actividadB comun en add_activities
        marker_A = avl_tree_1.after(marker_A) # Pasamos al siguiente NodoA (marcador)

    # Agregar las actividades restantes de avl_tree_2, si las hay
    while marker_B is not None:
        add_activities[marker_B.key()] = marker_B.value() # Metemos la actividadB comun en add_activities
        marker_B = avl_tree_2.after(marker_B) # Pasamos al siguiente NodoB (marcador)
        
    return add_activities, offer_minim_common # Al final del todo devolvemos la tupla con los arboles

                




# Función eliminar duplicados y dejar la actividad con menor coste
# Función sumar actividades
# Recorre el arbol(A) y el arbol(B) y devuelve las actividades que al menos esten en una de las empresas, llama a la funcion offer_minim_common y almacena las actividades resultantes en un arbol C
# Es decir, las empresas comunes y no comunes
def add_activities(avl_tree_1, avl_tree_2):
    """
    Combina los dos árboles AVL dados en uno nuevo, agregando las actividades únicas de ambos árboles.

    Parameters
    ----------
    avl_tree_1 : AVLTree
        El primer árbol AVL que se quiere combinar.
    avl_tree_2 : AVLTree
        El segundo árbol AVL que se quiere combinar.

    Returns
    -------
    AVLTree
        Un nuevo árbol AVL que contiene todas las actividades de avl_tree_1 y avl_tree_2, eliminando las duplicadas.
    """
    avl_tree_3 = offer_minim_common(avl_tree_1, avl_tree_2)

    for activity in avl_tree_1:
        if activity not in avl_tree_3:
            avl_tree_3[activity] = avl_tree_1[activity]

    for activity in avl_tree_2:
        if activity not in avl_tree_3:
            avl_tree_3[activity] = avl_tree_2[activity]

    return avl_tree_3

# Función oferta mínima común
# Recorre el arbol(A) y el arbol(B) y devuelve las actividades que esten en ambas empresas y llama a la funcion eliminar duplicados y almacena las actividades resultantes en un arbol D
# Es decir, las empresas comunes
def offer_minim_common(avl_tree_1, avl_tree_2):
    """
    Crea un nuevo árbol AVL que contiene las actividades en común entre avl_tree_1 y avl_tree_2,
    y sus valores son los objetos Activity que tienen los costos por participante más bajos.

    Parameters
    ----------
    avl_tree_1 : AVL
        El primer árbol AVL que contiene actividades.
    avl_tree_2 : AVL
        El segundo árbol AVL que contiene actividades.

    Returns
    -------
    AVL
        Un nuevo árbol AVL que contiene las actividades en común entre avl_tree_1 y avl_tree_2,
        y sus valores son los objetos Activity que tienen los costos por participante más bajos.
    """
    avl_tree_3 = AVL()
    for activity in avl_tree_1:
        if activity in avl_tree_2:
            if (avl_tree_1[activity].get_cost_per_participate()) < (avl_tree_2[activity].get_cost_per_participate()):
                avl_tree_3[activity] = avl_tree_1[activity]
            else:
                avl_tree_3[activity] = avl_tree_2[activity]
    return avl_tree_3


# Funciones para imprimir los arboles
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
        print('\033[1;3{0}m{1}\033[0m'.format(height % 6 + 1, node.key()),' \033[2;50;1m\033[0.1m{0}\033[0m'.format(node.value()))

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
        
        # Cambiar el símbolo según si el nodo es un hijo izquierdo o derecho
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
