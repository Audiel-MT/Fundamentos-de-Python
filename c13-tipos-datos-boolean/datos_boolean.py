# Tipos de datos Boolean True, False y casting.
"""
Comprender los booleanos en Python te
permite tomar decisiones claras en el flujo de un programa.
Aquí verás cómo obtener valores True y False, cómo funciona el casting
a bool y cómo usar isinstance para validar tipos sin enredarte.
"""

print("ESTOS SON LOS DOS VALORES QUE PUEDEN TOMAR LOS DATOS DE TIPO BOOLEAN")
# Lo datos Booleanos pueden tomar dos tipos de valores.
v = True # Verdadero.
f = False # Falso.
print(v)
print(f)
print("************************************")

# De esta otra forma podemos conseguir que nos de un valor Boolean.
print("COMPARACIÓN DE NÚMEROS")
# Comparamos si 5 > 2.
print("5 > 2")
print(5 > 2) # True.
print("3 > 5")
print(3 > 5) # False.
print("************************************")

# Para ver que tipo de valor son nuestra variables.
print('ESTO SON LOS TIPOS DE VALORES DE LAS VARIABLES "v" y "f"')
print(type(v))
print(type(f))
print("************************************")

# También podemos hacer castear (casting) con otros tipos de datos a Boolean.
print('CASTING DE VALORES DE TIPO "string" A "bool"')
# casting de un texto nos da el siguiente resultado.
print(bool("Hola mundo")) # True
# casting de un texto vació nos da el siguiente resultado.
print(bool(""))
print("************************************")

"""
Nota cualquier datos que sea diferente a cero (0), a un string vació
y el dato de tipo None, cuando realicemos en casting de ellos nos dará
el valor de 'True' de lo contrario nos dará el valor de 'False'.
"""
print('TIPOS DE DATOS QUE AL HACER "casting" NOS DARÁN COMO RESULTADO "True"')
# Numero mayor a cero (0).
print(bool(3))
# String con caracteres.
print(bool("Hola"))
# Lista con datos.
print(bool([1,"hola", False]))
print("************************************")

print('TIPOS DE DATOS QUE AL HACER "casting" NOS DARÁN COMO RESULTADO "False"')
# El numero cero (0).
print(bool(0))
# string vació.
print(bool(""))
# Lista sin datos.
print(bool([]))
# El tipo de dato None lo veremos mas adelante,
# pero si hacemos un casting de el nos dará como resultado "False".
print(bool(None))
print("************************************")

# Para validar si un tipo de datos corresponde al que nosotros estamos buscado.
# podemos utilizar el método isinstance() para comparar nuestra variable con el dato.
print('MÉTODO "isinstance()" PARA COMPARAR UNA VARIABLE CON UN TIPO DE DATO')
# Vamos a comprar el valor "123", con nuestra clase de tipo "int".
print("Tipo de dato entero (int)")
entero = 123
print(isinstance(entero, int)) # Nos retornara un True.
# Creamos un valor de tipo decimal.
print("Tipo de dato decimal (float)")
decimal = 12.50
print(isinstance(decimal, float)) # Nos retornara un True.
print("Tipo de dato texto (string)")
# Creamos un valor de tipo texto.
texto = "hola"
print(isinstance(texto, str)) # Nos retornara un True.
print("Tipo de dato lista (list)")
# Creamos una lista.
lista = [1, "hola", 3.25]
print(isinstance(lista, list))