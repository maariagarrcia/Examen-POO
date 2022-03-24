##### I M P O R T S

from APlazoFijo import APlazoFijo
import CuentaBancaria
from VIP import VIP
import random
from colorama import *

##### C L A S E
# Creacion de una cuenta que refleje una cuenta bancaria
# Para poder crear la plantilla CreadorCuenta hay que tener en cuenta
# las ACCIONES QUE POODEMOS REALIZAR eN ELLA :
#           - Tranferir dinero
#           - Ingresar dinero
#           - Retirar dinero, entre otras....
# Hay que tener en curnta que en algunas cuentas bancarias hay que retirar "x" dinero antes de un dia fijado,
# es decir, antes de la fecha de vencimiento (EXPLICADO  EN SU RESPECTIVA CLASE),QUE SEAN ALEATORIAS LAS FECHAS.
# Además a esta cuenta le añadiremos  que tenga  una atributo adicional: EL POSIBLE
# DINERO EN NEGATIVO --->  En las cuentas Vip uno podrá tener saldo negativo siempre que no supere este valor.

# Por lo tanto vemso que es NECESARIO EL USO DE LA HERENCIA ya qu emuchas veces hay que
# reutilizar codigoo y hacer unos pequeñps cambios.

class CreadorCuenta():
    # __id ---> Recibe como argumento un objeto y retorna otro objeto que sirve como
    # identificador único para el primero. Devuelve un ENTERO
    __id = 1
    # Metodo constructor
    def __init__(self, tipodeCuenta, titular): 
        # CUANDO ES NONE NO HACE FALTA PASARLO POR PARAMETRO
        self.cuenta = None
        fecha1 = CuentaBancaria.escribirfecha()
        fecha2 = CuentaBancaria.escribirfecha()
        self.fecha = CuentaBancaria.fechamenor(fecha1, fecha2)
        if(self.fecha == fecha1):
            self.vencimiento = fecha2
        else:
            self.vencimiento = fecha1
        self.numerocuenta = CuentaBancaria.crearnumero()
        self.saldo = 10000
        self.negativo = random.randint(1, self.saldo/8)
        if(tipodeCuenta == "CuentaBancaria"):
            self.cuenta = CuentaBancaria.CuentaBancaria(
                CreadorCuenta.__id, titular, self.fecha, self.numerocuenta, self.saldo)
        elif(tipodeCuenta == "APlazoFijo"):
            self.cuenta = APlazoFijo(
                CreadorCuenta.__id, titular, self.fecha, self.numerocuenta, self.saldo, self.vencimiento)
        elif(tipodeCuenta == "VIP"):
            self.cuenta = VIP(CreadorCuenta.__id, titular, self.fecha,
                              self.numerocuenta, self.saldo, self.negativo)
        CreadorCuenta.__id += 1


###
#  I N I C I O    P R O G R A M A
###

# Instanciar la clase CreadorCuenta
Cuenta1 = CreadorCuenta("CuentaBancaria", "Paco")
Cuenta2 = CreadorCuenta("APlazoFijo", "Benito")
Cuenta3 = CreadorCuenta("VIP", "Sparrow")


print(Cuenta1.cuenta.cuenta())
print(Cuenta2.cuenta.cuenta())
print(Cuenta3.cuenta.cuenta())
Cuenta1.cuenta.transferirdinero(2000, Cuenta2.cuenta)
Cuenta2.cuenta.transferirdinero(2000, Cuenta3.cuenta)
Cuenta1.cuenta.ingresardinero(575)
Cuenta2.cuenta.ingresardinero(575)
Cuenta3.cuenta.ingresardinero(575)
Cuenta1.cuenta.retirardinero(78)


print("Saldo de la cuenta 1 es " + Fore.GREEN +
      str(Cuenta1.cuenta.getsaldo()) + Fore.WHITE)
print("Saldo de la cuenta 2 es " + Fore.GREEN +
      str(Cuenta2.cuenta.getsaldo()) + Fore.WHITE)
print("Saldo de la cuenta 3 es "+Fore.GREEN +
      str(Cuenta3.cuenta.getsaldo()) + Fore.WHITE)
Cuenta3.cuenta.retirardinero(Cuenta3.cuenta.saldo+Cuenta3.cuenta.negativo+1)
print("Saldo de la cuenta 3 es "+Fore.GREEN +
      str(Cuenta3.cuenta.getsaldo()) + Fore.WHITE)
Cuenta3.cuenta.retirardinero(Cuenta3.cuenta.saldo+Cuenta3.cuenta.negativo)
print("Saldo de la cuenta 3 es "+Fore.GREEN +
      str(Cuenta3.cuenta.getsaldo()) + Fore.WHITE)
fecha2 = [Cuenta2.cuenta.vencimiento[0]-1,
          Cuenta2.cuenta.vencimiento[1], Cuenta2.cuenta.vencimiento[2]]
Cuenta2.cuenta.retirardinero(1000, fecha2)
print("Saldo de la cuenta 2 es "+Fore.GREEN +
      str(Cuenta2.cuenta.getsaldo()) + Fore.WHITE)
fecha2 = [Cuenta2.cuenta.vencimiento[0]+1,
          Cuenta2.cuenta.vencimiento[1], Cuenta2.cuenta.vencimiento[2]]
Cuenta2.cuenta.retirardinero(1000, fecha2)
print("Saldo de la cuenta 2 es "+Fore.GREEN +
      str(Cuenta2.cuenta.getsaldo()) + Fore.WHITE)
