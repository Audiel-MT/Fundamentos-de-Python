# Manipulación y conversión de tipos numéricos en Python.
"""
Aprende a manejar números en Python con precisión:
identifica tipos con type, convierte con float, int y complex,
y genera aleatorios con random.randrange. Con estos fundamentos
evitarás pérdidas de datos por truncado y entenderás
por qué el límite superior no se incluye.
"""

numeroEntero = 45
numeroDecimal = 8.25
numeroComplejo = 1j

# Como podemos saber de que tipo son.
print("TIPOS DE NÚMEROS")
print(type(numeroEntero))
print(type(numeroDecimal))
print(type(numeroComplejo))
print("*********************")

"""
Los números enteros y decimales pueden tomar valores
positivos y negativos.
"""
print("POSITIVOS Y NEGATIVOS EN NÚMEROS ENTEROS Y DECIMALES")
positivoEntero = 10
negativoEntero = -75
positivoDecimal = 75.10
negativoDecimal = -89.25
print(positivoEntero)
print(negativoEntero)
print(positivoDecimal)
print(negativoDecimal)
print("***********************************************")

"""
En los numero complejo ambas partes (entera y imaginaria)
se pueden tener en positivo o negativo.
"""
print("POSITIVOS Y NEGATIVOS EN NÚMEROS COMPLEJOS")
complejoPositivo = 4+5j
complejoNegativo = -2-5j
print(complejoPositivo)
print(complejoNegativo)
print("***********************************************")

"""
En algunas ocasiones vamos a necesitar convertir un numero
entero a decimal o viceversa a esto se le llama casteo (casting).
"""
print("CONVERSION DE NÚMEROS O CASTEO (CASTING)")
print("números originales antes de hacer un casteo")
print(numeroEntero)
print(numeroDecimal)
print("CONVERSION DE NUMERO O CASTEO")
casteoDecimal = float(numeroEntero)
casteoEntero = int(numeroDecimal)
print(casteoDecimal)
print(casteoEntero)
print("***********************************************")
# DEBEMOS TENER MUCHO CUIDADO CUANDO SE CONVIERTA UN DATO DE DECIMAL A ENTERO.

"""
Con los complejos hay limitantes si se puede pasar un numero entero o decimal
a complejo pero no podemos pasar un complejo a entero o decimal.
"""
print("CONVERSION DE NÚMEROS ENTEROS, DECIMAL A COMPLEJOS")
entero = 55
decimal = 5.23

enteroComplejo = complex(entero)
decimalComplejo = complex(decimal)
print(enteroComplejo)
print(decimalComplejo)
print("***********************************************")

# Como podemos tener números aleatorio, utilizaremos random
# importamos la librería random
print("NUMERO ALEATORIO CON RANDOM")
import random
# imprimimos los números aleatorios.
print(random.randrange(1, 10))
# Nos dará un numero aleatorio entre en 1 y 9, no incluye el numero 10.