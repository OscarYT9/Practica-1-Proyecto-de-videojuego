import sys
import pandas as pd
from classes import *


Cola_despegues = ArrayQueue()

cola_prioridad_1 = ArrayQueue()
cola_prioridad_2 = ArrayQueue()
cola_prioridad_3 = ArrayQueue()
cola_prioridad_4 = ArrayQueue()
cola_prioridad_5 = ArrayQueue()
cola_mas20 = ArrayQueue()

Lista_de_colas_prioridad = [cola_mas20, cola_prioridad_1, cola_prioridad_2, cola_prioridad_3, cola_prioridad_4, cola_prioridad_5]




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
    data = [] # lista vacía para guardar los datos de cada avión
    while not Cola_despegues.is_empty() or any(len(cola) > 0 for cola in Lista_de_colas_prioridad):
            tiempo += 1
            print("Tiempo Actual:", tiempo)
            if not Cola_despegues.is_empty():
                avion = Cola_despegues.dequeue() # para obtener el elemento del frente de la cola
                avion.time = tiempo
                
                print(f"Entrando en pista vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >") #En términos de eficiencia computacional, utilizar una cadena formateada con f es ligeramente más costoso que simplemente concatenar cadenas con comas.
                if avion.clase == "domestico":
                    Lista_de_colas_prioridad[1].enqueue(avion)
                elif avion.clase == "privado":
                    Lista_de_colas_prioridad[2].enqueue(avion)
                elif avion.clase == "regular":
                    Lista_de_colas_prioridad[3].enqueue(avion)
                elif avion.clase == "charter":
                    Lista_de_colas_prioridad[4].enqueue(avion)
                elif avion.clase == "transoceanico":
                    Lista_de_colas_prioridad[5].enqueue(avion)
    
            # Verificar si han transcurrido 5 unidades de tiempo
            if tiempo % 5 == 0:
                # Ordenar el despegue del vuelo de máxima prioridad
                    if not Lista_de_colas_prioridad[0].is_empty():
                        avion = Lista_de_colas_prioridad[0].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo
                        data.append((avion.id, avion.clase, avion.time, avion.departure))
            
                    elif not Lista_de_colas_prioridad[1].is_empty():
                        avion = Lista_de_colas_prioridad[1].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo
                        data.append((avion.id, avion.clase, avion.time, avion.departure))

                    elif not Lista_de_colas_prioridad[2].is_empty():
                        avion = Lista_de_colas_prioridad[2].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo
                        data.append((avion.id, avion.clase, avion.time, avion.departure))

                    elif not Lista_de_colas_prioridad[3].is_empty():
                        avion = Lista_de_colas_prioridad[3].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo
                        data.append((avion.id, avion.clase, avion.time, avion.departure))

                    elif not Lista_de_colas_prioridad[4].is_empty():
                        avion = Lista_de_colas_prioridad[4].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo
                        data.append((avion.id, avion.clase, avion.time, avion.departure))

                    elif not Lista_de_colas_prioridad[5].is_empty():
                        avion = Lista_de_colas_prioridad[5].dequeue() #Desencola el primer elemento
                        print(f"Despegando vuelo... < {avion.id} > < {avion.clase} > < {avion.time} min >")
                        avion.departure = tiempo
                        data.append((avion.id, avion.clase, avion.time, avion.departure))

            # Verificar si hay aviones en la cola con tiempo mayor a 20
            for cola_prioridad in Lista_de_colas_prioridad:
                for avion in cola_prioridad:
                    if tiempo - avion.time > 20 and avion not in Lista_de_colas_prioridad[0]:
                        cola_prioridad.remove_element(avion)
                        Lista_de_colas_prioridad[0].enqueue(avion)
                        print("se ha cambiado el tiempo",avion.id, avion.clase, avion.time)
                        print('[{}]'.format(', '.join(str(elemento.id) for elemento in cola_mas20)))


    if tiempo == 190:
        import pandas as pd

        # dentro del ciclo while que simula la lógica del aeropuerto
        # agregar los tiempos de entrada y salida de cada avión a la lista data
        # la estructura del avión se representa con una tupla (id, clase, tiempo_entrada, tiempo_salida)
        # por ejemplo: data.append((avion.id, avion.clase, avion.time, avion.departure))

        # una vez que se hayan agregado todos los aviones, se transforma la lista en un DataFrame
        df = pd.DataFrame(data, columns=['id', 'clase', 'time', 'departure'])
        print(df)

        df['duracion'] = df['departure'] - df['time']
        duracion_media_por_clase = df.groupby('clase')['duracion'].mean()
        print("=====================================================")
        print(duracion_media_por_clase)

 



def parse_params(params):
    
    id, clase, time, departure = params[0], params[1], 0, None
    return Avion(id, clase, time, departure)

if __name__ == "__main__":
    run(sys.argv[1])

