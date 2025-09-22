# Juego de Adivinar el numero

# import random
from random import randint
'''
Variable de Entrada
Nombre     Tipo
numero      int

Variable de salida
intentos   int     contador

Variable de control
numero    int 
'''

#numero_aelatorio = random.randint(0,50)
numero_aleatorio = randint(1,100)

intentos = 0
# numero = -1 # Obliga a entrar al while la primnera vez 

while True:
    numero = int(input("Adivina el número oculto entre 1 y 100: "))
    intentos += 1
    if numero > numero_aleatorio:
        print('Tu número es menor')
    elif numero < numero_aleatorio:
        print('Tu número es mayor')
    else:
        print('Felicidades adivinaste el numero')
        break

print(f'Adivinaste en {intentos} intentos')
