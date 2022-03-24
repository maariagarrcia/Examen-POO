# NOS PIDEN LA RELACION que hay entre los 6 "objetos" que nos dan
# Todos los objetos que hay que crear son animales, por tanto MINIMO
# cada objeto va a heredar ATRIBUTOS de algun objeto
# ---> Todos los animales no son iguales cada unop tiene sus propias caracteristicas que hagan
# que se diferencien de ootros.
class Animal():  # Creacion de la clase Animal que nunca crea un objeto pq no
    # se inicializa.
    # Superclase o clase base
    # Creación del coonstructor don su paramentro
    def __init__(self, name):
        self.name = name


class Mamifero(Animal): # Un mamifero es un animal --> Hereda atributoos de Animal
                        # Hasta la propia descripcion de wikipedia nos dice que:
                        # Mamifero es una clase de animal
    # Subclase que hereda da la clase BASE por esoo podemos usar el metodo super
    def __init__(self, name):
        # Super nos permite acceder desde la subclase a metodos o atributos de la clase base.
        super().__init__(self, name)


class Oviparo(Animal): # Un oviparo es un animal  ---> Hereda caracteristicas  de ASnimal
    # Subclase que hereda da la clase base por eso podemos usar el metodo super
    def __init__(self, name):
        super().__init__(self, name)


class Gato(Mamifero):
    # Subclase que hereda de ptra clase
    def __init__(self, name):
        Mamifero.__init__(self, name)


class Ornitorrinco(Mamifero, Oviparo):
    # Subclase que hereda de ptra clase, herencia multiple
    def __init__(self, name):
        # No se puede usar super ya que no hereda de la clase base
        Mamifero.__init__(self, name)
        Oviparo.__init__(self, name)


class Pollo(Oviparo):
    # Subclase que hereda de ptra clase
    def __init__(self, name):
        Oviparo.__init__(self, name)

###
# I N I C I O   P R O G R A M A
###
# a = Animal("nomrbe")
# print(a.name)
