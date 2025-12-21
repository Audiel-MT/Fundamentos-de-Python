# ¿Qué son los tipos de datos en Python y cómo elegirlos?
"""
Los tipos de datos definen la naturaleza del valor
que guardas en una variable. En Python, trabajarás
con texto (string), números (entero, flotante, complejo),
colecciones (lista, tupla, diccionario, conjunto)
y booleanos. La elección depende del contenido 
y de si necesitas modificarlo (mutable) o mantenerlo fijo (inmutable).
"""

# Datos de tipo texto (string).
print("TIPOS DE DATOS TEXTOS")
comillasSimples = 'Este es un texto con comillas simples'
comillasDobles = "Este es un texto con comillas dobles"
# En este caso también se puede utilizar las comillas dobles. 
comillasTriples = '''Este es un texto con comillas triples pero se utilizan las comillas simples'''
# Mostramos los datos por consola.
print(comillasSimples)
print(comillasDobles)
print(comillasTriples)
print("****************************")

# Tipo de datos números (int, float y complex)
print("TIPOS DE DATOS NÚMEROS")
numeroEntero = 10
numeroDecimal = 3.1416
numeroComplejo = 5+2j
# Mostramos los datos por consola.
print(numeroEntero)
print(numeroDecimal)
print(numeroComplejo)
print("****************************")

# Tipo de datos lista (list).
"""
Es una colección de dato (cualquier dato) ordena y mutable (se puede modificar)
en el cual cada elemento de esa lista tiene un indice (es la posición).
"""
print("TIPOS DE DATOS LISTA")
lista = [25, "hola", 2+8j, 2.16]
# Mostramos la lista completa en consola.
print(lista)
# Mostramos un dato por su indice.
print(lista[2])
print("****************************")

# Tipo de datos tupla (Tuple)
"""
Es una colección de datos (cualquier dato) ordenadas, pero son immutable (no se pueden modificar)
los datos, pero al igual que las listan tienen un indice para acceder a un dato. 
"""
print("TIPOS DE DATOS TUPLA")
tupla = ("hola", 56, 4+8j)
# Mostramos la tupla completa en consola.
print(tupla)
# Mostramos un dato por su indice.
print(lista[1])
print("****************************")

# Tipo de datos diccionario.
"""
Es una colección de datos clave y valor (key and value) ordenadas y mutables (se pueden modificar),
a partir de python 3.7  se agrego que los diccionario fueran ordenados.
"""
diccionario = {
    "nombre":"Juan",
    "edad": 45,
    "ciudad": "Barcelona"
}
print("TIPOS DE DATOS DICCIONARIO")
# Mostramos el diccionario completo.
print(diccionario)
# Mostramos un datos por su clave (key).
print(diccionario["edad"])
print("****************************")

# Tipo de datos conjunto (sets)
"""
Es una colección de datos (cualquier tipo de dato) desordenada
y es mutable (se pueden modificar) los elementos van hacer
únicos ningún dato se repito y no se pueden mostrar un único dato 
por su indice. 
"""
print("TIPOS DE DATOS CONJUNTOS")
conjuntos = {1, 1, "hola", 2, 3, 3, "hola"}
# Mostramos el conjunto completo.
print(conjuntos)
print("****************************")

# Tipo de datos booleanos.
"""
Este tipo de datos son dos True y False
"""
print("TIPOS DE DATOS BOOLEANOS")
booleanosVerdadero = True
booleanosFalso = False
# Mostramos los datos por consola.
print(booleanosVerdadero)
print(booleanosFalso)
print("****************************")

