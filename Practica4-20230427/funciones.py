import sys
sys.path.append('/project/home/oscaryt9/workspace/Practica4-20230427/ABBs_posicionales')
from ABBs_posicionales.avl_tree import *
from classes import *

#Función sumar actividades
#Recorre el arbol(A) y el arbol(B) y devuelve las actividades que al menos esten en una de las empresas, llama a la funcion eliminar duplicados y almacena las actividades resultantes en un arbol C
def sumar_actividades(avl_tree_1, avl_tree_2):
    avl_tree_3 = AVL()
    for actividad in avl_tree_1:

        if actividad not in avl_tree_3:
            if actividad in avl_tree_2:
                if (avl_tree_1[actividad].get_total_price() / avl_tree_1[actividad].get_participation() / avl_tree_1[actividad].get_duration()) < (avl_tree_2[actividad].get_total_price() / avl_tree_2[actividad].get_participation() / avl_tree_2[actividad].get_duration()):
                    avl_tree_3[actividad] = avl_tree_1[actividad]
                else:
                    avl_tree_3[actividad] = avl_tree_2[actividad]
            else:
                avl_tree_3[actividad] = avl_tree_1[actividad]

        else:
            if actividad in avl_tree_2:
                if (avl_tree_1[actividad].get_total_price() / avl_tree_1[actividad].get_participation() / avl_tree_1[actividad].get_duration()) < (avl_tree_2[actividad].get_total_price() / avl_tree_2[actividad].get_participation() / avl_tree_2[actividad].get_duration()):
                    avl_tree_3[actividad] = avl_tree_1[actividad]
                else:
                    avl_tree_3[actividad] = avl_tree_2[actividad]

    for actividad in avl_tree_2:
        if actividad not in avl_tree_3:
            avl_tree_3[actividad] = avl_tree_2[actividad]

    return avl_tree_3

#Función oferta mínima común
#Recorre el arbol(A) y el arbol(B) y devuelve las actividades que esten en ambas empresas y llama a la funcion eliminar duplicados y almacena las actividades resultantes en un arbol D
def oferta_minima_comun(avl_tree_1, avl_tree_2):
    avl_tree_3 = AVL()
    for actividad in avl_tree_1:
        if actividad in avl_tree_2:
            if (avl_tree_1[actividad].get_total_price() / avl_tree_1[actividad].get_participation() / avl_tree_1[actividad].get_duration()) < (avl_tree_2[actividad].get_total_price() / avl_tree_2[actividad].get_participation() / avl_tree_2[actividad].get_duration()):
                avl_tree_3[actividad] = avl_tree_1[actividad]
            else:
                avl_tree_3[actividad] = avl_tree_2[actividad]
    return avl_tree_3


#Función eliminar duplicados y dejar la actividad con menor coste




