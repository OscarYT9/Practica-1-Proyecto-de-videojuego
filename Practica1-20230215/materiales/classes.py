from items import *
from abc import ABC, abstractmethod
class Avatar:
    @abstractmethod
    def __init__(self, name, life, strength, defense, weapon, armor):
        self.name = name
        self.life = life
        self.strength = strength
        self.defense = defense
        self.weapon = None   #El arma, la armadura, y el escudo se inicializan en None
        self.armor = None
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_life(self):
        return self.life
    
    def set_life(self, life):
        self.life = life
        
    def get_strength(self):
        return self.strength

    def set_strength(self, strength):
        self.strength = strength

    def get_defense(self):
        return self.defense

    def set_defense(self, defense):
        self.defense = defense

    def get_weapon(self):
        return self.weapon

    def get_armor(self):
        return self.armor

    def set_armor(self, armor):
        self.armor = armor

    def attack(self):
        pass

    def defend(self):
        pass
    
    
    
class Melee(Avatar):
    @abstractmethod
    def __init__(self, name, life, strength, defense, weapon, armor, shield):
        super().__init__(name, life, strength, defense, weapon, armor)

        self.shield = None
        
    def get_shield(self):
        return self.shield

    def set_shield(self, shield):
        self.shield = shield

    def set_weapon(self,Item):
        self.weapon = Item


class Warrior(Melee): 
    def __init__(self, name, life, strength, defense, fury, weapon, armor, shield):
        super().__init__(name, life, strength, defense, weapon, armor, shield)
        
        self.fury = fury

    def get_fury(self):
        return self.fury
    
    def set_fury(self, fury):
        self.fury = fury

    def set_shield(self, shield):
        self.shield = shield

    def attack(self):
        import random
        if self.weapon is None:
            return self.strength + random.randint(0, self.fury)
        else:
            return self.strength + self.weapon.power + random.randint(0, self.fury)

    def defend(self):
        if (self.armor is None) and (self.shield is None):
            return self.defense
        elif self.armor is None:
            return self.defense + self.shield.protection
        elif self.shield is None:
            return self.defense + self.armor.protection
        else:
            return self.defense + self.armor.protection + self.shield.protection
#_______________________________________________________________________________________

class Caster(Avatar):
    @abstractmethod
    def __init__(self, name, life, strength, defense, mana, weapon, armor):
        super().__init__(name, life, strength, defense, weapon, armor)
        
        self.mana = mana

    def get_mana(self):
        return self.mana
    
    def set_mana(self,mana):
        self.mana = mana
        
    def set_weapon(self,Item):
        self.weapon = Item
        

class Mage(Caster):
    def __init__(self, name, life, strength, defense, mana, weapon, armor):
        super().__init__(name, life, strength, defense, mana, weapon, armor)

    def attack(self):
        import random
        aleatorio = random.randint(0,1)
        if aleatorio == 1:
            return aleatorio
        if aleatorio == 0:
            self.mana += 2
            print(f"{self.get_name()} ha recuperado 2 puntos de mana.")
        if self.mana > 1:
            if self.weapon is None:
                damage = self.strength
            else:
                damage = self.strength + self.weapon.power
            self.mana -= 1
            print(f"{self.get_name()} ha utilizado 1 punto de mana.")
            return damage
        else:
            print(f"{self.get_name()} no tiene suficiente mana para atacar.")
            return 1
        
            
    def defend(self):
        if self.armor is None:
            return self.defense
        else:
            return self.defense + self.armor.protection
            
#_______________________________________________________________________________________


class Priest(Caster):
    def __init__(self, name, life, strength, defense, mana, weapon, armor):
        super().__init__(name, life, strength, defense, mana, weapon, armor)

    def attack(self):
        import random
        aleatorio = random.randint(0,1)
        if aleatorio == 1:
            return aleatorio
        if aleatorio == 0:
            self.mana += 2
            print(f"{self.get_name()} ha recuperado 2 puntos de mana.")
        if self.mana > 1:
            if self.weapon is None:
                damage = self.strength
            else:
                damage = self.strength + self.weapon.power
            self.mana -= 1
            print(f"{self.get_name()} ha utilizado 1 punto de mana.")
            return damage
        else:
            print(f"{self.get_name()} no tiene suficiente mana para atacar.")
            return 1

    def defend(self):
        if self.armor is None:
            return self.defense
        else:
            return self.defense + self.armor.protection
        
    def heal(self):
        import random
        aleatorio = random.randint(0, 1)
        if aleatorio == 1:
            self.mana += 2
        
        if self.mana > 2:
            if self.weapon is None:
                curacion = (self.strength + self.attack()) // 2
            else:
                curacion = (self.strength + self.attack() + self.weapon.power) // 2
            self.mana -= 2
        else:
            curacion = 0
        
        return curacion