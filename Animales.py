
class Animal(): #Creacion de la clase Animal que nunca crea un objeto pq no 
                # se inicializa.
    # Superclase o clase base
    # Creación del coonstructor don su paramentro
    def __init__(self, name):
        self.name = name


class Mamifero(Animal):
    # Subclase que hereda da la clase base por esoo podemos usar el metodo super
    def __init__(self, name):
        super().__init__(self, name)


class Oviparo(Animal):
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
