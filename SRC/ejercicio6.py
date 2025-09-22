### Ejercicio 6

#Una compañía de paquetería internacional tiene servicio en algunos países según su zona. El costo por el servicio de paquetería se basa en el peso del paquete y la zona a la que va dirigido. Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados por seguridad. Usa la siguiente tabla para resolver el problema:


# | Zona | Ubicación | Costo/gramo |
# | --- | --- | --- |
# | 1 | América del Norte | $11 |
# | 2 | América Central | $10 |
# | 3 | América del Sur | $12 |
# | 4 | Europa | $24 |
# | 5 | Asia | $27 |

##solucion
print("Ingrese la zona de envío, Elija un numero")
zona = int(input("1.Norteamérica\n2. Centroamérica\n3. Suramérica\n4. Europa\n5. Asia\nElija un numero : "))
if zona >= 1 and zona <= 5:
    peso = float(input("Ingrese peso del paquete en gramos: "))
    if peso <= 5000:
        if zona == 1:
            total = peso * 11
        elif zona == 2:
            total = peso * 10
        elif zona == 3:
            total = peso * 12
        elif zona == 4:
            total = peso * 24
        elif zona == 5:
            total = peso * 27
        print(f"El envío de su paquete cuesta ${total}")
    else:
        print("No se pueden enviar paquetes de mas de 5Kg")
else:
    print("La zona ingresada no existe.")




