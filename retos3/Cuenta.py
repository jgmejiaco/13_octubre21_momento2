'''
3. El banco de hierro de la isla de Braavos necesita de sus servicios para programar un software que permita:

Almacenar información de un cliente (nombre,apellido,cedula)
Almacenar información de la cuenta (numeroCuenta, saldo)
Se debe permitir consultar saldo en cualquier momento
Se debe permitir ingresar o retirar dinero cuando se desee
'''

class Cuenta:
    def __init__(self, numeroCuentaDada, saldoDado):
        self.numeroCuenta = numeroCuentaDada,
        self.saldo = saldoDado

    def mostrarCuenta(self):
        print(f'Su cuenta es: {self.numeroCuenta}')

    def consultarSaldo (self):
        print(f'El saldo consultado es: {self.saldo}')

    def ingresarDinero (self):
        print(f'El dinero ingresado es: ')

    def retirarDinero (self):
        print(f'El dinero retirado es: ')