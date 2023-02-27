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

    for i in range(0,31):
        while len(personajes)>1:
            combat(personajes)

def parse_params(params):

    name, life, strength, protection = params[1], int(params[2]), int(params[3]), int(params[4])
    if params[0].lower() == "warrior":
        fury = int(params[5])
        weapon, armor, shield = None, None, None
        print ("Create Warrior  [todo]")
    elif params[0].lower() == "mage":
        mana = int(params[5])
        weapon, armor = None, None
        print ("Create Mage [todo]")
    elif params[0].lower() == "priest":
        mana = int(params[5])
        weapon, armor = None, None
        print ("Create Priest [todo]")
    else:
        raise ValueError("Avatar '{}' is not valid".format(params[0]))
    

if __name__ == "__main__":

    run(sys.argv[1])

