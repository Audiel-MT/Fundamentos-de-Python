# Para importa un modulo completo en nuestro archivo
# utilizamos la siguiente sintaxis.
import operaciones

# De esta manera podemos utilizar una operación.
print("DE ESTA MANERA PODEMOS UTILIZAR NUESTRO MODULO CON UNA OPERACIÓN")
print("Utilizamos nuestra operación de multiplicar")
# Llamamos a nuestro modulo 'operaciones'.
print(operaciones.multiplicar(5, 3))
# Pero debemos de estar llamando a nuestro
# modulo 'operaciones' por cada vez que necesitemos
# hacer una operación.
print("Utilizamos nuestra operación de suma")
print(operaciones.sumar(10, 8))
print()

# Como podemos evitar llamar a nuestro modulo 'operaciones'
# muchas veces para realizar nuestras operaciones.
print("CON LA SIGUIENTE SINTAXIS PODEMOS EVITAR LLAMAR A NUESTRO MODULO UN MONTÓN DE VECES")
# De esta manera podemos llamar a nuestro modulo solo
# una vez y importa todas las operaciones de el modulo.
from operaciones import sumar, restar, multiplicar, dividir
# Con la palabra reservada 'from' podemos traer el solo
# las funciones que necesitamos del modulo.
print("Utilizamos nuestra operación para dividir")
print(dividir(10, 0))
print("Utilizamos nuestra operación para restar")
print(restar(10, 15))

# Los módulos nos ayudan a tener diferentes archivo
# para separar nuestro código para que cada uno tenga 
# una funcionalidad distinta y tener un archivo 
# principal donde los podemos importa para utilizarlos.

