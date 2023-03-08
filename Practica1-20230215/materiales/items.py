class Item:
    """Clase base para todos los objetos del juego."""
    pass
#_______________________________________________________________________________________

class Weapon(Item):
    """Clase base para las armas del juego.

    Attributes
    ----------
    name : str
        El nombre del arma.
    power : int
        El poder del arma.

    Methods
    -------
    get_power()
        Devuelve el poder del arma.
    set_shield(power)
        Establece el poder del arma a un nuevo valor.
    mostrar()
        Muestra la información del arma.
    get_name()
        Devuelve el nombre del arma.
    """
    def __init__(self, name, power):

        self.name = name
        self.power = power

    def get_power(self):
        return self.power

    def set_shield(self, power):
        self.power = power

    def mostrar(self):
        #print(f"Nombre: {self.name}")
        #print(f"Poder: {self.power}")
        return f"Nombre: {self.name}\nPoder: {self.power}"

    def get_name(self):
        return self.name


class Sword(Weapon):
    swords = []
    
    def __init__(self, name, power):
        super().__init__(name, power)
        Sword.swords.append(self)

def generate_sword():
    import random
    name = f"Sword {len(Sword.swords)+1}"
    power = random.randint(1, 5)
    return Sword(name, power)


class Wand(Weapon):
    wands = []

    def __init__(self, name, power):
        super().__init__(name,power)
        self.name = name
        self.power = power
        Wand.wands.append({'name': self.name, 'power': self.power})
        
def generate_wand():
    import random
    name = f"Wand {len(Wand.wands)+1}"
    power = random.randint(1, 5)
    return Wand(name, power)

#_______________________________________________________________________________________

class Covering(Item):
    def __init__(self, name, protection):
        self.name = name
        self.protection = protection

    def get_proteccion(self):
        return self.protection

    def set_proteccion(self, protection):
        self.protection = protection
    

    def mostrar(self):
        #print(f"Nombre: {self.name}")
        #print(f"Protección: {self.protection}")
        return f"Nombre: {self.name}\nProtección: {self.protection}"

    def get_name(self):
        return self.name


class Armor(Covering):

    armors = []

    def __init__(self, name,  protection):
        super().__init__(name, protection)

        self.protection = protection


def generate_armor():
    import random
    name = f"Armor {len(Armor.armors)+1}"
    protection = random.randint(1, 5)
    return Armor(name, protection)

class Shield(Covering): #Solo los Warriors pueden tener escudo

    shields = []

    def __init__(self, nombre, protection):
        super().__init__(nombre, protection)

        self.protection = protection

def generate_shield():
    import random
    name = f"Shield {len(Shield.shields)+1}"
    protection = random.randint(1, 5)
    return Shield(name, protection)

