### Ejercicio 6

#Una compañía de paquetería internacional tiene servicio en algunos países según su zona. El costo por el servicio de paquetería se basa en el peso del paquete y la zona a la que va dirigido. Parte de su política implica que los paquetes con un peso superior a 5 kg no son transportados por seguridad. Usa la siguiente tabla para resolver el problema:


# | Zona | Ubicación | Costo/gramo |
# | --- | --- | --- |
# | 1 | América del Norte | $11 |
# | 2 | América Central | $10 |
# | 3 | América del Sur | $12 |
# | 4 | Europa | $24 |
# | 5 | Asia | $27 |

# Solución

print("\nIngrese la zona de envío, Elija un numero\n")
zona = int(input("1.Norteamérica\n2. Centroamérica\n3. Suramérica\n4. Europa\n5. Asia\nElija un numero : "))
peso = float(input("Ingrese peso del paquete en gramos: "))

if zona > 0 and zona < 6:
    if 0 < peso <= 5000:
        match zona:
            case 1:
                total = peso * 11
                print(f"El envio de su paquete cueta ${total}")
            case 2:
                total = peso * 10
                print(f"El envio de su paquete cueta ${total}")
            case 3:
                total = peso * 12
                print(f"El envio de su paquete cueta ${total}")
            case 4:
                total = peso *  24
                print(f"El envio de su paquete cueta ${total}")
            case _:
                total = peso * 27
                print(f"El envio de su paquete cueta ${total}")
    else:
        print("No se pueden enviar paquetes de mas de 5Kg")
else:
    print("Zona inválida debe estar entre 1 y 5")

           