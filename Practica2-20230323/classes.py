from abc import ABC, abstractmethod
import heapq

class Avion:
    def __init__(self, id, clase, time, departure):
        self.id = id
        self.clase = clase
        self.time = time
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

class PriorityQueue:
  def __init__(self):
      self._cola = []
      self._indice = 0
  
  def __len__(self):
    """Return the number of elements in the queue."""
    return len(self._cola)
    
  def push(self, elemento, prioridad):
      heapq.heappush(self._cola, (-prioridad, self._indice, elemento))
      self._indice += 1
    
  def pop(self):
      return heapq.heappop(self._cola)[-1]

  def remove(self, elemento):
      for i, (_, _, e) in enumerate(self._cola):
          if e == elemento:
              self._cola.pop(i)
              heapq.heapify(self._cola)
              return e
      raise ValueError(f"{elemento} is not in the queue")
  
  def __getitem__(self, index):
    """Return the element at the specified index."""
    if index < 0 or index >= self._size:
      raise IndexError('Index out of range')
    return self._data[(self._front + index) % len(self._data)]