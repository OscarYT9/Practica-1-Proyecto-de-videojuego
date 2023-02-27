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
    for personaje in personajes:
        nombres = []
        nombres.append(personaje.name)

    #while len(pjs)>1:
    combat(nombres)


def create_character(name, life, strength, protection, fury):
    weapon, armor, shield = None, None, None
    return Warrior(name, life, strength, protection, fury, weapon, armor, shield)

def create_character1(name, life, strength, protection, mana):
    weapon, armor = None, None
    return Mage(name, life, strength, protection, mana, weapon, armor)

def create_character2(name, life, strength, protection, mana):
    weapon, armor = None, None
    return Priest(name, life, strength, protection, mana, weapon, armor)


def parse_params(params):

    name, life, strength, protection = params[1], int(params[2]), int(params[3]), int(params[4])
    if params[0].lower() == "warrior":
        fury = int(params[5])
        weapon, armor, shield = None, None, None
        #print ("Create Warrior  [todo]")
        return create_character(name, life, strength, protection, fury)

    elif params[0].lower() == "mage":
        mana = int(params[5])
        weapon, armor = None, None
        #print ("Create Mage [todo]")
        return create_character1(name, life, strength, protection, mana)
    elif params[0].lower() == "priest":
        mana = int(params[5])
        weapon, armor = None, None
        #print ("Create Priest [todo]")
        return create_character2(name, life, strength, protection, mana)
    else:
        raise ValueError("Avatar '{}' is not valid".format(params[0]))
    

if __name__ == "__main__":

    run(sys.argv[1])