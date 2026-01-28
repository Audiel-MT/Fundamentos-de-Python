# Operadores de comparación y lógicos.
"""
Domina los operadores lógicos en Python para tomar decisiones
con seguridad y construir un flujo de control claro.
Aquí verás cómo usar el operador lógico or, la negación con not,
y los booleanos (True y False) junto a operadores de comparación
como igualdad (==) y mayor que (>), tal como se explica paso a paso.
"""

# Vamos a comparar estas variables.
x = 5
y = 3
z = 5

# Operador de igualdad (==).
print(x," == ",y, x == y)

# Operador si es distinto a (!=).
print(x," != ", y, x != y)

# Operador para saber si es mayor (>).
print(x, " > ", y, x > y)

# Operador para saber si es menor (<).
print(x, " < ", y, x < y)

# Operador para saber si es mayor (>).
print(x, " > ", y, x > y)

print("UTILIZAMOS NUESTRA VARIABLES CON VALOR DE", z)
# Operador para saber si es mayor o igual (>=).
print(x, " >= ", z, x >= z)

# Operador para saber si es menor o igual (<=).
print(x, " <= ", z, x <= z)

"""
Que pasa si tenemos mas de dos variables para 
comparar, para eso utilizaremos operadores lógicos.
"""
# Operadores lógicos.
print("OPERADORES LÓGICOS (and, or, not)")

# Utilizaremos el operador (and) en este
# ambas condiciones se deben de cumplir para que nos de True.
print("OPERADOR LÓGICO and")
print(x," == ", z ,"and", z, " > ", y,":", x == z and z > y)

# Utilizaremos el operador (or) en este
# caso solo una condición se debe cumplir para que nos de True.
print("OPERADOR LÓGICO or")
print(x," == ", z ,"or", z, " < ", y,":", x == z or z < y)

# Utilizaremos el operador (not) en este
# caso podemos negar un valor y cambiar el resultado de True a False
# o de False a True.
print("OPERADOR LÓGICO not")
# Vamos a negar el valor True.
print("Valor True: ", not(True))
# Vamos a negar el valor False.
print("Valor False: ", not(False))

"""
Con los operadores de comparación y operadores lógicos
le podemos dar flujo a nuestros programas de Python
para tomar diferentes decisiones.
"""