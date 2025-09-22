def simulacion_vuelo():
    #------Entrada-----
    total_combustible = float(input("Ingrese total de combustible disponible (en unidades/min): "))
    consumo_crucero = float(input("Ingrese consumo en crucero (unidades/min): "))
    distancia_planificada = float(input("Ingrese la distancia planificada (km): "))
    velocidad_base = float(input("Ingrese la velocidad base (km/min): "))

    # --- Inicialización ---
    combustible = total_combustible
    tiempo = 0
    distancia_recorrida = 0

    alerta_mitad = False
    alerta_cuarto = False
    alerta_5min = False

    ASCENSO_MIN = 5
    DESCENSO_UMBRAL_MIN = 5

    # --- Bucle de simulación ---
    while combustible > 0 and distancia_recorrida < distancia_planificada:

        # Determinar fase de vuelo
        if tiempo < ASCENSO_MIN:
            consumo_actual = consumo_crucero * 1.20
        elif (distancia_planificada - distancia_recorrida) / velocidad_base <= DESCENSO_UMBRAL_MIN:
            consumo_actual = consumo_crucero * 0.85
        else:
            consumo_actual = consumo_crucero

        # Verificar si el combustible alcanza para menos de 1 minuto
        if combustible - consumo_actual < 0:
            tiempo_parcial = combustible / consumo_actual
            distancia_recorrida += velocidad_base * tiempo_parcial
            tiempo += tiempo_parcial
            combustible = 0
            break

        # Actualizar variables
        combustible -= consumo_actual
        distancia_recorrida += velocidad_base
        tiempo += 1

        # Alertas
        if not alerta_mitad and combustible <= total_combustible / 2:
            print(" Alerta: Queda la mitad del combustible")
            alerta_mitad = True

        if not alerta_cuarto and combustible <= total_combustible / 4:
            print(" Alerta: Queda un cuarto del combustible")
            alerta_cuarto = True

        if not alerta_5min and (combustible / consumo_actual) <= 5:
            print(" Alerta: Autonomía menor o igual a 5 minutos")
            alerta_5min = True

    # --- Resultados finales ---
    print("\n--- Resultados del vuelo ---")
    print("Tiempo total de vuelo:", round(tiempo, 2), "minutos")
    print("Distancia recorrida:", round(distancia_recorrida, 2), "km")

    if distancia_recorrida >= distancia_planificada:
        print(" El vuelo alcanzó el destino")
    else:
        print(" El vuelo no alcanzó el destino")


import random

# Función para asignar un número de asiento aleatorio
def asignar_asiento():
    return random.randint(1, 20)

# Función para devolver el tipo de asiento y su precio
def elegir_asiento(opcion):
    if opcion == 1:
        return "Asiento con artículo personal", 100
    elif opcion == 2:
        return "Asiento con equipaje de mano", 200
    elif opcion == 3:
        return "Asiento con equipaje de bodega", 300
    else:
        return None, 0

# Programa principal
def main():
    continuar = "S"
    compra_numero = 1
    resumen = ""      # Texto acumulado con todos los boletos
    total_pagar = 0   # Acumulador de precios
    total_boletos = 0 # Contador de boletos

    print("\n=== COMPRA DE BOLETOS DE AVIÓN ===")
    print(" Precios de los asientos:")
    print("1. Asiento con artículo personal - $100")
    print("2. Asiento con equipaje de mano   - $200")
    print("3. Asiento con equipaje de bodega - $300")

    while continuar.upper() == "S":
        print("\n--- NUEVA COMPRA ---")

        # Validación de opción hasta que elija correctamente
        tipo_asiento = None
        precio = 0
        while tipo_asiento is None:
            try:
                opcion = int(input("Elige el tipo de asiento (1-3): "))
                tipo_asiento, precio = elegir_asiento(opcion)
                if tipo_asiento is None:
                    print(" Opción no válida, intenta de nuevo.\n")
            except ValueError:
                print(" Debes ingresar un número válido.\n")

        # El asiento siempre lo asigna automáticamente el programa
        asiento = asignar_asiento()

        # Mostrar boleto actual
        print(f"\n Boleto {compra_numero}:")
        print(f"   Tipo de asiento: {tipo_asiento}")
        print(f"   Número de asiento asignado: {asiento}")
        print(f"   Precio: ${precio}")

        # Guardar en resumen
        resumen = resumen + f"Boleto {compra_numero}: {tipo_asiento} - Asiento {asiento} - Precio ${precio}\n"

        # Acumular totales
        total_pagar = total_pagar + precio
        total_boletos = total_boletos + 1
        compra_numero = compra_numero + 1

        continuar = input("\n¿Deseas comprar otro boleto? (S = Sí / N = No): ")

    # --- Resumen final ---
    print("\n Gracias por su compra. Resumen de boletos:")
    print(resumen)
    print(f"Total de boletos comprados: {total_boletos}")
    print(f"Precio final a pagar: ${total_pagar}")









