'''
funcion : menu 
parametro deentrada : ninguno 
ejecucion: imprimir 4 opciones dieferentes. soicitar que se elija una opcion y que la guarde en una variable.
valor de retonorno : opcion elegida
'''

def menu():
    opcion = int(input("1.Encabezado\n2. Porcentaje\n3. Mensaje\n4. salir\nElija una opcion(solo numero).\n  " ))
    return opcion 

def encabezado(mensaje):
    print("- Nombre: Anibal de Jesus\n- Apellido: Ipuana Ipuana.\n- Edad: 18 años.\n- Estatura: 1.66m.\n - ID: 000560610. ")
    print(mensaje)

def porcentaje(a,b):
    valor_de_porcentaje =  (a / b) * 100
    return valor_de_porcentaje

def 


eleccion = menu()
match(eleccion):
    case 1:
        encabezado(mensaje)
        #imprimir informacion sobre ustedes. 
        # Parametro: Mensaje que se imprima dentro de la funcion.
    case 2:
        pass
        # parametro 1: valor total
        # parametro 2: Porcentajee 
        # Retorno : valor de porcentaje 
    
    case 3:
        pass
        # no reciba ningun parametro y no devuelva un resultado 
        # imprime en panatlla un mensaje de cierre de programa 


