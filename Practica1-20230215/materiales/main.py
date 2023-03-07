import numpy as np
import pandas as pd
import math
import sys
from classes import *
from items import *
from combat import *

personajes = []

def run(path):

    with open(path) as f:
        pjs = f.readlines()
        for pj in pjs:
            personaje = parse_params(pj.split()) #Separar por espacios
            personajes.append(personaje)
    #TODO: Implement simulation here

    x = personajes.copy() #Creamos una copia de la lista de personajes antes de ejecutar el bucle (la necesitaremos para obtener los nombres de los personajes y así acceder al diccionario de resultados)
    i=0
    for i in range(0,31): 
        while len(personajes)>1:
            combat(personajes)
    
    #Creamos el DataFrame
    df = pd.DataFrame.from_dict(resultados, orient='index')
    df.rename_axis("nombre", inplace=True)
    df["daño_medio"] = df["daño_total"] / df["total_peleas_atacante"]
    df["desviacion_tipica"] = df["daño_total"].apply(lambda x: np.sqrt(((df["daño_total"] - x)**2).sum() / df["daño_total"].count()))

    #Ordenamos el DataFrame por numero de victorias (en orden descendente)
    df_sorted = df.sort_values(by="victorias", ascending=False)
    df.groupby("nombre")[["daño_medio", "desviacion_tipica"]].mean().reset_index()
    print(df_sorted.to_string(max_rows=None))

    #Calculamos la media de daño y desviación atípica por clases e imprimimos el DataFrame
    class_stats = df.groupby('clase')['daño_medio'].agg(['mean', 'std'])
    print(class_stats)

    import matplotlib.pyplot as plt

    # Crear el gráfico
    plt.scatter(df['clase'], df['victorias'])

    # Agregar etiquetas de los ejes
    plt.xlabel('Eje X')
    plt.ylabel('Victorias')

    # Agregar título al gráfico
    plt.title('Gráfico de dispersión')

    # Mostrar el gráfico
    plt.show()
    plt.savefig('nombre_del_archivo.png')
    
    #Gráfico con todas las columnas del DataFrame
    import seaborn as sns
    import matplotlib.pyplot as plt

    sns.pairplot(df, hue='clase', markers=['o', 's', 'D'],
                plot_kws={'alpha': 0.5}) # Set marker opacity here
    plt.show()
    plt.savefig('mi_grafico.png')
        
    #Gráfico interactivo con todas las columnas del DataFrame
    import plotly.express as px

    # Create a dictionary that maps class names to marker symbols
    symbol_map = {'Mage': 'square', 'Warrior': 'diamond'}

    fig = px.scatter_matrix(df,
        dimensions=['victorias', 'daño_total', 'total_peleas_atacante', 'curación', 'daño_medio', 'desviacion_tipica'],
        color='clase',
        opacity=0.5,
        symbol='clase',
        symbol_map=symbol_map)

    fig.show()

    print(Avatar.get_life.__doc__)
    print(combat.__doc__)
    
def parse_params(params):

    name, life, strength, protection = params[1], int(params[2]), int(params[3]), int(params[4])
    if params[0].lower() == "warrior":
        fury = int(params[5])
        weapon, armor, shield = None, None, None
        #print ("Create Warrior  [todo]")
        return Warrior(name, life, strength, protection, fury, weapon, armor, shield)

    elif params[0].lower() == "mage":
        mana = int(params[5])
        weapon, armor = None, None
        #print ("Create Mage [todo]")
        return Mage(name, life, strength, protection, mana, weapon, armor)
    
    elif params[0].lower() == "priest":
        mana = int(params[5])
        weapon, armor = None, None
        #print ("Create Priest [todo]")
        return Priest(name, life, strength, protection, mana, weapon, armor)
    
    else:
        raise ValueError("Avatar '{}' is not valid".format(params[0]))
    
if __name__ == "__main__":

    run(sys.argv[1])
