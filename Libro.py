#### C L A S E
# Se define una clase Libro, es  decir, una plantilla para la  psoteriior creación del objetoo cuando
# se instancie.
# Una clase es una estructura general del objeto. Por ejemplo, puede 
# decir que la clase Libro necesita tener una titulo, un autor, una fecha y 
# un editorial, un ISBN, pero no va a decir cual es titulo, un autor, una fecha y 
# un editorial, un ISBN, es aquí donde entran las instancias,
# que haran que salgan cuales son, pq lo pasas por parametro. 

class Libro():  # Declaramos la clase Libro su la plantilla ya que 
                #  hasta que no lo instanciemos no se creará el objeto/instancia
    def __init__(self, titulo, autor, fecha, editorial, ISBN):  # Definimos los parámetros, atributos que son particulares para cada objeto creado con esa clase.
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
#l = Libro("titulo", "autor", "fecha", "editorial", "ISBN")

# l.setAutor("After")
# l.setAutor("Anna Ted")
# l.setAutor("febrero del 2000")
# l.setAutor("Burbuja")
# l.setAutor("9486426538")


