'''
2. Codificar un programa en Python utilizando funciones lamba que permita: recibir 2 números y devolver  
 
1 → si el primer número es mayor que el segundo 
-1→ si el primer número es menor que el segundo 
 
Después una segunda función debe recibir el 1 o el -1 retornado por la función 1 y mostrar un mensaje  
 
Si recibe 1 → Debe indicar que el primer número es mayor 
Si recibe -1 → Debe indicar que el segundo número es mayor

Usar operador ternario +1
'''

mayorMenor = lambda num1,num2: ( 1 if num1 > num2 else -1 )

total = mayorMenor(100, 10)


def funcion2(): return print("El primer número es mayor que el segundo") if total == 1 else print(
    "El segundo número es mayor que el primero")

funcion2()