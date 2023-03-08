class Item:
    """Clase base para todos los objetos del juego."""
    pass
#_______________________________________________________________________________________

class Weapon(Item):
    """Clase base para las armas del juego.

    Attributes
    ----------
    name : str
        El nombre del arma.
    power : int
        El poder del arma.

    Methods
    -------
    get_power()
        Devuelve el poder del arma.
    set_power(power)
        Establece el poder del arma a un nuevo valor.
    """
    def __init__(self, name, power):
        """Inicializa una instancia de la clase Weapon.

        Parameters
        ----------
        name : str
            El nombre del arma.
        power : int
            El poder del arma.

        Returns
        -------
        None
        """
        self.name = name
        self.power = power

    def get_power(self):
        """
        Devuelve el poder del arma.

        Returns
        -------
        int
            El poder del arma.
        """
        return self.power

    def set_power(self, power):
        """Establece el poder del arma a un nuevo valor.

        Parameters
        ----------
        power : int
            El nuevo valor de poder.

        Returns
        -------
        None
        """
        self.power = power


class Sword(Weapon):
    """Clase que representa una espada en el juego.

    Attributes
    ----------
    name : str
        El nombre de la espada.
    power : int
        El poder de la espada.

    Methods
    -------
    get_power()
        Devuelve el poder de la espada.
    set_power(power)
        Establece el poder de la espada a un nuevo valor.
    """
    swords = []
    
    def __init__(self, name, power):
        """
        Inicializa una instancia de la clase Sword.
        
        Parameters:
        ----------
        name : str
            El nombre de la espada.
        power : int
            La potencia de la espada.
        
        Returns:
        -------
        None
        """
        super().__init__(name, power)
        Sword.swords.append(self)




class Wand(Weapon):
    """Clase que representa una varita en el juego.

    Attributes
    ----------
    name : str
        El nombre de la varita.
    power : int
        El poder de la varita.

    Methods
    -------
    get_power()
        Devuelve el poder de la varita.
    set_power(power)
        Establece el poder de la varita a un nuevo valor.
    """
    wands = []

    def __init__(self, name, power):
        """
        Inicializa una instancia de la clase Wand.
        
        Parameters:
        ----------
        name : str
            El nombre de la varita.
        power : int
            El poder de la varita.
        
        Returns:
        -------
        None
        """
        super().__init__(name,power)
        self.name = name
        self.power = power
        Wand.wands.append({'name': self.name, 'power': self.power})
        


#_______________________________________________________________________________________

class Covering(Item):
    """Clase base para los objetos que pueden ser equipados para proteger al personaje.

    Attributes
    ----------
    name : str
        El nombre del objeto defensivo.
    protection : int
        La cantidad de protección que proporciona el objeto.

    Methods
    -------
    get_protection()
        Devuelve la cantidad de protección del objeto.
    set_protection(protection)
        Establece la cantidad de protección del objeto a un nuevo valor.
    """
    def __init__(self, name, protection):
        """
        Inicializa una instancia de la clase Covering.

        Parameters:
        ----------
        name : str
            El nombre del objeto defensivo.
        protection : int
            La protección del objeto defensivo.

        Returns:
        -------
        None
        """
        self.name = name
        self.protection = protection

    def get_proteccion(self):
        """
        Devuelve la protección del objeto defensivo.

        Returns:
        -------
        int
            La protección del objeto defensivo.
        """
        return self.protection

    def set_proteccion(self, protection):
        """
        Establece una nueva protección al objeto defensivo.

        Parameters:
        ----------
        protection : int
            La nueva protección del objeto defensivo.

        Returns:
        -------
        None
        """
        self.protection = protection
    

class Armor(Covering):
    """Clase para las armaduras del juego.

    Attributes
    ----------
    name : str
        El nombre de la armadura.
    protection : int
        La protección que proporciona la armadura.

    Methods
    -------
    get_protection()
        Devuelve la protección que proporciona la armadura.
    set_protection(protection)
        Establece la protección que proporciona la armadura a un nuevo valor.
    mostrar()
        Muestra la información de la armadura.
    get_name()
        Devuelve el nombre de la armadura.
    """
    armors = []

    def __init__(self, name,  protection):
        """
        Inicializa una instancia de la clase Armor.

        Parameters:
        ----------
        name : str
            El nombre de la armadura.
        protection : int
            La protección de la armadura.

        Returns:
        -------
        None
        """
        super().__init__(name, protection)

        self.protection = protection




class Shield(Covering): #Solo los Warriors pueden tener escudo
    """Clase para los escudos del juego.

    Attributes
    ----------
    name : str
        El nombre del escudo.
    protection : int
        La protección que proporciona el escudo.

    Methods
    -------
    get_protection()
        Devuelve la protección que proporciona el escudo.
    set_protection(protection)
        Establece la protección que proporciona el escudo a un nuevo valor.
    mostrar()
        Muestra la información del escudo.
    get_name()
        Devuelve el nombre del escudo.
    """
    shields = []

    def __init__(self, nombre, protection):
        """
        Inicializa una instancia de la clase Shield.

        Parameters:
        ----------
        nombre : str
            El nombre del escudo.
        protection : int
            La protección del escudo.

        Returns:
        -------
        None
        """
        super().__init__(nombre, protection)

        self.protection = protection



