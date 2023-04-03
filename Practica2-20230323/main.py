import sys
from classes import *
import pandas as pd

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
    data = [] # lista vacía para guardar los datos de cada avión
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

            # Verificar si hay aviones en la cola con tiempo mayor a 20
            for i, cola_prioridad in enumerate(Lista_de_colas_prioridad):
                for avion in cola_prioridad:
                    if tiempo - avion.time > 20:
                        if i > 0:
                            cola_prioridad.remove_element(avion)
                            Lista_de_colas_prioridad[i-1].enqueue(avion)  # mover el avión a la cola de prioridad más alta
                            avion.time = tiempo
                            print("se ha cambiado el tiempo", avion.id)



    import pandas as pd

    # dentro del ciclo while que simula la lógica del aeropuerto
    # agregar los tiempos de entrada y salida de cada avión a la lista data
    # la estructura del avión se representa con una tupla (id, clase, tiempo_entrada, tiempo_salida)
    # por ejemplo: data.append((avion.id, avion.clase, avion.time, avion.departure))

    # una vez que se hayan agregado todos los aviones, se transforma la lista en un DataFrame
    df = pd.DataFrame(data, columns=['id', 'clase', 'time', 'departure'])

    df['duracion'] = df['departure'] - df['time']
    
    #Creamos un nuevo dataframe que contiene los valores de la columna "clase" y los valores de las duraciones medias por grupo.
    duracion_media_por_clase = df.groupby('clase')['duracion'].mean().reset_index()

    # Ordenar las duraciones promedio de menor a mayor
    duracion_media_por_clase = duracion_media_por_clase.sort_values('duracion', ascending=True).reset_index(drop=True)

    # Reordenar las categorías de 'clase' en el DataFrame original
    df['clase'] = pd.Categorical(df['clase'], categories=duracion_media_por_clase['clase'], ordered=True)

    print("=====================================================")
    print("                   Datos aviones                     ")
    print("=====================================================")

    print(df)
    
    print("===============================================================================================================================")
    print("Media entre el momento en el que el avión entra en pista y el momento en que despega, agrupado por la clase de vuelo (Duración)")
    print("===============================================================================================================================")

    print(duracion_media_por_clase)

    import seaborn as sns
    import matplotlib.pyplot as plt

# Crear los subplots con los dos ejes y compartir el eje x
    x = input("¿Quieres imprimir los gráficos? [y/n] ")
    if x == "y":
        y = 1
        if y == 1:
            fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True, figsize=(10,5), gridspec_kw={'width_ratios': [3, 1]})

            sns.boxplot(x='clase', y='duracion', data=df, ax=ax1)
            ax1.set(xlabel='Clase', ylabel='Duración')

            sns.barplot(x='clase', y='duracion', data=df.groupby('clase')['duracion'].mean().reset_index(), ax=ax2).set(xlabel=None)
            ax2.set(xlabel='', ylabel='Duración promedio')
            ax2.set_xticklabels(ax2.get_xticklabels(), rotation=90)

            plt.show()
            plt.savefig('Gráficos1.png')
        if y == 1:

            fig, (ax1, ax2) = plt.subplots(nrows=2, sharey=True, figsize=(10,5))

            sns.boxplot(x='duracion', y='clase', data=df, ax=ax1)
            ax1.set(xlabel='Duración', ylabel='Clase')

            sns.barplot(x='duracion', y='clase', data=df.groupby('clase')['duracion'].mean().reset_index(), ax=ax2)
            ax2.set(xlabel='Duración promedio', ylabel='')

            plt.show()
            plt.savefig('Gráficos2.png')
        
        if y ==1:
            fig, (ax1, ax2) = plt.subplots(ncols=2, sharey=True, figsize=(10,5), gridspec_kw={'width_ratios': [3, 1]})

            sns.boxplot(y='clase', x='duracion', data=df, ax=ax1)
            ax1.set(xlabel='Duración', ylabel='Clase')

            sns.barplot(y='clase', x='duracion', data=df.groupby('clase')['duracion'].mean().reset_index(), ax=ax2)
            ax2.set(xlabel='Duración promedio', ylabel='')

            plt.show()
            plt.savefig('Gráficos3.png')

        import plotly.express as px
        import plotly.graph_objs as go
        from plotly.subplots import make_subplots
        

        #Gráfico interactivo
        colores = {'domestico': 'cornflowerblue', 'privado': 'gold', 'regular': 'mediumseagreen', 'charter': 'tomato', 'transoceanico': 'plum'}

        fig = make_subplots(rows=3, cols=1, shared_yaxes=True,
                            subplot_titles=("Duración por Clase", "Duración Promedio por Clase", "Dispersión de Tiempo por Avión"))

        for tipo, group in df.groupby('clase'):
            fig.add_trace(go.Box(x=group['clase'], y=group['duracion'], name=tipo, marker_color=colores[tipo]), row=1, col=1)

        fig.add_trace(go.Bar(x=duracion_media_por_clase['clase'], y=duracion_media_por_clase['duracion'], name="Duración Promedio", marker_color=[colores[tipo] for tipo in duracion_media_por_clase['clase']]), row=2, col=1)

        tiempo_total_por_avion = df.groupby('id')['duracion'].sum().reset_index().sort_values(by='duracion')
        fig.add_trace(go.Scatter(x=tiempo_total_por_avion['id'], y=tiempo_total_por_avion['duracion'], mode='markers', 
                        marker=dict(color=[colores[tipo] for tipo in df['clase']], size=10, line_width=1), 
                        text=tiempo_total_por_avion['duracion'], name='Tiempo Total de Vuelo'), row=3, col=1)

        fig.update_xaxes(title_text="Clase", row=1, col=1)
        fig.update_yaxes(title_text="Duración", row=1, col=1)
        fig.update_xaxes(title_text="Clase", row=2, col=1)
        fig.update_yaxes(title_text="Duración Promedio", row=2, col=1)
        fig.update_xaxes(title_text="Avión", row=3, col=1)
        fig.update_yaxes(title_text="Tiempo Total", row=3, col=1)

        fig.update_layout(height=4000, showlegend=True, coloraxis_showscale=False)

        fig.update_layout(
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=1.02,
                xanchor="right",
                x=1
            )
        )

        tiempo_total_por_avion['duracion_texto'] = tiempo_total_por_avion['duracion'].apply(lambda x: f"{x:.2g} min")
        fig.update_traces(text=tiempo_total_por_avion['duracion_texto'], row=3, col=1)

        fig.show()







def parse_params(params):
    
    id, clase, time, departure = params[0], params[1], 0, None
    return Avion(id, clase, time, departure)

if __name__ == "__main__":
    run(sys.argv[1])

