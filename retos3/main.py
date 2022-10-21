'''
3. El banco de hierro de la isla de Braavos necesita de sus servicios para programar un software que permita:

Almacenar información de un cliente (nombre,apellido,cedula)
Almacenar información de la cuenta (numeroCuenta, saldo)
Se debe permitir consultar saldo en cualquier momento
Se debe permitir ingresar o retirar dinero  cuando se desee

'''
from Cliente import Cliente
from Cuenta import Cuenta

# ------------------------------------------------------------
saldo = 1000
opcion = 10

print("***MENU***")
print("0. Salir")
print("1. Consignar")
print("2. Retirar")
print("3. Consultar Saldo")

while(opcion != 0):
    opcion = int( input("Digita una opcion: ") )
    if(opcion == 1):
        print("Consignar")
        nombres = input(f'Digite su nombre: ')
        apellidos = input(f'Digite su apellido: ')
        documento = input(f'Digite su cédula: ')

        cuenta = input(f'Digite el número de cuenta: ')

        ingreso = float(input(f'Digite el valor a consignar: '))

        saldo = saldo + ingreso

    elif(opcion == 2):
        nombres = input(f'Digite su nombre: ')
        apellidos = input(f'Digite su apellido: ')
        documento = input(f'Digite su cédula: ')

        cuenta = input(f'Digite el número de cuenta: ')

        print("Retirar")
        egreso = float(input(f'Digite el valor a retirar: '))

        saldo = saldo - egreso

    elif(opcion == 3):
        print(f'Tu saldo es: {saldo}')

    elif(opcion == 0):
        print("Salir")

    else:
        print("Seleccione opcion valida")
# else:
#     print("terminé")

# ------------------------------------------------------------

objeto_cliente = Cliente(nombres, apellidos, documento)

objeto_cuenta = Cuenta(cuenta, saldo)

# -----------------------------------------------------------

objeto_cuenta.consultarSaldo()

objeto_cliente.mostrarCliente()

objeto_cuenta.mostrarCuenta()


objeto_cuenta.ingresarDinero()

objeto_cuenta.retirarDinero()

# ------------------------------------------------------------