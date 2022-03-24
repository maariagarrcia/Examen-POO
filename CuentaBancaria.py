#### I M P O R T S
import random
from colorama import Fore


#### C L A S E

# Cuenta bancaria sera nuestar clase base
# Se crea la clase CuentaBancaria, es decir, una plantilla para posteriormente coon el costructor
# inicializarlo y crear el objeto.
# Cada objetoo tiene sus respectivas caracteristicas.

class CuentaBancaria():
    # Metodo constructor con sus parametros
    # Hay dos tipos de atributos:
    #           1) LOS DE INSTANCIA --->Pertenecen a la instancia de la clase o al objeto.
    #                                   Son atributos particulares de cada instancia, en nuestro caso de cada perro.

    #           2) LOS DE CLASES ---> Se trata de atributos que pertenecen a la clase, por
    #                                 lo tanto serán comunes para todos los objetos.

    # Los atributos de instancia para nuestra cuenta bancaria
    def __init__(self, id, titular, fecha, numerocuenta, saldo):
        self.id = id
        self.titular = titular
        self.fecha = fecha
        self.numerocuenta = numerocuenta
        self.saldo = saldo

    # Los métodos que permiten acceder al valor de un atributo se denominan "getters".
    # Los que dan y guardan el valor de un atributo se denominan "setters".
    # A partir de aqui empezamos a definirlos
    def setid(self, id):
        self.id = id

    def settitular(self, titular):
        self.titular = titular

    def setFecha(self, fecha):
        self.fecha = fecha

    def setnumerocuenta(self, numerocuenta):
        self.numerocuenta = numerocuenta

    def setsaldo(self, saldo):
        self.saldo = saldo

    def getid(self):
        return self.id

    def gettitular(self):
        return self.titular

    def getFecha(self):
        return self.fecha

    def getnumerocuenta(self):
        return self.numerocuenta

    def getsaldo(self):
        return self.saldo

    # Definimos unos cuantos metodos necesarios para esta clase
    def retirardinero(self, dinero):
        # El metodo que definimos quiere poder retirar dinero de una cuenta bancaria ----> HAY QUE TENER  EN CUENTA QUE:
        # SI el dinero que deseamos retirar es menor o igual que el que disponemos.
        #       ENTONCES al retirar dinero se recalculara el dinero de la cuenta bancaria.
        # SINO se pasará un mensaje de error ya que no se puede extraer un dinero que no se tiene
        if (self.saldo >= dinero):
            self.saldo = self.saldo-dinero
        else:
            print(Fore.RED + "Error, quiere retirar más dinero del que tienes"+Fore.WHITE)

    def ingresardinero(self, dinero):
        # El dinero que se ingresa en una cuenta bancaria se suma al que ya había --->  El saldo
        # actual CAMBIA ---> Despues de ingresar dinero hay que sumarselo al que  ya disponiamos.
        self.saldo = self.saldo+dinero

    def transferirdinero(self, dinero, cuenta):
        # Cuando tranferimos dinero lo retiramos de la cuenta ---> Pasa lo mismo que en el metodo retirardinero.
        # --->      SI nuestro dinero disminuye al que hagamos la  tranferencia aumentara, es decir, el dinero de la
        # cuenta bancaria de otra persona recalculará su saldo en su cuenta
        #           SINO  pasará igual que  en retirar dinero---> No  se puede extraer mas dinero del que no se tiene
        if (self.saldo >= dinero):
            self.saldo = self.saldo-dinero
            cuenta.saldo = cuenta.saldo+dinero
        else:
            print(
                Fore.RED + "Error, quiere transferir más dinero del que tienes" + Fore.WHITE)

    def cuenta(self):
        # Lo que va adevolver este metodo por pantalla cuandose inicialice
        return "Cuenta bancaria: " + Fore.GREEN + str(self.id) + Fore.WHITE + " Saldo: " + Fore.GREEN + str(self.saldo) + Fore.WHITE


def esBisiesto(año):
    # Para  que un año sea bisiesto (de la wikipedia):Año bisiesto es el divisible entre 4,
    # salvo que sea año secular -último de cada siglo, terminado en «00»-,
    # en cuyo caso también ha de ser divisible entre 400.
    # Se crea un codigo con coondiciones
    # POR LO TANTO PARA QUE UN AÑO SEA BISIESTO TENDRAN QUE PASAR DOS C0SAS--->
    #       SECULARES: QUE  SEA  MULTIPLO DE 4
    #       NO SECULARES: MULTIPLOS DE 400
    Bisiesto = False
    if(año % 4 == 0):
        if(año % 100 == 0):
            if(año % 400 == 0):
                Bisiesto = True
        else:
            Bisiesto = True
    return Bisiesto


def escribirfecha():
    # Se elige aleatooriamente una fecha
    año = random.randint(2021, 2050)
    mes = random.randint(1, 12)
    día = 0
    if(mes == 2):
        if(esBisiesto(año) == True):
            día = random.randint(1, 29)
        else:
            día = random.randint(1, 28)
    elif(mes == 4 or mes == 6 or mes == 9 or mes == 11):
        día = random.randint(1, 30)
    else:
        día = random.randint(1, 31)
    # La fecha se devuelve en forma de lista
    fecha = [año, mes, día]
    return fecha


def fechatostring(fecha):
    # Ordena la fecha y la devuelve
    return str(fecha[2])+"/"+str(fecha[1])+"/"+str(fecha[0])


def compararfechas(fecha1, fecha2):
    # SE EMPIEZAN A COMPARAR LAS FECHAS
    # En fechamenor comparamos dos fechas y se llega a la fecha menor
    # Por lo tanto añadimos la funcion que calcula el menoro entre esos dos
    #
    fecha3 = fechamenor(fecha1, fecha2)
    # SI fecha 1 es diferente que la menor ---> devuelve 1
    # PUES SI fecha 2 es diferente que fecha 3 ---> devuelve un -1
    # SINO DEVUELVE UN 0
    if(fecha1 != fecha3):
        return 1
    elif(fecha2 != fecha3):
        return -1
    else:
        return 0


def fechamenor(fecha1, fecha2):
    if(fecha1[0] > fecha2[0]):
        #mayor = fecha1
        menor = fecha2
    elif(fecha1[0] < fecha2[0]):
        #mayor = fecha2
        menor = fecha1
    else:
        if(fecha1[1] > fecha2[1]):
            #mayor = fecha1
            menor = fecha2
        elif(fecha1[1] < fecha2[1]):
            #mayor = fecha2
            menor = fecha1
        else:
            if(fecha1[2] > fecha2[2]):
                #mayor = fecha1
                menor = fecha2
            elif(fecha1[2] < fecha2[2]):
                #mayor = fecha2
                menor = fecha1
            else:
                #mayor = fecha1
                menor = fecha2
    return menor  # TE DEVUELVE LA MENOR FECHA ENTRE FECHA 1 Y FECHA 2


def crearnumero():
    numero = 0
    for i in range(0, 13):
        num = random.randint(0, 9)
        numero += num*10 ^ i
    return numero
