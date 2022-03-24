#### I M P O R T S
from CuentaBancaria import CuentaBancaria, fechatostring, compararfechas

#### C L A S E
#  Una clase que hereda de otra puede añadir nuevos atributos,
# ocultarlos, añadir nuevos métodos o redefinirlos.
# LA PLANTILLA APlazoFijo tiene que tener en cuenta que --->
#       SI cuando extraes dinero estas un una fecha INCOORRECTA
#               ENTONCES ademas del dinero a retirar se penaliza con un 5% adicional.
#       SINO QUE DEVUELVA EL metodo creado  en cuenta bancaria que calculara el dinero que queda.
# Se define la clase APlazoFijo que hereda atributos de cuentabancaria
class APlazoFijo(CuentaBancaria):
    def __init__(self, id, titular, fecha, numerocuenta, saldo, vencimiento):
        CuentaBancaria.__init__(self, id, titular, fecha, numerocuenta, saldo)
        self.vencimiento = vencimiento
    # Cambia metodos de la clase base
    def retirardinero(self, dinero, fechaactual):
        if(compararfechas(fechaactual, self.vencimiento) < 0):
            dinero = dinero*1.05
        CuentaBancaria.retirardinero(self, dinero)

    def cuenta(self):
        cuentastr = CuentaBancaria.cuenta(self)
        # LO DEVUELVE
        return cuentastr + " Cuenta a plazo fijo con vencimento " + fechatostring(self.vencimiento)
