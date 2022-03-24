# I M P O R T S
from CuentaBancaria import CuentaBancaria
from colorama import Fore


# C L A S E
# Creamos la subclase VIP que hereda de CuentaBancaria con sus atributos
class VIP(CuentaBancaria):  # Uso de la herencia, uso de los atributos de CuentaBancaria
    # que pueden ser modificados
    def __init__(self, id, titular, fecha, numerocuenta, saldo, negativo):
        CuentaBancaria.__init__(self, id, titular, fecha, numerocuenta, saldo)
        self.negativo = negativo
    # NUEVOS metodos que se añaden a esta clase aparte de los que heredamos oo cambiamos.
    # Cuando pagas con tarjeta en depende de que sitio el dinero no te lo quitan de la cuenta
    # al momentoo, es decir, el dinero lo retienen y por eso hay veces que pdoemos tenner
    # dinero que esté en negativoo ---> DINERO QUE REALMENTE NO TIENES
    # Por lo tanto se calculara TODO igualq ue en la clase CuentaBancaria pero teniendo en cuenta
    # realmente que hay que quitarle el dinero en NEGATIVO al saldo.
    def retirardinero(self, dinero):
        if(self.saldo+self.negativo >= dinero):
            self.saldo = self.saldo-dinero
        else:
            print(
                Fore.RED+"Error, el dinero a retirar está fuera de tu limite"+Fore.WHITE)

    def transferirdinero(self, dinero, cuenta):
        if (self.saldo+self.negativo >= dinero):
            self.saldo = self.saldo-dinero
            cuenta.saldo = cuenta.saldo+dinero
        else:
            print(
                Fore.RED+"Error, el dinero a transferir está fuera de tu limite" + Fore.WHITE)

    def cuenta(self):
        cuentastr = CuentaBancaria.cuenta(self)
        return cuentastr + " Cuenta VIP con limite negativo de " + str(self.negativo)
