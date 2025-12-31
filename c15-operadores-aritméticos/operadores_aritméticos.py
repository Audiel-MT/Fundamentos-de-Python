# Operadores aritméticos.
"""
Domina los operadores aritméticos en Python
con ejemplos claros y resultados esperados.
Aquí verás cómo aplicar suma, resta, multiplicación, división,
módulo, potencia y división entera, cómo validar si un número es par
con el operador de igualdad, y cuál es la precedencia de operadores
que guía la evaluación de expresiones.
"""

# Variables.
x = 5
y = 10

# Operadores aritméticos.
print("OPERADORES ARITMÉTICOS")

# Suma (+).
print("Suma", x + y)

# Resta (-).
print("Resta", x - y)

# Multiplicación (*).
print("Multiplicación", x * y)

# División (/) siempre retorna un Float.
print("División", x / y)

# Modulo (%) o resto de la división.
print("Modulo o resto de la división", x % y)

# Potencia (**).
print("Potencia", y ** x)

# División entera (//).
print("División entera", y // x)
print("************************************")

# Como podemos utilizar el operador "Modulo"

# para validar si un numero es par.
v1 = 8
print("El numero 8 es par: ", v1 % 2 == 0) # Obtenemos True.
print("Modulo o resto de la división de 8 / 2:", v1 % 2)
# Validemos con el numero 9.
v2 = 9
print("El numero 9 es par: ", v2 % 2 == 0) # Obtenemos False.
print("Modulo o resto de la división de 9 / 2:", v2 % 2)
print("************************************")

# Jerarquía de los operadores.
print("JERARQUÍA DE OPERADORES ARITMÉTICOS")
print("1 - todo lo que este en paréntesis () se ejecutara de primero")
print("2 - Exponentes")
print("3 - Multiplicaciones(*), Divisiones(/), Divisiones Enteras(//) y Módulos o Resto(%)")
print("4 - Sumas(+) y Restas(-)")
print("6 - Comparaciones de identidad y Pertenecía")
print("7 - Lógicos")
print("************************************")