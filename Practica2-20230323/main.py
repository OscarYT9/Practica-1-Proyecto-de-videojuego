import sys
from classes import *


Cola_despegues = ArrayQueue()
Lista_de_colas_prioridad = PriorityQueue()

def run(path):
    """
    Ejecuta la simulación de combate entre los personajes leídos desde el archivo especificado.
    
    Parameters
    ----------
    path : str
        ruta del archivo que contiene los parámetros de los personajes
    
    Returns
    -------    
    None
    """

    with open(path) as f:
        pjs = f.readlines()
        for pj in pjs:
            avion = parse_params(pj.split())
            Cola_despegues.enqueue(avion)
    #TODO: Implement simulation here

    print(Cola_despegues.__len__())
    tiempo = 0
    while not Lista_de_colas_prioridad.is_empty() or not Cola_despegues.is_empty():
        tiempo += 1
        avion = Cola_despegues.dequeue() # para obtener el elemento del frente de la cola
        avion.time = tiempo
        
        print(f"Entrando en pista vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >") #En términos de eficiencia computacional, utilizar una cadena formateada con f es ligeramente más costoso que simplemente concatenar cadenas con comas.
        if avion.clase == "domestico":
            Lista_de_colas_prioridad.push(avion,5)
        elif avion.clase == "privado":
            Lista_de_colas_prioridad.push(avion,4)
        elif avion.clase == "regular":
            Lista_de_colas_prioridad.push(avion,3)
        elif avion.clase == "charter":
            Lista_de_colas_prioridad.push(avion,2)
        elif avion.clase == "transoceanico":
            Lista_de_colas_prioridad.push(avion,1)
        
        # Verificar si hay aviones en la cola con tiempo mayor a 20
        for i in range(Lista_de_colas_prioridad.__len__()):
            avion_en_cola = Lista_de_colas_prioridad.__getitem__(i)
            if avion_en_cola.time > 20:
                Lista_de_colas_prioridad.remove(avion_en_cola)
                Lista_de_colas_prioridad.push(avion_en_cola,5)
        # Verificar si han transcurrido 5 unidades de tiempo
        if tiempo % 5 == 0:
            x = Lista_de_colas_prioridad.pop()
            print(x.id)
            print(f"Se ha ordenado el despegue del vuelo de maxima prioridad {x.id}, {x.clase}, {x.time}")
    print(Lista_de_colas_prioridad.__len__())
def parse_params(params):
    
    id, clase, time = params[0], params[1],0
    return Avion(id, clase, time)

if __name__ == "__main__":
    run(sys.argv[1])

