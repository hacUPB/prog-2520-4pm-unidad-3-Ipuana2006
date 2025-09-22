'''
for i in range(5,20,3):
    print(i)
'''

'''
for i in range(0,-21,-1):
    print(i)
'''
'''
mensaje = "Programacion en Python"
numero = int(input('Ingrese numero: '))
for i in range(numero):
    print(mensaje)
'''

'''
# Ejercicio 2
Escribe un programa que solicite al usuario ingresar un número entero positivo n. 
Luego, utiliza un bucle for con la función range() para calcular la suma de todos los números pares desde 1 hasta n.
'''
n = int(input('Ingrese un numero entero positivo:'))
acumulador = 0

for i in range(n+1):
    if  i  % 2 == 0:
        acumulador += i # tipo de variable: acumulador

print(f' La suma de los pares hasta {n} es {acumulador}')
    
