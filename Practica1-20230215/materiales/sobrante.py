#personajes_info = []
#victorias=0
#victorias+=1
#personajes_info.append([winner.name, winner.__class__.__name__, winner.life, winner.attack(),victorias])
#print("Lista con los nombres de los personajes: ",personajes_info)




#print_remaining_characters(personajes) #Imprime la lista de personajes restantes
        #print("")
        #print(resultados)



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



#def create_warrior(name, life, strength, protection, fury):
    #weapon, armor, shield = None, None, None
    #return Warrior(name, life, strength, protection, fury, weapon, armor, shield)

#def create_mage(name, life, strength, protection, mana):
    #weapon, armor = None, None
    #return Mage(name, life, strength, protection, mana, weapon, armor)

#def create_priest(name, life, strength, protection, mana):
    #weapon, armor = None, None
    #return Priest(name, life, strength, protection, mana, weapon, armor)




for personaje in x:
        peleas_participadas = resultados[personaje.get_name()]["total_peleas_atacante"]
        daño_medio = resultados[personaje.get_name()]["daño_total"] / peleas_participadas if peleas_participadas > 0 else 0
        print(f"{personaje.get_name()} causó un daño medio de {daño_medio} en {peleas_participadas} peleas.")

    # Calcular la media de los daños totales
    total_danos = [resultados[p]["daño_total"] for p in resultados]
    media_danos = sum(total_danos) / len(total_danos)

    # Calcular la desviación típica
    desviacion_tipica = math.sqrt(sum((x - media_danos)**2 for x in total_danos) / len(total_danos))

    print(f"La desviación típica de los daños totales es: {desviacion_tipica:.2f}")


















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