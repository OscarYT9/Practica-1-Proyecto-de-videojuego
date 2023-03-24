import sys
from classes import *


Cola_despegues = ArrayQueue()

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


    

def parse_params(params):
    
    id, clase = params[0], params[1]
    #print ("Create Warrior  [todo]")
    return Avion(id, clase)

if __name__ == "__main__":
    run(sys.argv[1])

