# Operador de asignación y operador walrus.
"""
Aprende a escribir código más claro y corto en Python
dominando operadores de asignación como +=, -=, =, /=, %=, //=, =
y el operador walrus* (:=). Con ejemplos simples verás cómo
actualizar variables sin repetirlas y cómo estos operadores
afectan los tipos numéricos.
"""

# Diferentes formas de utilizar el operador e igual (=) para asignar valores.

# Para asignar un valor a una variable.
x = 5
print("Valor de la variables x: ", x)

# Formas de acortar las asignaciones a una variable.

# Para realizar una suma (+=).
x += 3
print("Suma de 5 + 3 = ", x)

# Para realizar una resta (-=).
x -= 3
print("Resta: de 8 - 3 = ", x)

# Para realizar una multiplicación (*=).
x *= 3
print("Multiplicación de 5 * 3 = ", x)

# Para realizar una división (/=) da resultado con punto decimal.
x /= 3
print("División: de 15 / 3 = ", x)

# Para realizar el modulo (%=) o resto de una division.
x %= 2
print("Modulo o resto de 5 % 2 = ", x)

# Definimos una nueva variable (y)
y = 20

"""Para realizar una division y que esta nos de el resultado
con un valor entero (int) lo podemos hacer con las dobles diagonales
(//).
"""
# Division entera (//=).
y //= 2
print("Division entera de 20 // 2 = ", y)
# La parte decimal no la toma.

# Para realizar la operación de exponente se utiliza lo siguiente (**=).
y **= 3
print("Exponente de 10 ** 3 = ",y)

print()
"""
Vamos a utilizar un nuevo operador llamado WALRUS (morsa :=)
formas en como lo podemos utilizar.
"""
# Lo podemos utilizar directamente en la función print
# para asignar un valor a una variable.
print("UTILIZANDO EL OPERADOR WALRUS :=")
print("Asignado el valor a la variable en esta misma función: ", z := 567)