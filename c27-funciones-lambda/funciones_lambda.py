# Funciones lambda y fabrica de funciones.
"""
Las lambdas en Python simplifican operaciones
puntuales con código claro y directo. Aquí entenderás
qué es una función anónima, cómo manejar argumentos y
cómo crear una fábrica de funciones para construir un
duplicador y un triplicador con poca sintaxis y alto impacto.
"""

# Sintaxis básica de una función lambda.
print("SINTAXIS BÁSICA DE UNA FUNCIÓN lambda")
# lambda argumento : expresión.
x = lambda a : a + 10
print()

# Imprimimos el dato de la función lambda.
print("UTILIZAMOS LA FUNCIÓN lambda")
print(x(5))
print()

# También podemos utilizar una función lambda con mas de un argumento.
print("FUNCIÓN LAMBDA CON MAS DE UN ARGUMENTO")
# Creamos la función lambda con doble argumento.
y = lambda x, v : x + v
print(y(2, 3))
print()

# Una de las funciones mas importante que podemos realizar con 'lambda'.
print("FABRICA DE FUNCIONES")
# Creamos nuestras funciones.
def mi_funcion(n):
    return lambda a : a * n

duplicador = mi_funcion(2)
triplicador = mi_funcion(3)
quintiplicador = mi_funcion(5)
# Imprimimos las variables.
print(duplicador(5))
print(triplicador(5))
print(quintiplicador(5))

# Una función lambda nos permite crear 
# pequeñas porciones de código que realice
# una tarea en especifico y para la cual no
# es necesario declarar una función con la 
# palabra reservada 'def'.  

