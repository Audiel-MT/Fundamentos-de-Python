# Tipo de dato None.
"""
Comprender None en Python marca la diferencia al escribir código claro y seguro.
Aquí verás por qué None es la ausencia de valor, cómo se imprime,
cuál es su tipo real (NoneType) y en qué se diferencia de un string vacío,
un cero, un false o una lista vacía. Además, verás por qué será clave
cuando trabajes con funciones.
"""
print('TIPO DE DATO "None"')
# Vamos a imprimir una variable con el tipo de dato None (seria la ausencia de valor).
x = None
print(x)
print(type(x))
print("**************************")

# Para comprender mejor el None es una clase distintas a
# un string vació.
# a un numero cero.
# y a una lista sin datos.
print('DIFERENCIAS ENTRE EL DATO "None" Y DATOS COMO "string vació, un cero y una lista sin datos o False"')
print(type(""))
print(type(0))
print(type(False))
print(type([]))
print("**************************")
"""
El tipo de dato 'None' es muy utilizado en la funciones
ya que las funciones retornan valores y en alguna ocasiones
no pueden retornar nada y es necesario saber que es el valor 'None'
(ausencia de valor).
"""