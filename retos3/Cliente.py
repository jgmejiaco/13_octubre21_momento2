'''
3. El banco de hierro de la isla de Braavos necesita de sus servicios para programar un software que permita:

Almacenar información de un cliente (nombre,apellido,cedula)
Almacenar información de la cuenta (numeroCuenta, saldo)
Se debe permitir consultar saldo en cualquier momento
Se debe permitir ingresar o retirar dinero  cuando se desee
'''

class Cliente:
    def __init__(self, nombredado, apellidodado, ceduladada):
        self.nombre = nombredado,
        self.apellido = apellidodado,
        self.cedula = ceduladada

    def mostrarCliente(self):
        print(f'Hola cliente {self.nombre + self.apellido}, su cédula es: {self.cedula}')
        