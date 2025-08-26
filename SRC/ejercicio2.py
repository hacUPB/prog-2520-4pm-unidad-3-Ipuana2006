# Determinar si un número es par o impar 

# leer numero
numero = int(input("Ingrese un número entero: "))
residuo = numero % 2 
# si residuo es cero es par 
if residuo == 0:
    print(numero, "es par")
else:
    print(numero, "es impar")
    