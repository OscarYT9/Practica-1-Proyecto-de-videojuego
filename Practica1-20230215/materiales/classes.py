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

    def set_shield(self, shield):
        self.shield = shield

    def attack(self):
        import random
        if self.weapon is None:
            return self.strength + random.randint(0, self.fury)
        else:
            return self.strength + self.weapon.power + random.randint(0, self.fury)

    def defend(self):
        if (self.weapon is None) or (self.shield is None):
            return self.defense
        else:
            return self.defense + self.armor.protection + self.shield.protection
#_______________________________________________________________________________________

class Caster(Avatar):
    @abstractmethod
    def __init__(self, name, life, strength, defense, weapon, armor, mana):
        super().__init__(name, life, strength, defense)
        
        self.mana = mana

    def get_mana(self):
        return self.mana
    
    def set_mana(self,mana):
        self.mana = mana
        
    def set_weapon(self,Item):
        self.weapon = Item
        

class Mage(Caster): 

    def attack(self):
        import random
        aleatorio = random.randint(0,1)
        return aleatorio
        if aleatorio == 0:
            self.mana += 2
        if self.mana > 1:
            return self.strength + self.weapon.power
        else:
            self.attack = 1
            
            
    def defense(self):
        return self.defense + self.weapon.value
            
#_______________________________________________________________________________________


class priest(Caster):
    def __init__(self, name, life, strength, defense, mana):
        super().__init__(name, life, strength, defense, mana)

    def attack(self):
        return super().attack()
    

