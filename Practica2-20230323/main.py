import sys
from classes import *


Cola_despegues = ArrayQueue()

cola_prioridad_1 = ArrayQueue()
cola_prioridad_2 = ArrayQueue()
cola_prioridad_3 = ArrayQueue()
cola_prioridad_4 = ArrayQueue()
cola_prioridad_5 = ArrayQueue()

Lista_de_colas_prioridad = [cola_prioridad_1, cola_prioridad_2, cola_prioridad_3, cola_prioridad_4, cola_prioridad_5]




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
    while not Cola_despegues.is_empty() or any(len(cola) > 0 for cola in Lista_de_colas_prioridad):
            tiempo += 1
            print("Tiempo Actual:", tiempo)
            if not Cola_despegues.is_empty():
                avion = Cola_despegues.dequeue() # para obtener el elemento del frente de la cola
                avion.time = tiempo
                
                print(f"Entrando en pista vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >") #En términos de eficiencia computacional, utilizar una cadena formateada con f es ligeramente más costoso que simplemente concatenar cadenas con comas.
                if avion.clase == "domestico":
                    Lista_de_colas_prioridad[0].enqueue(avion)
                elif avion.clase == "privado":
                    Lista_de_colas_prioridad[1].enqueue(avion)
                elif avion.clase == "regular":
                    Lista_de_colas_prioridad[2].enqueue(avion)
                elif avion.clase == "charter":
                    Lista_de_colas_prioridad[3].enqueue(avion)
                elif avion.clase == "transoceanico":
                    Lista_de_colas_prioridad[4].enqueue(avion)
    
            # Verificar si han transcurrido 5 unidades de tiempo
            if tiempo % 5 == 0:
                # Ordenar el despegue del vuelo de máxima prioridad
                    if not Lista_de_colas_prioridad[0].is_empty():
                        avion = Lista_de_colas_prioridad[0].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo

                    elif not Lista_de_colas_prioridad[1].is_empty():
                        avion = Lista_de_colas_prioridad[1].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo

                    elif not Lista_de_colas_prioridad[2].is_empty():
                        avion = Lista_de_colas_prioridad[2].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo

                    elif not Lista_de_colas_prioridad[3].is_empty():
                        avion = Lista_de_colas_prioridad[3].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo

                    elif not Lista_de_colas_prioridad[4].is_empty():
                        avion = Lista_de_colas_prioridad[4].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo

            # Verificar si hay aviones en la cola con tiempo mayor a 20
            for i, cola_prioridad in enumerate(Lista_de_colas_prioridad):
                for avion in cola_prioridad:
                    if tiempo - avion.time > 20:
                        cola_prioridad.remove_element(avion)
                        if i == 0:
                            Lista_de_colas_prioridad[0].enqueue(avion)
                            avion.time = tiempo
                            print("se ha cambiado el tiempo",avion.id, avion.clase, avion.time)
                        else:
                            Lista_de_colas_prioridad[i-1].enqueue(avion)  # mover el avión a la cola de prioridad más alta
                            avion.time = tiempo
                            print("se ha cambiado el tiempo", avion.id)

            print(Cola_despegues.__len__())
            print(Lista_de_colas_prioridad.__len__())
            print("")
            for i in Lista_de_colas_prioridad:
                print(i.__len__())

 



def parse_params(params):
    
    id, clase, time, departure = params[0], params[1], 0, None
    return Avion(id, clase, time, departure)

if __name__ == "__main__":
    run(sys.argv[1])

