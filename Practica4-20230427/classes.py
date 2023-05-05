class Activity:
    """
    Clase que representa una actividad.

    Atributos
    ----------
    name : str
        Nombre de la actividad.
    duration : int
        Duración de la actividad en minutos.
    participation : int
        Número de participantes en la actividad.
    total_price_activity : float
        Precio total de la actividad.
    cost_per_participate : float
        Precio por participante de la actividad.

    Métodos
    -------
    get_name() -> str:
        Devuelve el nombre de la actividad.
    set_name(name: str):
        Asigna un nombre a la actividad.
    get_duration() -> int:
        Devuelve la duración de la actividad en minutos.
    set_duration(duration: int):
        Asigna una duración en minutos a la actividad.
    get_participation() -> int:
        Devuelve el número de participantes en la actividad.
    set_participation(participation: int):
        Asigna un número de participantes a la actividad.
    get_total_price_activity() -> float:
        Devuelve el precio total de la actividad.
    set_total_price_activity(total_price_activity: float):
        Asigna un precio total a la actividad.
    get_cost_per_participate() -> float:
        Devuelve el precio por participante de la actividad.
    set_cost_per_participate(cost_per_participate: float):
        Asigna un precio por participante a la actividad.
    """
    def __init__(self, name, duration, participation, total_price_activity, cost_per_participate):
        """
        Inicializa los atributos de un objeto Activity.

        Parameters
        ----------
        name : str
            El nombre de la actividad.
        duration : int
            Duración en minutos de la actividad.
        participation : int
            La cantidad de participantes de la actividad.
        total_price_activity : float
            El precio total de la actividad.
        cost_per_participate : float
            El costo por participante de la actividad.

        Returns
        -------
        None
        """
        self.name =name
        self.duration = duration
        self.participation = participation
        self.total_price_activity = total_price_activity
        self.cost_per_participate = cost_per_participate

    def get_name(self):
        """
        Devuelve el nombre de la actividad.

        Returns
        -------
        str
            El nombre de la actividad.
        """
        return self.name
    
    def set_name(self, name):
        """
        Establece el nombre de la actividad.

        Parameters
        ----------
        name : str
            El nuevo nombre de la actividad.

        Returns
        -------
        None
        """
        self.name = name
    
    def get_duration(self):
        """
        Devuelve la duración de la actividad en horas.

        Returns
        -------
        float
            La duración de la actividad en horas.
        """
        return self.duration
    
    def set_duration(self, duration):
        """
        Establece la duración de la actividad en horas.

        Parameters
        ----------
        duration : float
            La nueva duración de la actividad en horas.

        Returns
        -------
        None
        """
        self.duration = duration
    
    def get_participation(self):
        """
        Devuelve el número de participantes de la actividad.

        Returns
        -------
        int
            El número de participantes de la actividad.
        """
        return self.participation
    
    def set_participation(self, participation):
        """
        Establece el número de participantes de la actividad.

        Parameters
        ----------
        participation : int
            El nuevo número de participantes de la actividad.

        Returns
        -------
        None
        """
        self.participation = participation
    
    def get_total_price_activity(self):
        """
        Devuelve el precio total de la actividad.

        Returns
        -------
        float
            El precio total de la actividad.
        """
        return self.total_price_activity
    
    def set_total_price_activity(self, total_price_activity):
        """
        Establece el precio total de la actividad.

        Parameters
        ----------
        total_price_activity : float
            El nuevo precio total de la actividad.

        Returns
        -------
        None
        """
        self.total_price_activity = total_price_activity
    
    def get_cost_per_participate(self):
        """
        Devuelve el costo por participante de la actividad.

        Returns
        -------
        float
            El costo por participante de la actividad.
        """
        return self.cost_per_participate
    
    def set_cost_per_participate(self, cost_per_participate):
        """
        Establece el costo por participante de la actividad.

        Parameters
        ----------
        cost_per_participate : float
            El nuevo costo por participante de la actividad.

        Returns
        -------
        None
        """
        self.cost = cost_per_participate
        
    def __str__(self):
        return f"({self.duration} min, {self.participation} participantes, ${self.total_price_activity})"
    
    def __eq__(self, other):
        """
        Compara los costes y devuelve True si tienen el mismo coste.
        De lo contrario, devuelve False.
        """
        if isinstance(other, Activity):
            return (self.cost_per_participate == other.cost_per_participate)
        return False

    def __ge__(self, other):
        """
        Compara dos objetos Libro por su autor, título y año de edición.

        Parameters
        ----------
        other : Libro
            El otro objeto Libro con el que se va a comparar.

        Returns
        -------
        bool or NotImplemented
            True si el objeto actual es mayor o igual que el otro objeto Libro en términos de autor, título y año de edición;
            False en caso contrario;
            NotImplemented si el objeto no es del tipo Libro.
        """
        if isinstance(other, Activity):
            return (self.cost_per_participate >= other.cost_per_participate)
        
        return NotImplemented
    
    def __gt__(self, other):
        """
        Compara dos objetos Libro por su autor, título y año de edición.

        Parameters
        ----------
        other : Libro
            El otro objeto Libro con el que se va a comparar.

        Returns
        -------
        bool or NotImplemented
            True si el objeto actual es mayor que el otro objeto Libro en términos de autor, título y año de edición;
            False en caso contrario;
            NotImplemented si el objeto no es del tipo Libro.
        """
        if isinstance(other, Activity):
            return (self.cost_per_participate > other.cost_per_participate)
        
        return NotImplemented

