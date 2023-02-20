
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
    def attack(self):
        import random
        return self.strength + self.weapon.power + random.randint(0,self.fury)
    def defend(self):
        return self.defense + self.armor.protection + self.shield.protection


class item:
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor

    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Valor: {self.valor}")

class arma(item):
    def __init__(self, nombre, valor, poder):
        super().__init__(nombre, valor)
        self.poder = poder

  # Método para mostrar el poder del arma
    def mostrar_poder(self):
        print(f"Poder: {self.poder}")

# Definir la subclase armadura que hereda de la clase item
class armadura(item):
  # Constructor de la subclase
  def __init__(self, nombre, valor, proteccion):
    # Llamar al constructor de la superclase
    super().__init__(nombre, valor)
    # Asignar el atributo adicional
    self.proteccion = proteccion

  # Método para mostrar la protección de la armadura
  def mostrar_proteccion(self):
    print(f"Protección: {self.proteccion}")

# Definir la subclase pocion que hereda de la clase item
class pocion(item):
  # Constructor de la subclase
  def __init__(self, nombre, valor, efecto):
    # Llamar al constructor de la superclase
    super().__init__(nombre, valor)
    # Asignar el atributo adicional
    self.efecto = efecto

  # Método para mostrar el efecto de la poción 
  def mostrar_efecto(self):
   print(f"Efecto: {self.efecto}")


#class Mage(Caster): 



#PRUEBAS
# Crear un objeto arma
espada = arma("Espada", 10, 5)

# Mostrar los atributos del objeto
espada.mostrar()
espada.mostrar_poder()

iron= armadura

Morthecaiser = Warrior("Morthecaiser", 100, 50, 25,espada,iron)

# Llamar al método get_name usando el operador punto
print(Morthecaiser.get_name())