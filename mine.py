""" Codificar un programa en Python utilizando funciones que permita
recibir: Nombre, edad, País, Equipo y tiempo en minutos de
múltiples ciclistas. El software estará en la capacidad de calcular y
mostrar en pantalla cual fue el ciclista más rápido
Recomendaciones: Programar menú (1. Agregar ciclista, 2. Ver
resultados) +2  """


opcion = 10

print("***MENU***")
print("0. Salir")
print("1. Agregar ciclista")
print("2. Ver resultados")


ciclistas = []



while (opcion != 0):
    opcion = int(input("Digita una opcion: "))
    if (opcion == 1):
        ciclista = {}
        ciclista['nombre'] = input("Digite el nombre: ")
        ciclista['edad'] = input("Digite la edad: ")
        ciclista['pais'] = input("Digite el pais: ")
        ciclista['equipo'] = input("Digite el equipo: ")
        ciclista['tiempo'] = int(input("Digite el tiempo del ciclista: "))

        ciclistas.append(ciclista)

        print('Ciclista guardado exitosamente')

        print("***MENU***")
        print("0. Salir")
        print("1. Agregar ciclista")
        print("2. Ver resultados")

    elif (opcion == 2):
        ciclistaMenor = ciclistas[0]
        
        for cicli in ciclistas:

            if cicli['tiempo'] < ciclistaMenor['tiempo']:
                ciclistaMenor=cicli
        


        print(f'El ciclista más rápido es: {ciclistaMenor}')

        print("***MENU***")
        print("0. Salir")
        print("1. Agregar ciclista")
        print("2. Ver resultados")


    elif (opcion == 0):
        print("Salir")

    else:
        print("Seleccione opcion valida")
