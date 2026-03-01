# Manejo de errores con try, except y finally.
"""
Aprende a manejar errores en Python con confianza:
captura excepciones con try, responde con except y
garantiza acciones finales con finally. Con ejemplos
claros como ZeroDivisionError y NameError,
verás cómo evitar caídas y comunicar la intención
del código con mensajes útiles.
"""
# Esta seria la sintaxis básica de try y except.
print("SINTAXIS BÁSICA DE try Y except")
# Intentamos algo.
try:
    print("Se ejecuta nuestro código")
# Si hay un error se ejecutara el 'except'.
except:
    print("Captura el error")
print()

# Crearemos un error con una división entre cero.
print("ERROR CUANDO QUEREMOS DIVIDIR ENTRE CERO ( 0 )")
# Realizamos nuestra división entre cero ( 0 ).
try:
    numero = 20 / 0
# Colocamos el tipo de except que se espera recibir.
except ZeroDivisionError:
    # Colocamos un mensaje mas claro para los usuario.
    print("No se puede dividir entre 0")
print()

# Otro error que se puede validar es cuando no declaramos una variable.
print("OTRO ERROR ES CUANDO NO DECLARAMOS LA VARIABLE")
# Intentamos imprimir nuestra variable.
try:
    print("Bienvenido ", nombre)
# Colocamos el tipo de error en nuestro except.
except NameError:
    # Y colocamos un mensaje.
    print("La variable no ha sido definida")
print()

# También podemos utilizar la sentencia finally
# esta se ejecutara cuando se ejecute el 'try' o el 'except'.
print("SENTENCIA finally SIEMPRE SE EJECUTARA")
try:
    print("Se ejecuta con éxito")
except:
    print("No se puede ejecutar")
# Utilizamos la sentencia finally.
finally:
    print("La sentencia 'finallly' se ejecutara siempre")
print()

# Declaramos una lista de números. 
numeros = [1, 2, 3]
print("INGRESAMOS AL INDICE NUMERO [10] DE LA LISTA números")
try:
    print(numeros[10])
except IndexError:
    # Ponemos el error que nos dará en nuestro except.
    print("No se puede ingresar al indice")
    print("Total de datos en la lista es de", len(numeros))
finally:
    print("Ejecución finalizada...")

# De esta manera podemos capturar errores
# y mostrar un mensaje claro para el usuario.