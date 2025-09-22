








# Problema: Simulación de autonomía de un avión ligero

Se desea diseñar un programa en Python que simule la autonomía de combustible de un avión ligero durante un vuelo planificado.

## **Entradas requeridas por el usuario**

- Cantidad total de combustible disponible en el avión (en litros).

- Consumo de combustible por minuto en condiciones de crucero (en litros/min).

- Distancia total planificada del vuelo (en kilómetros).

- Velocidad media del avión en condiciones de crucero (en km/min).

## Reglas de la simulación
### 1. Consumo dinámico (según la fase del vuelo)

- Ascenso: durante los primeros 5 minutos, el consumo aumenta en un 20% respecto al consumo de crucero.

- Crucero: se mantiene el consumo normal ingresado por el usuario.

- Descenso: en los últimos 5 minutos antes de llegar al destino, el consumo disminuye en un 15%.

### 2. Alertas obligatorias durante el vuelo

- El sistema debe mostrar alertas en los siguientes casos:

- Cuando el combustible restante sea igual o menor a la mitad del total.

- Cuando el combustible restante sea igual o menor a la cuarta parte del total.

- Cuando la autonomía restante sea de 5 minutos o menos.

### 3. Resultado final

Al terminar la simulación, el programa debe mostrar:

- Si el avión logró completar la distancia planificada o si se quedó sin combustible antes.

- El tiempo total de vuelo alcanzado (en minutos).

- La distancia total recorrida (en km).

- Todas las alertas registradas durante el vuelo.

# Tabla de análisis del problema


## Constantes
| Constante            | Descripción                                       | Unidad | Valor sugerido |
|----------------------|---------------------------------------------------|--------|----------------|
| `ASCENSO_MIN`        | Minutos de fase de ascenso con mayor consumo      | min    | 5              |
| `DESCENSO_UMBRAL_MIN`| Minutos antes del destino considerados descenso   | min    | 5              |

---

## Variables de entrada
| Variable              | Descripción                                | Unidad      |
|-----------------------|--------------------------------------------|-------------|
| `total_combustible`   | Cantidad total de combustible disponible   | litros (L)  |
| `consumo_crucero`     | Consumo de combustible en crucero          | litros/min  |
| `distancia_planificada` | Distancia total que se desea recorrer     | km          |
| `velocidad_base`      | Velocidad promedio del avión en crucero    | km/min      |

---

## Variables de proceso
| Variable              | Descripción                                                       | Unidad      |
|-----------------------|-------------------------------------------------------------------|-------------|
| `combustible`         | Combustible restante durante la simulación                        | litros (L)  |
| `tiempo`              | Tiempo acumulado de vuelo                                         | minutos     |
| `distancia_recorrida` | Distancia acumulada recorrida                                     | km          |
| `consumo_actual`      | Consumo que se aplica en el minuto según la fase (ascenso, crucero, descenso) | litros/min |
| `tiempo_parcial`      | Tiempo fraccionado en el último minuto si el combustible no alcanza| minutos     |

---

## Variables de salida
| Variable              | Descripción                                   | Unidad  |
|-----------------------|-----------------------------------------------|---------|
| `tiempo_total`        | Tiempo total de vuelo alcanzado               | minutos |
| `distancia_final`     | Distancia recorrida hasta agotar combustible  | km      |
| `estado_vuelo`        | Mensaje: si alcanzó el destino o no           | -       |

---

## Fórmulas utilizadas

1. **Autonomía total (sin fases de vuelo):**
   ```
   A = total_combustible / consumo_crucero

   ```
2. **Consumo en ascenso:**
   ```
    consumo_actual = consumo_crucero * 1.20
   ```
3. **Consumo en descenso:**
   ```
    consumo_actual = consumo_crucero * 0.85
   ```

4. **Combustible restante por minuto:**
   ```
    combustible = combustible - consumo actual
   ```
5. **Distancia recorrida por minuto:**
   ```
    distancia_recorrida = distancia_recorrida + velicidad_base
   ```

6. **Tiempo total:**
   ```
    tiempo = tiempo +1
   ```

7. **Último minuto (cuando el combustible no alcanza un minuto completo):**
   ```
    tiempo_ parcial = combustible / consumo_actual
   ```
   ```
    distancia_reccorrida = distancia_recorrida + (velociddad_base * tiempo_parcial)
   ```
   ```
    tiempo = tiempo + tiempo_parcial
   ```
 

## Pseudocódigo
```
INICIO

LEER total_combustible
LEER consumo_crucero
LEER distancia_planificada
LEER velocidad_base

        # --- Inicialización de variables ---
        combustible = total_combustible
        tiempo = 0
        distancia_recorrida = 0

        alerta_mitad = FALSO
        alerta_cuarto = FALSO
        alerta_5min = FALSO
        ASCENSO_MIN = 5 # min 
        DESCENSO_UMBRAL_MIN = 5 # min

        # --- Bucle de simulación ---
        MIENTRAS combustible > 0 Y distancia_recorrida < distancia_planificada HACER

            # --- Determinar fase de vuelo ---
            SI tiempo < ASCENSO_MIN ENTONCES
                consumo_actual = consumo_crucero * 1.20
            SINO SI (distancia_planificada - distancia_recorrida) / velocidad_base ≤ DESCENSO_UMBRAL_MIN ENTONCES
                consumo_actual = consumo_crucero * 0.85
            SINO
                consumo_actual = consumo_crucero
            FIN SI

            # --- Verificar si queda combustible para menos de 1 minuto ---
            SI combustible - consumo_actual < 0 ENTONCES
                tiempo_parcial = combustible / consumo_actual
                distancia_recorrida = distancia_recorrida + velocidad_base * tiempo_parcial
                tiempo = tiempo + tiempo_parcial
                combustible ← 0
                SALIR DEL BUCLE
            FIN SI

            # --- Actualizar variables ---
            combustible = combustible - consumo_actual
            distancia_recorrida ← distancia_recorrida + velocidad_base
            tiempo = tiempo + 1

            # --- Alertas ---
            SI alerta_mitad = FALSO Y combustible ≤ total_combustible / 2 ENTONCES
                MOSTRAR " Alerta: Queda la mitad del combustible"
                alerta_mitad = VERDADERO
            FIN SI

            SI alerta_cuarto = FALSO Y combustible ≤ total_combustible / 4 ENTONCES
                MOSTRAR " Alerta: Queda un cuarto del combustible"
                alerta_cuarto = VERDADERO
            FIN SI

            SI alerta_5min = FALSO Y (combustible / consumo_actual) ≤ 5 ENTONCES
                MOSTRAR " Alerta: Autonomía menor o igual a 5 minutos"
                alerta_5min ← VERDADERO
            FIN SI

        FIN MIENTRAS

        # --- Resultados finales ---
        MOSTRAR "Tiempo total de vuelo: ", tiempo, " minutos"
        MOSTRAR "Distancia recorrida: ", distancia_recorrida, " km"

        SI distancia_recorrida ≥ distancia_planificada ENTONCES
            MOSTRAR "El vuelo alcanzó el destino"
        SINO
            MOSTRAR " El vuelo no alcanzó el destino"
        FIN SI

    FIN FUNCIÓN

FIN


```
- **prueba de escritorio**
![alt text](<prueba de escritorio.jpg>)


# Problema: Compra de Boletos de Avión

##  Enunciado
Diseñar un programa en Python que simule la **compra de boletos de avión**.  
El usuario podrá elegir entre tres tipos de asiento:

1. **Asiento con artículo personal** – $100  
2. **Asiento con equipaje de mano** – $200  
3. **Asiento con equipaje de bodega** – $300  

Cada vez que el usuario compre un boleto:  
- El programa le asignará automáticamente un **número de asiento aleatorio entre 1 y 20** (el usuario no lo elige).  
- Se mostrará el tipo de asiento, el número asignado y el precio.  

El usuario podrá seguir comprando hasta que decida finalizar.  
Al terminar, el programa debe mostrar un **resumen de compra**, indicando:  
- Los boletos adquiridos.  
- El tipo de asiento elegido.  
- El número de asiento asignado automáticamente.  
- El precio total a pagar.  

---

# Tabla de analisis del problema

## Variables de Entrada
| Nombre         | Tipo de dato | Descripción                                     |
|----------------|--------------|-------------------------------------------------|
| opcion         | Entero       | Opción del usuario para elegir tipo de asiento  |
| continuar      | Cadena       | Indica si el usuario sigue comprando (S/N)      |

## Variables de Salida
| Nombre         | Tipo de dato | Descripción                                     |
|----------------|--------------|-------------------------------------------------|
| resumen        | Texto        | Acumulación de todos los boletos comprados      |
| total_pagar    | Entero       | Precio total de todos los boletos comprados     |
| total_boletos  | Entero       | Cantidad total de boletos comprados             |

## Variables de Proceso
| Nombre         | Tipo de dato | Descripción                                     |
|----------------|--------------|-------------------------------------------------|
| compra_numero  | Entero       | Número consecutivo de cada boleto               |
| tipo_asiento   | Cadena       | Tipo de asiento según la opción elegida         |
| precio         | Entero       | Precio del tipo de asiento elegido              |
| asiento        | Entero       | Número de asiento asignado automáticamente      |

## Constantes
| Nombre                | Tipo de dato | Descripción                                |
|-----------------------|--------------|--------------------------------------------|
| PRECIO_PERSONAL       | Entero       | Precio del asiento con artículo personal = 100 |
| PRECIO_MANO           | Entero       | Precio del asiento con equipaje de mano = 200   |
| PRECIO_BODEGA         | Entero       | Precio del asiento con equipaje de bodega = 300 |
| RANGO_ASIENTOS        | Rango        | Rango de números de asientos (1 a 20)           |

## Ecuaciones
## 1. Acumulación del precio total

Cada boleto comprado suma al precio total:
```
total_pagar = total_pagar + precio
```
##  2. Conteo de boletos

Cada vez que se compra un boleto, se incrementa el contador:
```
total_boletos = total_boletos + 1
```
## 3. Construcción del resumen de compra

El resumen se va formando concatenando texto:
```
resumen = resumen + "Boleto N: Tipo - Asiento - Precio"
```

## Pseudocódigo
```

INICIO

    MOSTRAR "=== COMPRA DE BOLETOS DE AVIÓN ==="
    MOSTRAR "1. Asiento con artículo personal - $100"
    MOSTRAR "2. Asiento con equipaje de mano   - $200"
    MOSTRAR "3. Asiento con equipaje de bodega - $300"

    compra_numero = 1
    total_boletos = 0
    total_pagar = 0
    resumen = ""   # texto acumulado
    continuar = "S"

    MIENTRAS continuar = "S" HACER

        tipo_asiento = NULO
        precio = 0

        REPETIR
            MOSTRAR "Elige el tipo de asiento (1-3): "
            LEER opcion

            SI opcion = 1 ENTONCES
                tipo_asiento = "Asiento con artículo personal"
                precio ← 100
            SINO SI opcion = 2 ENTONCES
                tipo_asiento = "Asiento con equipaje de mano"
                precio ← 200
            SINO SI opcion = 3 ENTONCES
                tipo_asiento = "Asiento con equipaje de bodega"
                precio = 300
            SINO
                MOSTRAR " Opción inválida, intenta de nuevo"
            FIN SI
        HASTA QUE tipo_asiento ≠ NULO

        asiento ← número aleatorio entre 1 y 20

        MOSTRAR " Boleto ", compra_numero
        MOSTRAR "   Tipo de asiento: ", tipo_asiento
        MOSTRAR "   Número de asiento asignado: ", asiento
        MOSTRAR "   Precio: $", precio

        resumen ← resumen + "Boleto " + compra_numero + ": " + tipo_asiento + 
                   " - Asiento " + asiento + " - Precio $" + precio + "\n"

        total_pagar = total_pagar + precio
        total_boletos = total_boletos + 1
        compra_numero = compra_numero + 1

        MOSTRAR "¿Deseas comprar otro boleto? (S/N)"
        LEER continuar

    FIN MIENTRAS

    MOSTRAR " Gracias por su compra. Resumen:"
    MOSTRAR resumen
    MOSTRAR " Total de boletos comprados: ", total_boletos
    MOSTRAR " Precio final a pagar: $", total_pagar

FIN
```