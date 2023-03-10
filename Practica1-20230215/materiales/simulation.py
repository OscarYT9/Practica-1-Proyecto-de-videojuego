from classes import *
from items import *
import random

resultados = {} # Diccionario vacío para almacenar los resultados de cada personaje


def combat(personajes):
    """
    Realiza un combate entre dos personajes aleatorios del conjunto de personajes proporcionado. Un personaje es elegido como el atacante y el otro como el defensor. Se realiza un ataque y se calcula la defensa del defensor. El daño causado al defensor es reducido por la defensa del defensor. Se actualizan los resultados del combate en el diccionario "resultados".

    Parameters
    ----------
    personajes : list
        Una lista de objetos Personaje que se utilizarán en el combate.

    Returns
    -------
    None.
    """

    # Decide aleatoriamente dos personajes de la lista personajes y les asigna la variable atacante y defensor.
    attacker = random.choice(personajes)
    defender = random.choice(personajes)
    while attacker == defender:
        defender = random.choice(personajes)


    # Ataque al defensor en funcion del personaje que sea el atacante,
    if isinstance(attacker, Priest):
        if random.random() < 0.25:
            attacker.life = attacker.heal() + attacker.life

            if attacker.get_name() not in resultados:
                resultados[attacker.get_name()] = {"clase": type(attacker).__name__,"victorias": 0,"daño_total": 0, "total_peleas_atacante":0,"curación": attacker.heal()}
                damage = 0
            else:
                resultados[attacker.get_name()]["curación"] += attacker.heal()
                damage = 0

        else:
            damage = attacker.attack()
    else:
        damage = attacker.attack()

    reduced_damage = defender.defend() # Calcular cuánto daño se reduce por la defensa del defensor
    damage_received = max(damage - reduced_damage, 0) # El daño reducido nunca puede ser mayor que el daño causado
    reduce_life(defender, damage_received)
    

    # Actualiza los resultados
    if attacker.get_name() not in resultados:
        resultados[attacker.get_name()] = {"clase": type(attacker).__name__,"victorias": 0,"daño_total": 0, "total_peleas_atacante":0,"curación":0}
    else:
        resultados[attacker.get_name()]["daño_total"] += damage_received
        resultados[attacker.get_name()]["total_peleas_atacante"] += 1

    if defender.get_name() not in resultados:
        resultados[defender.get_name()] = {"clase": type(defender).__name__,"victorias": 0,"daño_total": 0, "total_peleas_atacante":0,"curación":0}

    # Comprobar si el defensor ha muerto
    if defender.life <= 0:
        defender.life = 0
        personajes.remove(defender) # Elmina al personaje de la lista en caso de morir

        # Actualizar los resultados
        if attacker.get_name() not in resultados and len(personajes)==1:
            resultados[attacker.get_name()] = {"clase": type(attacker).__name__, "victorias": 1,"daño_total": damage_received}
        elif len(personajes)==1:
            resultados[attacker.get_name()]["victorias"] += 1

        winner = attacker
        
        if isinstance(winner, Warrior):
            # Generar una nueva espada para el ganador
            if random.random() < 0.5:
                new_sword = generate_sword()
                equip(winner, new_sword)
            
            # Generar una nueva armadura para el ganador
            if random.random() < 0.5:
                    new_armor = generate_armor()
                    equip(winner, new_armor)

            # Generar un nuevo escudo para el ganador
            if random.random() < 0.5:
                new_shield = generate_shield()
                equip(winner, new_shield)
        
        elif isinstance(winner, Caster):
            # Generar una nueva varita mágica para el ganador
            if random.random() < 0.5:
                new_wand = generate_wand()
                equip(winner, new_wand)
        
            # Generar una nueva armadura para el ganador
            if random.random() < 0.5:
                new_armor = generate_armor()
                equip(winner, new_armor)
        
            
   

def reduce_life(self, damage):
    """
    Reduce la vida del personaje por la cantidad de daño recibido. Si la vida del personaje llega a 0 o menos, se establece la vida en 0.

    Parameters
    ----------
    damage : int
        La cantidad de daño que se reducirá de la vida del personaje.

    Returns
    -------
    None
    """
    self.life -= damage
    if self.life <= 0:
        self.life = 0


def equip(self, item):
    """
    Equipa al personaje con el objeto proporcionado. Si el objeto es una espada o una varita, se equipa como arma. Si el objeto es una armadura o un escudo, se equipa como armadura. Si el objeto es un objeto desconocido, se ignora.

    Parameters
    ----------
    item : Sword, Wand, Armor, Shield
        El objeto que se equipará.

    Returns
    -------
    None
    """
    if isinstance(item, Sword) or isinstance(item, Wand):
        if self.weapon is None or item.power > self.weapon.power:
            self.weapon = item
    elif isinstance(item, Armor):
        if self.armor is None or item.protection > self.armor.protection:
            self.armor = item
    elif isinstance(item, Shield):
        if isinstance(self, Warrior):
            if self.shield is None or item.protection > self.shield.protection:
                self.shield = item

def generate_sword():
    """Genera una espada aleatoria.

    Genera una espada aleatoria con un nombre único y un poder aleatorio entre 1 y 5.

    Parameters
    ----------
    None

    Returns
    -------
    Sword
        Un objeto Sword con un nombre único y un poder aleatorio entre 1 y 5.
    """
    import random
    name = f"Sword {len(Sword.swords)+1}"
    power = random.randint(1, 5)
    return Sword(name, power)

def generate_wand():
    """Genera una varita aleatoria.

    Genera una varita aleatoria con un nombre único y un poder aleatorio entre 1 y 5.

    Parameters
    ----------
    None

    Returns
    -------
    Wand
        Un objeto Wand con un nombre único y un poder aleatorio entre 1 y 5.
    """
    import random
    name = f"Wand {len(Wand.wands)+1}"
    power = random.randint(1, 5)
    return Wand(name, power)

def generate_armor():
    """Genera una armadura aleatoria.

    Genera una armadura aleatoria con un nombre único y una protección aleatoria entre 1 y 5.

    Parameters
    ----------
    None

    Returns
    -------
    Armor
        Un objeto Armor con un nombre único y una protección aleatoria entre 1 y 5.
    """
    import random
    name = f"Armor {len(Armor.armors)+1}"
    protection = random.randint(1, 5)
    return Armor(name, protection)

def generate_shield():
    """Genera un escudo aleatorio.

    Genera un escudo aleatorio con un nombre único y una protección aleatoria entre 1 y 5.

    Parameters
    ----------
    None

    Returns
    -------
    Shield
        Un objeto Shield con un nombre único y una protección aleatoria entre 1 y 5.
    """
    import random
    name = f"Shield {len(Shield.shields)+1}"
    protection = random.randint(1, 5)
    return Shield(name, protection)