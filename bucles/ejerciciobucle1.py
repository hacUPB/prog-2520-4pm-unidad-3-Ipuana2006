'''
#numero = 1
# while numero <= 5:
    #print(numero)
    #numero += 1      #numero = numero + 1
'''
# imprimir los numeros pares entre el 20 y el 8o incluidos 
'''
#numero = 20
#while numero <= 80:
    #print(numero)
    #numero += 2
'''
# imprimir los numeros impares entre 99 y 61, en ordenn acedente.

'''
numero = 99
while numero >= 61:
    print(numero)
    numero -= 2
'''

# solicitar dos numeros al usuario e imprimir los numeros impares entre ellos 
'''
 
numero1 = int(input('Ingresar numero 1: '))
numero2 = int(input('Ingresar numero 2: '))

if numero1 > numero2:
    mayor = numero1
    menor = numero2
else:
    mayor = numero2
    menor = numero1

while menor <= mayor:
    if menor & 2 == 1:
        print(menor)
    menor += 1

'''
# Imprimir los multiplos de 7  entre 0 y 100
'''
numero = 0
while numero <= 100:
    if numero %  7 == 0:
        print(numero)
    numero += 1

'''
# solucitar un numero al usuario e imprimir su tabla de multiplicar hasta 15.
'''
numero = int(input('Ingrese uun número: '))
numero1 = 1
while numero1 <= 15:
    M = numero * numero1
    print(f'{numero} x {numero1} = {m}')
    numero1 += 1 
'''
# 

    




