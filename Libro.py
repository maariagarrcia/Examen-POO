# C L A S E
# Se define una clase Libro, es  decir, una plantilla para la  psoteriior creación del objetoo cuando
# se instancie.

class Libro():  # Declaramos la clase Libro, la platilla.
    def __init__(self, titulo, autor, fecha, editorial, ISBN):  # Definimos los parámetros en el constructor
        self.titulo = titulo
        self.autor = autor
        self.fecha = fecha
        self.editorial = editorial
        self.ISBN = ISBN

    # Los getters y  setters se utilizan en POO
    # para garantizar el principio de la encapsulación de datos.
    # Setters: dar un valor y guardarlo en el objeto
    # Los métodos que permiten acceder al valor de un atributo se denominan "getters".

    def setTitulo(self, titulo):
        self.titulo = titulo

    def setAutor(self, autor):
        self.autor = autor

    def setFecha(self, fecha):
        self.fecha = fecha

    def setEditorial(self, editorial):
        self.editorial = editorial

    def setISBN(self, ISBN):
        self.ISBN = ISBN

    def getTitulo(self):
        return self.titulo

    def getAutor(self):
        return self.autor

    def getFecha(self):
        return self.fecha

    def getEditorial(self):
        return self.editorial

    def getISBN(self):
        return self.ISBN

# Probar si funciona a la hora de instanciarlo
# l = Libro("Marrón", "claro", "Golden retriever", 1, 4)

# l.setAutor("Yo")

# print(l.autor)
