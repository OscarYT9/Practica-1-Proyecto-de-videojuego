from ABBs_posicionales.avl_tree import *
from classes import *
#Función sumar actividades
#Recorre el arbol(A) y el arbol(B) y devuelve las actividades que al menos esten en una de las empresas, llama a la funcion eliminar duplicados y almacena las actividades resultantes en un arbol C
def sumar_actividades(avl_tree_1, avl_tree_2):
    avl_tree_3 = AVL()
    for actividad in avl_tree_1:
        if actividad.get_name() not in avl_tree_3:
            avl_tree_3.insert(actividad.get_name(), actividad)
    for actividad in avl_tree_2:
        if actividad.get_name() not in avl_tree_3:
            avl_tree_3.insert(actividad.get_name(), actividad)
    #eliminar_duplicados(actividadesC)
    return avl_tree_3

#Función oferta mínima común
#Recorre el arbol(A) y el arbol(B) y devuelve las actividades que esten en ambas empresas y llama a la funcion eliminar duplicados y almacena las actividades resultantes en un arbol D
def oferta_comun(avl_tree_1, avl_tree_2):
    avl_tree_4 = AVL()
    for actividad in avl_tree_1:
        if actividad.get_name() in avl_tree_2:
            avl_tree_4.insert(actividad.get_name(), actividad)
    #eliminar_duplicados(actividadesD)
    return avl_tree_4

#Función eliminar duplicados y dejar la actividad con menor coste




