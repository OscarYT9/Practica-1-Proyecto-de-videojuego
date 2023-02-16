
from abc import ABC, abstractmethod
class Avatar:
    @abstractmethod
    def __init__(self, name, life, strength, defense, weapon, armor):
        self.name = name
        self.life = life
        self.strength = strength
        self.defense = defense
        self.weapon = None
        self.armor = None
    
    def get_name(self):
        return self.name
    
    def set_name(self, name):
        self.name = name

    def get_life(self):
        return self.life
    
    def set_life(self):
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
    def __init__(self, name, life, strength, defense):
        super().__init__(name, life, strength, defense)
        self.weapon = Sword(0)

    def attack(self):
        return self.strength + self.weapon.value

class Caster(Avatar):
    @abstractmethod
    def __init__(self, name, life, strength, defense):
        super().__init__(name, life, strength, defense)
        self.weapon = Wand(0)

    def attack(self):
        return self.strength + self.weapon.value

class Warrior(Melee):

class Mage(Caster):
    