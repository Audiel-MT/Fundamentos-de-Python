# Bucle While, break y continue.

"""
Aprende a dominar el bucle while en Python con ejemplos claros
y prácticos. Verás cómo controlar la condición, cortar la ejecución
con break, saltar iteraciones con continue y aprovechar el else del while.
Todo con código mínimo y explicaciones directas para evitar errores comunes
como el bucle infinito.
"""

# El bucle While se va arrepentir mientra nuestra condición nos de un dato True.
# inicializamos nuestra variable con el valor de 1.
i = 1

print("UTILIZAMOS NUESTRO BUCLE while")
# Y creamos nuestra condición while.
while i <= 10:
    # Vamos a imprimir nuestra variable (i).
    print("El valor de i es igual a", i)
    # Pero debemos colocar una
    # instrucción mas que nuestra
    # variable (i) se incremente de 1 en 1
    # para evitar un bucle infinito.
    i += 1
print()

print("UTILIZAMOS EL BUCLE while CON LA PALABRA RESERVADA break")
# Con la palabra reservada 'break' podemos 
# salir de nuestro bucle antes que se cumpla
# la condición y nos de un valor True.

j = 1
while j <= 10:
    # Se imprime la variable (i).
    print("El valor de j es igual a", j)
    # Creamos una nueva condición
    # donde validamos si (i) es igual a 5.
    if j == 5:
        print("El bucle a finalizado por la palabra reservada break")
        break
    # Siempre se debe de colocar
    # la instrucción donde la variable
    # (i) se incrementa.
    j += 1
print()

print("VALIDAMOS SI SE EJECUTA LA PALABRA break CON LA SIGUIENTE CONDICIÓN")
# variable que utilizaremos.
l = 0
# La condición seria validar si se ejecuta el break
# cuando la variable tenga el valor de 5.
while l <= 10:
    # Imprimimos el valor de l.
    print("El valor de l es igual a ", l)
    # Creamos la condición donde la variable (l) sea igual a 5.
    if l == 5:
        print("El bucle a finalizado con la palabra reservada break")
        break
    # Hace un incremento de la variable (l) pero de dos en dos.
    l += 2
    # Nuestra variable (l) nunca tomara el valor de 5, por eso el bucle no se rompe.
print()

print("UTILIZAREMOS LA PALABRA RESERVADA continue")
# Con esta palabra reservada podemos saltarnos 
# la linea de código cuando donde se encuentre.

c = 0
# Creamos nuestro bucle.
while c < 10:
    # Incrementamos nuestra variable antes para que no quede en un bucle infinito.
    c += 1
    # Creamos la condición donde utilizaremos la palabra reservada continue.
    if c == 5:
        print(" *No muestra la variable c* ")
        continue
    # Y no vamos a mostrar nuestra variable (c) cuando tenga el valor de 5.
    print("El valor de c es igual a", c)
print()

print("UTILIZAREMOS LA SENTENCIA else EN NUESTRO BUCLE while")
# Podemos utilizar la sentencia else en nuestro bucle while
# como en los condicionales if - else.

e = 0

# Creamos nuestro bucle while con la sentencia else.
while e < 10:
    # Y creamos nuestras condiciones.
    if e % 2 == 0:
        print("El valor actual de la variable es", e, " y es un numero par")
    else:
        print("El valor actual de la variable no es par")
    e += 1
# La condición else se ejecutara cuando termine el bucle while.
else:
    print(" *La variable e ya es mayor a 10* ")