from classes import *
from items import *

import random
def combat(warrior1, warrior2):
    # Comprobar si ambos personajes tienen vida
    if warrior1.life <= 0:
        print(f"{warrior1.get_name()} está muerto y no puede luchar.")
        return
    elif warrior2.life <= 0:
        print(f"{warrior2.get_name()} está muerto y no puede luchar.")
        return
    
    # Decidir aleatoriamente quién es el atacante y quién el defensor
    attacker, defender = random.sample([warrior1, warrior2], 2)
    print(f"{attacker.get_name()} es el atacante y {defender.get_name()} es el defensor.")

    # Atacar al defensor
    damage = attacker.attack()
    reduced_damage = defender.defend() # Calcular cuánto daño se reduce por la defensa del defensor
    damage_received = max(damage - reduced_damage, 0) # El daño reducido nunca puede ser mayor que el daño causado
    reduce_life(defender, damage_received)
    #print(f"{attacker.get_name()} ha atacado a {defender.get_name()} y le ha causado {damage_received} puntos de daño.") *****
    
    # Comprobar si el defensor ha muerto
    if defender.life <= 0:
        #print(f"{defender.get_name()} ha muerto.") ******
        defender.life = 0 #Esta muerto y al principio del programa comprueba si está muerto para que peleen los muertos
        winner = attacker

        if isinstance(winner, Warrior):
        # Generar una nueva espada para el ganador
            new_sword = generate_sword()
            equip(winner, new_sword)

            # Generar una nueva armadura para el ganador
            new_armor = generate_armor()
            equip(winner, new_armor)

            # Generar un nuevo escudo para el ganador
            new_shield = generate_shield()
            equip(winner, new_shield)
       
    else:
        print("Fin de la batalla me voy corriendo a buscar a otros dos tipos") #En esta parte habría que volver a coger otros dos de la lista para que peleen


#P.D: mirar el código de reduce_ life y mi mirar *******

def generate_armor():
    import random
    name = f"Armor {len(Armor.armors)+1}"
    proteccion = random.randint(1, 5)
    return Armor(name, proteccion)


def generate_shield():
    import random
    name = f"Shield {len(Shield.shields)+1}"
    proteccion = random.randint(1, 5)
    return Shield(name, proteccion)

def reduce_life(self, damage):
        self.life -= damage
        if self.life < 0:
            self.life = 0
            print(f"{self.name} ha muerto")
        else:
            print(f"{self.name} ha recibido {damage} puntos de daño y ahora tiene {self.life} puntos de vida")



def equip(self, item):
        if isinstance(item, Sword) or isinstance(item, Wand):
            if self.weapon is None or item.power > self.weapon.power:
                self.weapon = item
                print(f"{self.name} equipped {item.name} as a weapon!")
            else:
                print(f"{self.name} already has a more powerful weapon equipped!")
        elif isinstance(item, Armor):
            if self.armor is None or item.proteccion > self.armor.proteccion:
                self.armor = item
                print(f"{self.name} equipped {item.name} as armor!")
            else:
                print(f"{self.name} already has more powerful armor equipped!")
        elif isinstance(item, Shield):
            if isinstance(self, Warrior):
                if self.shield is None or item.proteccion > self.shield.proteccion:
                    self.shield = item
                    print(f"{self.name} equipped {item.name} as a shield!")
                else:
                    print(f"{self.name} already has a more powerful shield equipped!")
            else:
                print(f"{self.name} cannot equip a shield!")
        else:
            print(f"{item.name} is not a weapon or armor!")

#def equip(self, item):
    #if isinstance(item, Sword) or isinstance(item, Wand):
        #self.weapon = item
        #print(f"{self.name} equipped {item.name} as a weapon!")
    #elif isinstance(item, Armor):
        #self.armor = item
        #print(f"{self.name} equipped {item.name} as armor!")
    #elif isinstance(item, Shield):
        #if isinstance(self, Warrior):
            #self.shield = item
            #print(f"{self.name} equipped {item.name} as a shield!")
        #else:
            #print(f"{self.name} cannot equip a shield!")
    #else:
        #print(f"{item.name} is not a weapon or armor!")


#PRUEBAS
#espada = Sword("Espada", 10)

#Muestras las armas


Morthecaiser = Warrior("Morthecaiser", 100, 50, 25, 5 , None, None, None)
#sword.mostrar() #Muestra el Nombre y el poder del item

# Llamar al método get_name usando el operador punto
print(Morthecaiser.get_name())
print(Morthecaiser.get_weapon())
print(Morthecaiser.get_armor())
print(Morthecaiser.get_shield())

Racun = Warrior("Racun", 100, 50, 25, 5 , None, None, None)
#sword.mostrar() #Muestra el Nombre y el poder del item

combat(Morthecaiser,Racun)
print(Morthecaiser.get_life())
print(Racun.get_life())
combat(Morthecaiser,Racun)
print(Morthecaiser.get_life())
print(Racun.get_life())
combat(Morthecaiser,Racun)
print(Morthecaiser.get_life())
print(Racun.get_life())
combat(Morthecaiser,Racun)
print(Morthecaiser.get_life())
print(Racun.get_life())
combat(Morthecaiser,Racun)
print(Morthecaiser.get_life())
print(Racun.get_life())
combat(Morthecaiser,Racun)
print(Morthecaiser.get_life())
print(Racun.get_life())

print(Racun.get_weapon())
print(Racun.weapon.mostrar())


Thorfinn = Warrior("Thorfinn", 5, 50, 25, 5 , None, None, None)
combat(Thorfinn,Racun)
print(Thorfinn.get_life())
print(Racun.get_life())
combat(Thorfinn,Racun)
print(Thorfinn.get_life())
print(Racun.get_life())

print(Racun.get_weapon())
print(Racun.weapon.mostrar())
 #Funciones para actualizar el arma y la armadura de un personaje
    #def update_weapon(self, weapon):
        #if isinstance(self, Warrior) and isinstance(weapon, Sword):
            #self.weapon = weapon
            #print(f"{self.name} now has a {weapon.name} as a weapon!")
        #elif isinstance(self, Mage) and isinstance(weapon, Wand):
            #self.weapon = weapon
            #print(f"{self.name} now has a {weapon.name} as a weapon!")
        #else:
            #print(f"{self.name} cannot equip {weapon.name}!")

    #def update_armor(self, armor):
        #if isinstance(self, Warrior) and isinstance(armor, Armor):
            #self.armor = armor
            #print(f"{self.name} now has a {armor.name} as an armor!")
        #elif isinstance(self, Mage) and isinstance(armor, Robe):
            #self.armor = armor
            #print(f"{self.name} now has a {armor.name} as a robe!")
        #else:
            #print(f"{self.name} cannot equip {armor.name}!")


    #def damage(self, enemy):
        #attack = self.attack(enemy)
        #enemy.life = enemy.life - attack
        #print(self.name, "ha realizado", attack, "puntos de daño a",enemy.name)
        #if enemy.esta_vivo():
            #print("La vida de",enemy.name,"es",enemy.life)
        #else:
            #enemy.morir()

    #def is_alive(self):
    #return self.life >0

    #def die(self):
        #self.life = 0
        #print(self.name, "ha muerto")