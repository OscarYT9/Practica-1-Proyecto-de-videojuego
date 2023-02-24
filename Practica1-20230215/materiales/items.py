class Item:
    pass
#_______________________________________________________________________________________

class Weapon(Item):
    def __init__(self, name, power):

        self.name = name
        self.power = power

    def get_power(self):
        return self.power

    def set_shield(self, power):
        self.power = power

    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Poder: {self.power}")

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
    def __init__(self, name, proteccion):
        self.name = name
        self.proteccion = proteccion

    def get_proteccion(self):
        return self.proteccion

    def set_proteccion(self, proteccion):
        self.proteccion = proteccion
    

    def mostrar(self):
        print(f"Nombre: {self.name}")
        print(f"Protección: {self.proteccion}")

    def get_name(self):
        return self.name


class Armor(Covering):

    armors = []

    def __init__(self, name,  proteccion):
        super().__init__(name, proteccion)

        self.proteccion = proteccion


def generate_armor():
    import random
    name = f"Armor {len(Armor.armors)+1}"
    proteccion = random.randint(1, 5)
    return Armor(name, proteccion)

class Shield(Covering): #Solo los Warriors pueden tener escudo

    shields = []

    def __init__(self, nombre, proteccion):
        super().__init__(nombre, proteccion)

        self.proteccion = proteccion

def generate_shield():
    import random
    name = f"Shield {len(Shield.shields)+1}"
    proteccion = random.randint(1, 5)
    return Shield(name, proteccion)

