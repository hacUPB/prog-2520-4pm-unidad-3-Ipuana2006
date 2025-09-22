def suma(a, b):
	resultado = a + b
	return resultado

# crear una funcion que imprima la tabal de cualquier numero - bucle for

def tabla(num):
	for i in range(1,11):
		producto = i * num
		print(f'{num} * {i} = {producto}')

# esta funcon no tiene ningun valor de retorno 

#Llamando a la función
numero1 = 5
numero2 = 3
resultado_suma = suma(numero1, numero2)
print(f"{numero1} + {numero2} = {resultado_suma}")
print(suma(9898,564))
suma(45, 78)
# Llamando la funcion tabla 
numero =  int(input('Ingrese un valor: '))
var = tabla(numero) 





