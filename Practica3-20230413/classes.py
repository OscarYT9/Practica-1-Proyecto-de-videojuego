class Libro:
    def __init__(self, titulo, autor, anio_edicion, prestamos_realizados):
        self.titulo = titulo
        self.autor = autor
        self.anio_edicion = anio_edicion
        self.prestamos_realizados = prestamos_realizados

    def __ge__(self, other):
        if isinstance(other, Libro):
            return (self.anio_edicion, self.titulo) >= (other.anio_edicion, other.titulo)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Libro):
            return self.anio_edicion > other.anio_edicion
        return NotImplemented