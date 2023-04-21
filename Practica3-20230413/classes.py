# Nombre del archivo: classes.py
# Autores: Óscar Vilela Rodríguez (oscar.vilela.rodriguez@udc.es), Guillermo García Engelmo (g.garcia2@udc.es)
class Libro:
    """
    Clase que representa un libro.

    Atributos
    ----------
    titulo : str
        Título del libro.
    autor : str
        Autor del libro.
    anio_edicion : int
        Año de edición del libro.
    prestamos_realizados : int
        Cantidad de veces que el libro ha sido prestado.

    Métodos
    -------
    get_titulo() -> str:
        Devuelve el título del libro.
    get_autor() -> str:
        Devuelve el autor del libro.
    get_anio_edicion() -> int:
        Devuelve el año de edición del libro.
    get_prestamos_realizados() -> int:
        Devuelve la cantidad de veces que el libro ha sido prestado.
    __repr__() -> str:
        Devuelve una representación en forma de cadena del objeto Libro.
    __ge__(other: Libro) -> bool:
        Compara dos libros y devuelve True si el libro actual es mayor o igual que el otro libro en orden alfabético por autor, título y año de edición. De lo contrario, devuelve False.
    __gt__(other: Libro) -> bool:
        Compara dos libros y devuelve True si el libro actual es mayor que el otro libro en orden alfabético por autor, título y año de edición. De lo contrario, devuelve False.
    """

    def __init__(self, titulo, autor, anio_edicion, prestamos_realizados):
        """
        Inicializa los atributos de un objeto Libro.

        Parameters
        ----------
        titulo : str
            Título del libro.
        autor : str
            Autor del libro.
        anio_edicion : int
            Año de edición del libro.
        prestamos_realizados : int
            Cantidad de veces que el libro ha sido prestado.

        Returns
        -------
        None
        """

        self.titulo = titulo
        self.autor = autor
        self.anio_edicion = anio_edicion
        self.prestamos_realizados = prestamos_realizados

    def get_titulo(self):
        """
        Devuelve el título del libro.

        Returns
        -------
        str
            El título del libro.
        """
        return self.titulo
    
    def get_autor(self):
        """
        Devuelve el autor del libro.

        Returns
        -------
        str
            El autor del libro.
        """
        return self.autor

    def get_anio_edicion(self):
        """
        Devuelve el año de edición del libro.

        Returns
        -------
        int
            El año de edición del libro.
        """
        return self.anio_edicion
    
    def get_prestamos_realizados(self):
        """
        Devuelve la cantidad de préstamos realizados del libro.

        Returns
        -------
        int
            La cantidad de préstamos realizados del libro.
        """
        return self.prestamos_realizados

    def __repr__(self):
        """
        Devuelve una representación del objeto Libro.

        Returns
        -------
        str
            Una representación del objeto Libro en forma de cadena.
        """
        return f"Libro('{self.titulo}', '{self.autor}', {self.anio_edicion}, {self.prestamos_realizados})"        

    def __eq__(self, other):
        """
        Compara dos libros y devuelve True si tienen el mismo título, autor y año de edición.
        De lo contrario, devuelve False.
        """
        if isinstance(other, Libro):
            return (self.titulo == other.titulo and 
                    self.autor == other.autor and 
                    self.anio_edicion == other.anio_edicion)
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
        if isinstance(other, Libro):
            return (self.autor.lower(), self.titulo.lower(), self.anio_edicion) >= (other.autor.lower(), other.titulo.lower(), other.anio_edicion)
        
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
        if isinstance(other, Libro):
            return (self.autor.lower(), self.titulo.lower(), self.anio_edicion) > (other.autor.lower(), other.titulo.lower(), other.anio_edicion)
        
        return NotImplemented