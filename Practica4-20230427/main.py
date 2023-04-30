from ABBs_posicionales.avl_tree import *
from classes import *
from funciones import *
avl_tree_1 = AVL()
avl_tree_2 = AVL()


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

    # Leer las actividades del archivo B y almacenarlas en el árbol 2
    leer_actividades("actividadesB.txt", avl_tree_2)
        
    print(avl_tree_1)
    print(avl_tree_2)
    #for actividad in avl_tree_1:
        #print(actividad)
    #for actividad in avl_tree_2:
        #print(actividad)
    sumar_actividades(avl_tree_1,avl_tree_2)
    oferta_comun(avl_tree_1,avl_tree_2)
    print(avl_tree_3)
    print(avl_tree_4)