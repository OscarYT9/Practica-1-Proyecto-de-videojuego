import sys
sys.path.append('/project/home/oscaryt9/workspace/Practica4-20230427/ABBs_posicionales')
from ABBs_posicionales import *

def preorder_indent_BST(T, p, d):
    """Print preorder representation of a binary subtree of T rooted at p at depth d.
        To print aTree completely call preorder_indent_BST(aTree, aTree.root(), 0)"""
    if p is not None:
        # use depth for indentation
        print(2*d*' ' + "(" + str(p.key()) + "," +  str(p.value()) + ")") 
        preorder_indent_BST(T, T.left(p), d+1) # left child depth is d+1
        preorder_indent_BST(T, T.right(p), d+1) # right child depth is d+1


from classes import *
from funciones import *
avl_tree_1 = AVL()
print("Árbol vacío"); preorder_indent_BST(avl_tree_1,avl_tree_1.root(),0)
avl_tree_2 = AVL()
print("Árbol vacío"); preorder_indent_BST(avl_tree_2,avl_tree_2.root(),0)


def leer_actividades(path, arbol):

    with open(path) as archivo:
        # Abrir el archivo de texto y leer cada línea
        lineas = archivo.readlines()
        # Iterar sobre las líneas del archivo y agregar cada libro a la lista
        for linea in range(1, len(lineas)):
            # Dividir la línea en tres partes: título, autor y año de edición
            actividad = parse_params(lineas[linea].strip().split(';'))
            # Agregar el libro a la lista, ordenando por autor, título y año de edición
            arbol[actividad.get_name()] = actividad

#TODO: Implement simulation here

def parse_params(params):
    
    name, duration, participation, total_price = params[0], int(params[1]), int(params[2]), float(params[3])
    return Actividad(name, duration, participation, total_price)



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

if __name__ == "__main__":

    # Leer las actividades del archivo A y almacenarlas en el árbol 1
    leer_actividades("actividadesA.txt", avl_tree_1)
    preorder_indent_BST(avl_tree_1,avl_tree_1.root(),0)
    print("")
    # Leer las actividades del archivo B y almacenarlas en el árbol 2
    leer_actividades("actividadesB.txt", avl_tree_2)
    preorder_indent_BST(avl_tree_2,avl_tree_2.root(),0)

    #for actividad in avl_tree_1:
        #print(actividad)
    #for actividad in avl_tree_2:
        #print(actividad)
    print("")
    avl_tree_3 = sumar_actividades(avl_tree_1,avl_tree_2)
    preorder_indent_BST(avl_tree_3,avl_tree_3.root(),0)

    for actividad in avl_tree_3:
        print(actividad, avl_tree_3[actividad].total_price)

    print("")

    avl_tree_4 = oferta_minima_comun(avl_tree_1,avl_tree_2)
    preorder_indent_BST(avl_tree_4, avl_tree_4.root(),0)

    for actividad in avl_tree_4:
        print(actividad, avl_tree_4[actividad].total_price)


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
            print('\033[1;3{0}m{1}:{2}\033[0m'.format(height % 6 + 1, node.key(), node.value()))

            # Imprimir los subárboles izquierdo y derecho con una indentación adicional y un nivel de color diferente
            _print_tree(T, T.left(node), height - 1, indent + 1)
            _print_tree(T, T.right(node), height - 1, indent + 1)


    print_tree(avl_tree_2)

    print("___________________________________________________________________________________________________________________________________________________")
    from treelib import Node, Tree

    def preorder_tree_BST(T, p, tree, parent=None):
        """Add preorder representation of a binary subtree of T rooted at p to tree"""
        if p is not None:
            node_id = str(p.key()) + ", " + str(p.value())
            if parent is not None:
                tree.create_node(tag=node_id, identifier=node_id, parent=parent)
            else:
                tree.create_node(tag=node_id, identifier=node_id)
            preorder_tree_BST(T, T.left(p), tree, parent=node_id)
            preorder_tree_BST(T, T.right(p), tree, parent=node_id)

    # Construir un objeto Tree de treelib y añadir el nodo raíz
    avl_tree_interactive = Tree()

    # Añadir los nodos del árbol de búsqueda binaria AVL
    preorder_tree_BST(avl_tree_1, avl_tree_1.root(), avl_tree_interactive)

    # Mostrar el árbol de búsqueda binaria AVL de forma interactiva
    avl_tree_interactive.show()


    import plotly.graph_objects as go

    fig = go.Figure(go.Treemap(
        labels = ["root", "karaoke", "combate con churros de gomaespuma", "cine", "gimnasia", "fotografía", "senderismo", "pintura", "yoga", "teatro"],
        parents = ["", "root", "karaoke", "combate con churros de gomaespuma", "combate con churros de gomaespuma", "karaoke", "root", "senderismo", "senderismo", "yoga"],
    ))

    fig.show()
