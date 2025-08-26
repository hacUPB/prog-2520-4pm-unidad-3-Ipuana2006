# Operadores y Tipos de Datos en Python

## Operadores Aritméticos en Python
Los operadores aritméticos en Python se utilizan para realizar operaciones matemáticas básicas como suma, resta, multiplicación, división, entre otras. Son fundamentales para trabajar con números en cualquier programa.

| Operador | Descripción                 | Ejemplo en Python | Resultado |
|----------|-----------------------------|------------------|-----------|
| `+`      | Suma                        | `5 + 3`          | `8`       |
| `-`      | Resta                       | `5 - 3`          | `2`       |
| `*`      | Multiplicación              | `5 * 3`          | `15`      |
| `/`      | División (float)            | `5 / 2`          | `2.5`     |
| `//`     | División entera (floor)     | `5 // 2`         | `2`       |
| `%`      | Módulo (residuo)            | `5 % 2`          | `1`       |
| `**`     | Potencia                    | `2 ** 3`         | `8`       |

---

## Operadores Relacionales en Python
Los operadores relacionales permiten comparar dos valores. El resultado de estas comparaciones siempre es un valor lógico (`True` o `False`). Son esenciales para la toma de decisiones dentro de un programa.

| Operador | Descripción                            | Ejemplo | Resultado |
|----------|----------------------------------------|---------|-----------|
| `==`     | Igual a                                | `5 == 5` | `True`   |
| `!=`     | Distinto de                            | `5 != 3` | `True`   |
| `>`      | Mayor que                              | `7 > 3`  | `True`   |
| `<`      | Menor que                              | `3 < 7`  | `True`   |
| `>=`     | Mayor o igual que                      | `5 >= 5` | `True`   |
| `<=`     | Menor o igual que                      | `3 <= 5` | `True`   |

---

## Operadores Lógicos en Python
Los operadores lógicos se usan para combinar expresiones condicionales. Trabajan con valores booleanos (`True` o `False`) y son muy utilizados en estructuras de control como `if`, `while` y `for`.

| Operador | Descripción                          | Ejemplo           | Resultado |
|----------|--------------------------------------|------------------|-----------|
| `and`    | Devuelve `True` si ambas condiciones son verdaderas | `(5 > 2) and (3 < 4)` | `True` |
| `or`     | Devuelve `True` si al menos una condición es verdadera | `(5 > 10) or (3 < 4)` | `True` |
| `not`    | Invierte el valor lógico (negación)  | `not(5 > 2)`     | `False`  |

---

## Tipos de Datos en Python
En Python existen distintos tipos de datos que nos permiten representar información de diferentes formas: números, texto, valores lógicos, colecciones, entre otros. Conocerlos es clave para manejar correctamente la información en un programa.

| Tipo     | Descripción                          | Ejemplo                |
|----------|--------------------------------------|------------------------|
| `int`    | Números enteros                      | `x = 10`               |
| `float`  | Números decimales                    | `y = 3.14`             |
| `complex`| Números complejos                    | `z = 2 + 3j`           |
| `str`    | Cadenas de texto                     | `s = "Hola"`           |
| `bool`   | Valores lógicos (True/False)         | `flag = True`          |
| `list`   | Lista ordenada y mutable             | `[1, 2, 3]`            |
| `tuple`  | Tupla ordenada e inmutable           | `(1, 2, 3)`            |
| `set`    | Conjunto no ordenado y sin repetidos | `{1, 2, 3}`            |
| `dict`   | Diccionario clave-valor              | `{"a": 1, "b": 2}`     |

## Conclusión

Los operadores y tipos de datos en Python constituyen la base fundamental para el desarrollo de programas.  
Los **operadores aritméticos, relacionales y lógicos** permiten realizar cálculos, comparaciones y decisiones dentro del código, mientras que los **tipos de datos** ofrecen distintas formas de representar y organizar la información.  
Comprender estos elementos no solo facilita la resolución de problemas, sino que también es esencial para escribir programas eficientes, claros y fáciles de mantener.
