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
  """Error attempting to access an element from an empty container."""
  pass

class ArrayQueue:
  """FIFO queue implementation using a Python list as underlying storage."""
  DEFAULT_CAPACITY = 10          # moderate capacity for all new queues

  def __init__(self):
    """Create an empty queue."""
    self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
    self._size = 0
    self._front = 0

  def __len__(self):
    """Return the number of elements in the queue."""
    return self._size

  def is_empty(self):
    """Return True if the queue is empty."""
    return self._size == 0

  def first(self):
    """Return (but do not remove) the element at the front of the queue.
    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    return self._data[self._front]

  def dequeue(self):
    """Remove and return the first element of the queue (i.e., FIFO).

    Raise Empty exception if the queue is empty.
    """
    if self.is_empty():
      raise Empty('Queue is empty')
    answer = self._data[self._front]
    self._data[self._front] = None         # help garbage collection
    self._front = (self._front + 1) % len(self._data)
    self._size -= 1
    return answer

  def enqueue(self, e):
    """Add an element to the back of queue."""
    if self._size == len(self._data):
      self._resize(2 * len(self._data))     # double the array size
    avail = (self._front + self._size) % len(self._data)
    self._data[avail] = e
    self._size += 1

  def _resize(self, cap):                  # we assume cap >= len(self)
    """Resize to a new list of capacity >= len(self)."""
    old = self._data                       # keep track of existing list
    self._data = [None] * cap              # allocate list with new capacity
    walk = self._front
    for k in range(self._size):            # only consider existing elements
      self._data[k] = old[walk]            # intentionally shift indices
      walk = (1 + walk) % len(old)         # use old size as modulus
    self._front = 0                        # front has been realigned
  
  def __getitem__(self, index):
    """Return the element at the specified index."""
    if index < 0 or index >= self._size:
      raise IndexError('Index out of range')
    return self._data[(self._front + index) % len(self._data)]

  def remove_element(self, e):
      """Elimina la primera ocurrencia del elemento e de la cola."""
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

  def enqueue_front(self, e):
      """Add an element to the front of queue."""
      if self._size == len(self._data):
          self._resize(2 * len(self._data))     # double the array size
      self._front = (self._front - 1) % len(self._data)
      self._data[self._front] = e
      self._size += 1

  def insert(self, index, e):
    """Inserta un elemento en la posición index de la cola."""
    if index < 0 or index > self._size:
        raise IndexError('Index out of range')

    if self._size == len(self._data):
        self._resize(2 * len(self._data))

    i = (self._front + index) % len(self._data)
    for j in range(self._size, index, -1):
        self._data[(self._front + j) % len(self._data)] = self._data[(self._front + j - 1) % len(self._data)]

    self._data[i] = e
    self._size += 1

