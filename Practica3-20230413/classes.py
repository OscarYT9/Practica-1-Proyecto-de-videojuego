class Libro:
    def __init__(self, titulo, autor, anio_edicion, prestamos_realizados):
        self.titulo = titulo
        self.autor = autor
        self.anio_edicion = anio_edicion
        self.prestamos_realizados = prestamos_realizados

    def __repr__(self):
        return f"Libro('{self.titulo}', '{self.autor}', {self.anio_edicion}, {self.prestamos_realizados})"

    def __ge__(self, other):
        if isinstance(other, Libro):
            return (self.anio_edicion, self.autor, self.titulo) >= (other.anio_edicion, other.autor, other.titulo)
        return NotImplemented
    
    def __gt__(self, other):
        if isinstance(other, Libro):
            return (self.anio_edicion, self.autor, self.titulo) > (other.anio_edicion, other.autor, other.titulo)
        return NotImplemented