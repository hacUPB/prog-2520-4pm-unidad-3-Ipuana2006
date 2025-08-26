# Caalcular el indice de masa corporal
# INC = peso / estatura **2
#leer estatura 
estatura = input("Ingrese estatura en m: ")
estatura = float(estatura)
# leer peso
peso = input("Ingrese su peso en Kg: ")
peso = float(peso)
#calcular IMC
IMC  = peso / estatura ** 2
# mostrar IMC
if IMC <= 18.48:
    print("Peso bajo")
elif IMC <= 24.99:
    print("peso normal")
elif IMC <= 29.9:
    print("sobrepeso")
elif IMC <= 39.9:
    print("obesidad")
else:
    print("obecidad extrema")


#Tarea
'''
crear un archivo .md
crear las suguientes tablas:
- operadores aritméticos 
- operadores relacionales 
- tipos de datos en python

'''


