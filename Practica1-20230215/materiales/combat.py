from classes import *
from items import *
import random

total_peleas = []
resultados = {} # diccionario vacío para almacenar los resultados de cada personaje
#personajes_info = []
#victorias=0
#victorias+=1
#personajes_info.append([winner.name, winner.__class__.__name__, winner.life, winner.attack(),victorias])
#print("Lista con los nombres de los personajes: ",personajes_info)

def combat(personajes):

    # Decidir aleatoriamente quién es el atacante y quién el defensor
    attacker = random.choice(personajes)
    defender = random.choice(personajes)
    while attacker == defender:
        defender = random.choice(personajes)

    #print("El atacante es:", attacker.name,"y el defensor es:", defender.name)

    # Atacar al defensor
    if isinstance(attacker, Priest):
        if random.random() < 0.25:
            attacker.life = attacker.heal() + attacker.life
            return
            #print("El",attacker.name,"se ha curado",attacker.heal(),"y ahora tiene",attacker.life)
        else:
            damage = attacker.attack()

    damage = attacker.attack()

    reduced_damage = defender.defend() # Calcular cuánto daño se reduce por la defensa del defensor
    damage_received = max(damage - reduced_damage, 0) # El daño reducido nunca puede ser mayor que el daño causado
    reduce_life(defender, damage_received)

    # Actualizar los resultados
    if attacker.get_name() not in resultados:
        resultados[attacker.get_name()] = {"clase": type(attacker).__name__,"victorias": 0,"daño_total": 0, "total_peleas":0}
    else:
        resultados[attacker.get_name()]["daño_total"] += damage_received
        resultados[attacker.get_name()]["total_peleas"] += 1

    if defender.get_name() not in resultados:
        resultados[defender.get_name()] = {"clase": type(attacker).__name__,"victorias": 0,"daño_total": damage_received, "total_peleas":0}
    else:
        resultados[attacker.get_name()]["total_peleas"] += 1

    # Comprobar si el defensor ha muerto
    if defender.life <= 0:
        defender.life = 0 #Esta muerto
        personajes.remove(defender) #Elmina al personaje de la lista en caso de morir
        print("El ganador es",attacker.get_name())

        # Actualizar los resultados
        if attacker.get_name() not in resultados:
            resultados[attacker.get_name()] = {"clase": type(attacker).__name__, "victorias": 1,"daño_total": damage_received}
        else:
            resultados[attacker.get_name()]["victorias"] += 1

        #Podríamos también crear una lista de muertos donde se vayan añadiendo los personajes muertos
        winner = attacker
        
        if isinstance(winner, Warrior):
            # Generar una nueva espada para el ganador
            if random.random() < 0.5:
                new_sword = generate_sword()
                equip(winner, new_sword)
            #else:
                #print(f"{winner.get_name()} no ha obtenido una nueva espada.")
            
            # Generar una nueva armadura para el ganador
            if random.random() < 0.5:
                    new_armor = generate_armor()
                    equip(winner, new_armor)
            #else:
                #print(f"{winner.get_name()} no ha obtenido una nueva armadura.")

            # Generar un nuevo escudo para el ganador
            if random.random() < 0.5:
                new_shield = generate_shield()
                equip(winner, new_shield)
            #else:
                #print(f"{winner.get_name()} no ha obtenido un nuevo escudo.")
        
        elif isinstance(winner, Caster):
            # Generar una nueva varita mágica para el ganador
            if random.random() < 0.5:
                new_wand = generate_wand()
                equip(winner, new_wand)
            #else:
                #print(f"{winner.get_name()} no ha obtenido una nueva varita mágica.")
        
            # Generar una nueva armadura para el ganador
            if random.random() < 0.5:
                new_armor = generate_armor()
                equip(winner, new_armor)
            #else:
                #print(f"{winner.get_name()} no ha obtenido una nueva armadura.")
                
        #print_remaining_characters(personajes) #Imprime la lista de personajes restantes
        #print("")
        #print(resultados)
            
    #else:
        #print("Fin de la batalla me voy corriendo a buscar a otros dos tipos")
        #En esta parte habría que volver a coger otros dos de la lista para que peleen


def reduce_life(self, damage):
        self.life -= damage
        if self.life <= 0:
            self.life = 0
            #print(f"{self.name} ha recibido {damage} puntos de daño y ahora tiene {self.life} puntos de vida")
            #print(f"{self.name} ha muerto")
        #else:
            #print(f"{self.name} ha recibido {damage} puntos de daño y ahora tiene {self.life} puntos de vida")



def equip(self, item):
        if isinstance(item, Sword) or isinstance(item, Wand):
            if self.weapon is None or item.power > self.weapon.power:
                self.weapon = item
                #print(f"{self.name} equipped {item.name} as a weapon!")
            #else:
                #print(f"{self.name} already has a more powerful weapon equipped!")
        elif isinstance(item, Armor):
            if self.armor is None or item.protection > self.armor.protection:
                self.armor = item
                #print(f"{self.name} equipped {item.name} as armor!")
            #else:
                #print(f"{self.name} already has more powerful armor equipped!")
        elif isinstance(item, Shield):
            if isinstance(self, Warrior):
                if self.shield is None or item.protection > self.shield.protection:
                    self.shield = item
                    #print(f"{self.name} equipped {item.name} as a shield!")
                #else:
                    #print(f"{self.name} already has a more powerful shield equipped!")
            #else:
                #print(f"{self.name} cannot equip a shield!")
        #else:
            #print(f"{item.name} is not a weapon or armor!")



def print_remaining_characters(personajes):
    print("Personajes restantes:")
    for character in personajes:
        if isinstance(character, Warrior):
            weapon_info = f", Arma: {character.weapon.name} (Poder: {character.weapon.power})" if character.weapon else ", Arma: None"
            armor_info = f", Armadura: {character.armor.name} (Defensa: {character.armor.protection})" if character.armor else ", Armadura: None"
            shield_info = f", Escudo: {character.shield.name} (Defensa: {character.shield.protection})" if character.shield else ", Escudo: None"
            print(f"{character.get_name()} ({type(character).__name__}), Vida: {character.life}, Fuerza: {character.strength}, Defensa: {character.defense}, Furia: {character.fury}{weapon_info}{armor_info}{shield_info}")
            
        elif isinstance(character, Caster):
            weapon_info = f", Arma: {character.weapon.name} (Poder: {character.weapon.power})" if character.weapon else ", Arma: None"
            armor_info = f", Armadura: {character.armor.name} (Defensa: {character.armor.protection})" if character.armor else ", Armadura: None"
            print(f"{character.get_name()} ({type(character).__name__}), Vida: {character.life}, Fuerza: {character.strength}, Defensa: {character.defense}, Maná: {character.mana}{weapon_info}{armor_info}")



#def print_remaining_characters(personajes):
    #print("Personajes restantes:")
    #for character in personajes:
        #print(f"{character.get_name()} ({type(character).__name__}), vida: {character.life}")


























#Funciones descartadas:

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