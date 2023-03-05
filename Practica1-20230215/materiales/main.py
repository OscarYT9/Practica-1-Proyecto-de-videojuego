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

    x = personajes.copy()
    i=0
    for i in range(0,31): 
        while len(personajes)>1:
            combat(personajes)
    
    for personaje in x:
        peleas_participadas = resultados[personaje.get_name()]["total_peleas"]
        daño_medio = resultados[personaje.get_name()]["daño_total"] / peleas_participadas if peleas_participadas > 0 else 0
        print(f"{personaje.get_name()} causó un daño medio de {daño_medio} en {peleas_participadas} peleas.")

#def create_warrior(name, life, strength, protection, fury):
    #weapon, armor, shield = None, None, None
    #return Warrior(name, life, strength, protection, fury, weapon, armor, shield)

#def create_mage(name, life, strength, protection, mana):
    #weapon, armor = None, None
    #return Mage(name, life, strength, protection, mana, weapon, armor)

#def create_priest(name, life, strength, protection, mana):
    #weapon, armor = None, None
    #return Priest(name, life, strength, protection, mana, weapon, armor)


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
#El nombre de las armas indica el número de armas que ha tenido el personaje incluido la que tiene