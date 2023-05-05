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
        Compara el costo por participante de esta actividad con otra actividad
        y devuelve True si tienen el mismo costo. De lo contrario, devuelve False.

        Parameters
        ----------
        other : Activity
            La otra actividad con la que se comparará el costo.

        Returns
        -------
        bool
            True si ambos tienen el mismo costo por participante, False de lo contrario.

        Raises
        ------
        ValueError
            Si el objeto comparado no es una actividad.
        """
        if isinstance(other, Activity):
            return self.cost_per_participate == other.cost_per_participate
        else:
            raise ValueError('Segundo objeto no es una actividad')
    
    def __ne__(self, other):
        """
        Compara el costo por participante de esta actividad con otra actividad
        y devuelve True si tienen diferentes costos. De lo contrario, devuelve False.

        Parameters
        ----------
        other : Activity
            La otra actividad con la que se comparará el costo.

        Returns
        -------
        bool
            True si ambos tienen diferentes costos por participante, False de lo contrario.

        Raises
        ------
        ValueError
            Si el objeto comparado no es una actividad.
        """

        if isinstance(other, Activity):
            return self.cost_per_participate != other.cost_per_participate
        else:
            raise ValueError('Segundo objeto no es una actividad')

    
    def __gt__(self, other):
        """
        Compara el costo por participante de esta actividad con otra actividad
        y devuelve True si el costo de esta actividad es mayor que el costo de la otra actividad.
        De lo contrario, devuelve False.

        Parameters
        ----------
        other : Activity
            La otra actividad con la que se comparará el costo.

        Returns
        -------
        bool
            True si el costo de esta actividad es mayor que el costo de la otra actividad, False de lo contrario.

        Raises
        ------
        ValueError
            Si el objeto comparado no es una actividad.
        """
        
        if isinstance(other, Activity):
            return self.cost_per_participate > other.cost_per_participate
        else:
            raise ValueError('Segundo objeto no es una actividad')


    def __lt__(self, other):
        """
        Compara el costo por participante de esta actividad con otra actividad
        y devuelve True si el costo de esta actividad es menor que el costo de la otra actividad.
        De lo contrario, devuelve False.

        Parameters
        ----------
        other : Activity
            La otra actividad con la que se comparará el costo.

        Returns
        -------
        bool
            True si el costo de esta actividad es menor que el costo de la otra actividad, False de lo contrario.

        Raises
        ------
        ValueError
            Si el objeto comparado no es una actividad.
        """
        
        if isinstance(other, Activity):
            return self.cost_per_participate < other.cost_per_participate
        else:
            raise ValueError('Segundo objeto no es una actividad')

    def __le__(self, other):
        """
        Compara el costo por participante de esta actividad con otra actividad
        y devuelve True si el costo de esta actividad es menor o igual al costo de la otra actividad.
        De lo contrario, devuelve False.

        Parameters
        ----------
        other : Activity
            La otra actividad con la que se comparará el costo.

        Returns
        -------
        bool
            True si el costo de esta actividad es menor o igual al costo de la otra actividad, False de lo contrario.

        Raises
        ------
        ValueError
            Si el objeto comparado no es una actividad.
        """
        if isinstance(other, Activity):
            return self.cost_per_participate <= other.cost_per_participate
        else:
            raise ValueError('Segundo objeto no es una actividad')

def __ge__(self, other):
        """
        Compara el costo por participante de esta actividad con otra actividad
        y devuelve True si el costo de esta actividad es mayor o igual al costo de la otra actividad.
        De lo contrario, devuelve False.

        Parameters
        ----------
        other : Activity
            La otra actividad con la que se comparará el costo.

        Returns
        -------
        bool
            True si el costo de esta actividad es mayor o igual al costo de la otra actividad, False de lo contrario.

        Raises
        ------
        ValueError
            Si el objeto comparado no es una actividad.
        """
        if isinstance(other, Activity):
            return self.cost_per_participate >= other.cost_per_participate
        else:
            raise ValueError('Segundo objeto no es una actividad')

