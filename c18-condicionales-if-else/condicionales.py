# Condicionales if else.

"""
Domina los condicionales en Python con ejemplos 
claros y prácticos: cuándo usar la sentencia if,
cómo decidir con else, combinar condiciones con and y or,
comparar números y strings, anidar if y aprovechar el statement pass.
Controla el flujo del programa con seguridad y evita errores de sintaxis
gracias a la indentación correcta.
"""

# Variables qu utilizaremos.
x = 5
y = 3
z = 6

# Condición if.
print("UTILIZANDO LA CONDICIÓN if")
if x > y:
    # Imprimirá esto por consola.
    print("5 > 3:", x > y)

if x < y:
    # No va imprimir nada por consola.
    print("5 < 3", x < y)

# Para poder evaluar una segunda condición podemos utilizar elif.
print("UTILIZANDO LA CONDICIÓN if Y UN elif PARA LA SEGUNDA CONDICIÓN")

if x < y:
    print("No se va a ejecutar")
# Utilizamos el condicional elif para evaluar la siguiente condición.
elif x > y:
    print("Se cumple la condición elif")
    print("5 > 3:", x > y)

# Y cuando ninguna de las dos condiciones se cumple utilizamos el else.
print("UTILIZAREMOS LA CONDICIÓN else CUANDO NO SE CUMPLA EL if NI EL elif")

if x < y:
    print("El 'if' no se cumple")
elif x == y:
    print("El 'elif' no se cumple")
# utilizamos el else cuando ninguna condición se cumpla.
else:
    print("Se ejecuta el else cuando ya no hay if ni elif para evaluar")
print()


print("UTILIZAREMOS OPERADORES LÓGICOS EN NUESTRAS CONDICIONES")

print("UTILIZAMOS EL CONDICIONAL if CON EL OPERADOR LÓGICO and")
# Utilizaremos el operador (and) donde ambas condiciones deben de cumplirse.
if x > y and y < z: 
    print("Se utiliza el operador lógico (and) donde ambas condiciones se cumple")
    print(x, ">", y, "and", y ,"<", z)

print("UTILIZAMOS EL CONDICIONAL elif CON EL OPERADOR LÓGICO or")
# Utilizaremos el operador (or) donde solo una condición se debe cumplir.
if x > y and y == z:
    print("No se ejecuta este código")
# Utilizaremos en la condición elif el operador (or).
elif x < y or y < z:
    print("Se utiliza el operador lógico (or) donde solo una condición se debe de cumplir")
    print(x, "<", y, "or", y, "<", z)


print("UTILIZAREMOS LA CONDICIÓN else ESTA SE EJECUTA CUANDO NINGUNA CONDICIÓN if Y elif DA VERDADERO")
# Se ejecuta cuando ninguna condición es verdadera.
if x == y and y == z:
    print("No se ejecuta este código")
elif x == y or y == z:
    print("No se ejecuta este código")
# Se ejecuta el código que esta en el else por que ninguna da el valor True.
else:
    print("Se ejecuta por que ninguna condición es verdadera")
    print()

print("COMPARACIÓN DE STRING (str)")

# Variables.
py = "Python"
js = "JavaScript"
pyt = "Python"

# Creamos la condición if.
print("CREAMOS UNA CONDICIÓN if PARA VALIDAR LOS DATOS DE TIPO string (str)")
if py == js:
    print(py, "es igual a ", js)
else:
    print("Lo datos de tipo string no son iguales")

# Creamos una nueva condición donde anidamos otro if.
print("CREAMOS UNA CONDICIÓN if DONDE ESTARÁ ANIDADO OTRA CONDICIÓN if")
if py != js:
    print(py, " es diferente a ", js)
    if py == pyt:
        print(py, " es igual a ", pyt)
else:
    print("Los datos tipo string (str) no son iguales")
print()

print("UTILIZANDO LA PALABRA RESERVADA pass PARA QUE EL FLUJO DEL CÓDIGO NO DE ERROR")
# Cuando aun no tengamos el código completo
# podemos utilizar la palabra reservada (pass)
if py != x:
    pass
# Para evitar errores