import numpy as np
import pandas as pd
import sys
from classes import *
from items import *
from combat import *

personajes = []

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
            personaje = parse_params(pj.split()) #Separar por espacios
            personajes.append(personaje)
    #TODO: Implement simulation here

    import copy
    i=0
    for i in range(0,30):
        personajes_copy = copy.deepcopy(personajes)
        while len(personajes_copy)>1:
            combat(personajes_copy)
        
    #Creamos el DataFrame
    df = pd.DataFrame.from_dict(resultados, orient='index')
    df.rename_axis("nombre", inplace=True)
    df["daño_medio"] = df["daño_total"] / df["total_peleas_atacante"]
    df["curacion_media"] = df["curación"] / df["total_peleas_atacante"]

    df["desviacion_tipica_daño"] = df["daño_medio"].apply(lambda x: np.sqrt(((df["daño_medio"] - x)**2).sum() / df["daño_medio"].count()))
    df["desviacion_tipica_curacion"] = np.where(df['clase'] == 'Priest', df["curacion_media"].apply(lambda x: np.sqrt(((df["curacion_media"] - x)**2).sum() / df["curacion_media"].count())), np.nan)


    #Ordenamos el DataFrame por numero de victorias (en orden descendente)
    df_sorted = df.sort_values(by="victorias", ascending=False)
    df.groupby("nombre")[["daño_medio", "desviacion_tipica_daño"]].mean().reset_index()
    print(df_sorted[["victorias", "daño_medio", "desviacion_tipica_daño", "curacion_media","desviacion_tipica_curacion"]].to_string(max_rows=None))

    #Calculamos la media de daño y desviación atípica por clases e imprimimos el DataFrame
    class_stats = df.groupby('clase').agg({'daño_medio': ['mean', 'std'], 'victorias': 'sum'})
    print(class_stats)

    graficos=0
    if graficos == 1:
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
        
        unique_classes = df['clase'].unique()
        if len(unique_classes) == 2:
            sns.pairplot(df, hue='clase', markers=['o', 's'],
                        plot_kws={'alpha': 0.5}) # Set marker opacity here
        else:
            sns.pairplot(df, hue='clase', markers=['o', 's', 'D'],
                        plot_kws={'alpha': 0.5}) # Set marker opacity here
        plt.show()
        plt.savefig('mi_grafico.png')
            
        #Gráfico interactivo con todas las columnas del DataFrame
        import plotly.express as px

        # Create a dictionary that maps class names to marker symbols
        symbol_map = {'Mage': 'square', 'Warrior': 'diamond', 'Priest': 'circle'}

        # Create a list of colors for the classes

        fig = px.scatter_matrix(df,
            dimensions=['victorias', 'daño_total', 'total_peleas_atacante', 'curación', 'daño_medio', 'desviacion_tipica_daño',"desviacion_tipica_curacion"],
            color='clase',
            opacity=0.5,
            symbol='clase',
            symbol_map=symbol_map)

        fig.show()
    
def parse_params(params):
    """
    Crea un objeto de tipo Warrior, Mage o Priest con los parámetros especificados.
    
    Parameters
    ----------
    params : list
        lista con los parámetros del personaje (clase, nombre, vida, fuerza, protección, otros parámetros dependiendo de la clase)
    
    Returns
    -------
    Un objeto de la clase correspondiente (Warrior, Mage o Priest)
    
    Raises
    -------
    ValueError: si el primer parámetro de la lista no corresponde a ninguna de las tres clases válidas (Warrior, Mage o Priest)
    """

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
