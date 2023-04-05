# Nombre del archivo: classes.py
# Autores: Óscar Vilela Rodríguez (oscar.vilela.rodriguez@udc.es), Guillermo García Engelmo (g.garcia2@udc.es)
from abc import ABC, abstractmethod

class Avion:
    """
    Clase abstracta que representa a un avión.

    Attributes
    ----------
    id : str
        Identificación del avión.
    clase : str
        Clase del avion.
    time : int
        Tiempo de entrada en pista del avión.
    departure : int
        Tiempo de despegue del avión.

    Methods
    -------
    get_id()
        Devuelve la identificación del avión.
    set_id(id: str)
        Establece la identificación del avión.
    get_clase()
        Devuelve la clase de vuelo del avion.
    set_clase(clase: int)
        Establece la la clase de vuelo del avión.
    get_time()
        Devuelve el tiempo de entrada en pista del avión.
    set_time(time: int)
        Establece el tiempo de entrada en pista del avión.
    get_departure()
        Devuelve el timepo de despegue del avión.
    set_departure(departure: int)
        Establece el tiempo de despegue del avión.
    """
    def __init__(self, id, clase, time, departure):
        """
        Inicializa los atributos del avatar.

        Parameters
        ----------
        id : str
            identificación del avión.
        clase : int
            clase del avión.
        time : int
            tiempo de entrada en pista del avión.
        departure : int
            tiempo de despegue del avión.

        Returns
        -------
        None
        """
        self.id = id
        self.clase = clase
        self.time = time
        self.departure = departure

    def get_id(self):
        """
        Devuelve la identificación del avión.

        Returns
        -------
        str
            La identificación del avión.
        """
        return self.id

    def get_clase(self):
        """
        Devuelve la clase del avión.

        Returns
        -------
        str
            La clase del avión.
        """
        return self.clase

    def get_time(self):
        """
        Devuelve el tiempo de entrada en pista del avión.

        Returns
        -------
        int
            El tiempo de entrada en pista del avión.
        """
        return self.time

    def set_time(self, time):
        """
        Establece el tiempo de entrada en pista del avión.

        Returns
        -------
        int
            Nuevo tiempo de entrada en pista del avión.
        """
        self.time = time

    def get_departure(self):
        """
        Devuelve el tiempo de despegue del avión.

        Returns
        -------
        int
            El tiempo de despegue del avión.
        """
        return self.departure

    def set_departure(self, departure):
        """
        Establece el tiempo de despegue del avión.

        Returns
        -------
        int
            Nuevo tiempo de despegue del avión.
        """
        self.departure = departure


#_____________________________________________________________________________________________________________________________________________
class Empty(Exception):
    """
    Error que ocurre cuando se intenta acceder a un elemento de un contenedor vacío.
    
    """
    pass

class ArrayQueue:
    """Implementación de una cola FIFO utilizando una lista de Python como almacenamiento subyacente."""
    DEFAULT_CAPACITY = 10          # capacidad moderada para todas las nuevas colas

    def __init__(self):
        """
        Crea una cola vacía
        
        Parameters
        ----------
        data : int
            longitud de la cola por defecto.
        size : int
            numero de elementos de la cola.
        front : int
            primera posición de la cola.
            

        Returns
        -------
        None
            
        """
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):
        """
        Devuelve la longitud de la cola.

        Returns
        -------
        int
            longitud de la cola.
        
        """
        return self._size

    def is_empty(self):
        """
            Devuelve si la cola esta vacia o no.

        Returns
        -------
        bool
            True or False.
        """
        
        return self._size == 0

    def first(self):
        """
        Devuelve el elemento de la primera posción de la cola primera posción de la cola.

        Returns
        -------
        str
            El elemento de la primera posción de la cola o lanza la excepción Empty si la cola está vacía.
        """
        if self.is_empty():
            raise Empty('La cola está vacía')
        return self._data[self._front]
    
    def _resize(self, cap):                  
        """
        
        Redimensiona a una nueva lista de capacidad >= len(self)
        
        Returns
        -------
        None
        """
        
        old = self._data                       
        self._data = [None] * cap              
        walk = self._front
        for k in range(self._size):            
            self._data[k] = old[walk]            
            walk = (1 + walk) % len(old)         
        self._front = 0 

    def dequeue(self):
        """
        Elimina y devuelve el primer elemento de la cola.

        Returns
        -------
        str
            el primer elemento de la cola o lanza la excepción Empty si la cola está vacía.
        """
        if self.is_empty():
            raise Empty('La cola está vacía')
        answer = self._data[self._front]
        self._data[self._front] = None         
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        """
        Agrega un elemento al final de la cola.

        Returns
        -------
        None
        """
        if self._size == len(self._data):
            self._resize(2 * len(self._data))     
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1         

    def __getitem__(self, index):
        """
        Devuelve el elemento en el índice especificado.

        Returns
        -------
            elemento del índice indicado
        
        """
        if index < 0 or index >= self._size:
            raise IndexError('Index out of range')
        return self._data[(self._front + index) % len(self._data)]

    def remove_element(self, e):
        """
        Elimina la primera ocurrencia del elemento e de la cola

        Returns
        -------
        None
        """
        for i in range(self._size):
            if self._data[(self._front + i) % len(self._data)] == e:
                # Se encontró el elemento
                for j in range(i, self._size - 1):
                # Desplazar los elementos restantes hacia la izquierda
                    self._data[(self._front + j) % len(self._data)] = self._data[(self._front + j + 1) % len(self._data)]
                self._data[(self._front + self._size - 1) % len(self._data)] = None
                self._size -= 1
                return
        # El elemento no se encontró
        raise ValueError('Elemento no encontrado')
    


