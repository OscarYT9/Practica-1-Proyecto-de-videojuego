from classes import *
from items import *
from combat import *

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

Racun = Mage("Racun", 100, 50, 25, 5 , None, None)
#sword.mostrar() #Muestra el Nombre y el poder del item
Thorfinn = Priest("Thorfinn", 5, 50, 25, 5 , None, None)

personajes=[Morthecaiser,Racun,Thorfinn]
combat(personajes)
#print(Morthecaiser.get_life())
#print(Racun.get_life())
combat(personajes)
#print(Morthecaiser.get_life())
#print(Racun.get_life())
combat(personajes)
#print(Morthecaiser.get_life())
#print(Racun.get_life())
combat(personajes)
#print(Morthecaiser.get_life())
#print(Racun.get_life())
combat(personajes)
#print(Morthecaiser.get_life())
#print(Racun.get_life())
combat(personajes)
#print(Morthecaiser.get_life())
#print(Racun.get_life())

#print(Racun.get_weapon())
if Racun.weapon is not None:
    print(Racun.weapon.mostrar())


combat(personajes)
#print(Thorfinn.get_life())
#print(Racun.get_life())
combat(personajes)
#print(Thorfinn.get_life())
#print(Racun.get_life())

#print(Racun.get_weapon())
if Racun.weapon is not None:
    print(Racun.weapon.mostrar())