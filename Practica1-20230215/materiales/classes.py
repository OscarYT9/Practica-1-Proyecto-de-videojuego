from items import *
from abc import ABC, abstractmethod
class Avatar:
    """
    Clase abstracta que representa a un avatar.

    Attributes
    ----------
    name : str
        Nombre del avatar.
    life : int
        Vida actual del avatar.
    strength : int
        Fuerza del avatar.
    defense : int
        Defensa del avatar.
    weapon : Item
        Arma equipada del avatar.
    armor : Item
        Armadura equipada del avatar.

    Methods
    -------
    get_name()
        Devuelve el nombre del avatar.
    set_name(name: str)
        Establece el nombre del avatar.
    get_life()
        Devuelve la vida actual del avatar.
    set_life(life: int)
        Establece la vida actual del avatar.
    get_strength()
        Devuelve la fuerza del avatar.
    set_strength(strength: int)
        Establece la fuerza del avatar.
    get_defense()
        Devuelve la defensa del avatar.
    set_defense(defense: int)
        Establece la defensa del avatar.
    get_weapon()
        Devuelve el arma equipada del avatar.
    get_armor()
        Devuelve la armadura equipada del avatar.
    set_armor(armor: Item)
        Equipa una armadura al avatar.
    attack()
        Método abstracto que representa el ataque del avatar.
    defend()
        Método abstracto que representa la defensa del avatar.
    """
    @abstractmethod
    def __init__(self, name, life, strength, defense, weapon, armor):
        """
        Inicializa los atributos del avatar.

        Parameters
        ----------
        name : str
            Nombre del avatar.
        life : int
            Vida actual del avatar.
        strength : int
            Fuerza del avatar.
        defense : int
            Defensa del avatar.
        weapon : Item
            Arma equipada del avatar.
        armor : Item
            Armadura equipada del avatar.

        Returns
        -------
        None
        """
        self.name = name
        self.life = life
        self.strength = strength
        self.defense = defense
        self.weapon = None   #El arma, la armadura, y el escudo se inicializan en None
        self.armor = None
    
    def get_name(self):
        """
        Devuelve el nombre del avatar.

        Returns
        -------
        str
            El nombre del avatar.
        """
        return self.name
    
    def set_name(self, name):
        """
        Establece el nombre del avatar.

        Parameters
        ----------
        name : str
            Nuevo nombre del avatar.

        Returns
        -------
        None
        """
        self.name = name

    def get_life(self):
        """
        Devuelve la vida actual del avatar.

        Returns
        -------
        int
            La vida actual del avatar.
        """
        return self.life
    
    def set_life(self, life):
        """
        Establece la vida actual del avatar.

        Parameters
        ----------
        life : int
            Nueva vida actual del avatar.

        Returns
        -------
        None
        """
        self.life = life
        
    def get_strength(self):
        """
        Devuelve la fuerza del avatar.

        Returns
        -------
        int
            La fuerza del avatar.
        """
        return self.strength

    def set_strength(self, strength):
        """Establece la fuerza del avatar.

        Parameters
        ----------
        strength : int
            La fuerza del avatar.

        Returns
        -------
        None
        """
        self.strength = strength

    def get_defense(self):
        """Devuelve la defensa del avatar.

        Returns
        -------
        int
            La defensa del avatar.
        """
        return self.defense

    def set_defense(self, defense):
        """Establece la defensa del avatar.

        Parameters
        ----------
        defense : int
            La defensa del avatar.

        Returns
        -------
        None
        """
        self.defense = defense

    def get_weapon(self):
        """Devuelve el arma equipada del avatar.

        Returns
        -------
        str
            El arma del avatar.
        """
        return self.weapon

    def get_armor(self):
        """Devuelve la armadura equipada del avatar.

        Returns
        -------
        str
            La armadura del avatar.
        """
        return self.armor

    def set_armor(self, armor):
        """Establece la armadura del personaje.

        Parameters
        ----------
        armor : str
            La armadura del personaje.

        Returns
        -------
        None
        """
        self.armor = armor

    def attack(self):
        """Método abstracto que representa el ataque del avatar.

        Returns
        -------
        None
        """
        pass

    def defend(self):
        """Método abstracto que representa la defensa del avatar.

        Returns
        -------
        None
        """
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
            #print(f"{self.get_name()} ha recuperado 2 puntos de mana.")
        if self.mana > 1:
            if self.weapon is None:
                damage = self.strength
            else:
                damage = self.strength + self.weapon.power
            self.mana -= 1
            #print(f"{self.get_name()} ha utilizado 1 punto de mana.")
            return damage
        else:
            #print(f"{self.get_name()} no tiene suficiente mana para atacar.")
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
            #print(f"{self.get_name()} ha recuperado 2 puntos de mana.")
        if self.mana > 1:
            if self.weapon is None:
                damage = self.strength
            else:
                damage = self.strength + self.weapon.power
            self.mana -= 1
            #print(f"{self.get_name()} ha utilizado 1 punto de mana.")
            return damage
        else:
            #print(f"{self.get_name()} no tiene suficiente mana para atacar.")
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