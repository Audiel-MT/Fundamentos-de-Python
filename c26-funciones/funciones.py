# Definición y uso de funciones.
"""
Domina las funciones en Python para escribir código claro,
modular y reutilizable. Aquí verás cómo definir con def,
invocar con paréntesis, personalizar con argumentos y
parámetros, usar valores por defecto, devolver resultados
con return y preparar funciones vacías con pass.
Todo con ejemplos simples y directos.
"""

# Sintaxis para definir una función.
# Se utiliza la palabra reservada 'def'
# seguido del nombre de la función.
def mi_funcion():
    # Este código se ejecutara cuando llame
    # a la función.
    print("Hola mundo desde una función")
print()

# Forma de llamar o invocar una función.
print("DE ESTA FORMA PODEMOS LLAMAR A NUESTRA FUNCIÓN")
# Ponemos el nombre de nuestra función y colocamos los paréntesis.
mi_funcion()
print()

# Creamos otra función donde le podremos pasar argumentos.
print("FUNCIÓN LA CUAL RECIBE ARGUMENTOS CUANDO SE LLAMA")
# Definimos la función con el parámetro 'nombre'.
def saludar(nombre): # El parámetro de define al crear una función. 
    print("Hola ", nombre)

# Llamamos nuestra función 'saludar'
# y le pasamos nuestro argumentos que seria el valor.
saludar("Nicolas")
saludar("Marcelo")
# Asi es como podemos utilizar una función con diferentes nombres.
print()

# Debemos seguir el orden de los parámetros de nuestra función.
# por que asi se mostraran los argumentos que le pasemos a la función.
print("ORDEN DE PARÁMETRO Y ARGUMENTOS DE LAS FUNCIONES")
# Creamos una nueva función.
def datos(nombre, apellido, edad):
    print("Nombre ",nombre, " apellido ",apellido, " edad ",edad)

# Llamamos a nuestra función.
# Enviamos los argumentos de manera desordenada.
datos("Moran", 24, "Alexander")
# Ahora enviamos los argumentos de manera ordenada.
datos("Alexander", "Moran", 26)
# y si no mandamos alguno de los argumentos nos dará un error.
# datos("Alexander")
# Por eso es importante enviar todos los argumentos
# que espera una función.
print()

# De esta manera podemos evitar errores cuando no pasamos un argumentos
# poner en el parámetro un dato por defecto.
print("ARGUMENTOS POR DEFECTOS PARA EVITAR ERRORES")
# Creamos una nueva función con un parámetro por defecto.
def evitar_errores(nombre, nacionalidad="Colombia"):
    print("hola ", nombre, "de", nacionalidad)

# Llamamos a nuestra función.
evitar_errores("Jorge",)
evitar_errores("Jorge", "España")
print()

# De igual manera las funciones nos pueden devolver valores.
print("DE ESTA MANERA PODEMOS DEVOLVER VALORES CON LAS FUNCIONES")
# Creamos nuestras funciones.
def sumar(a, b):
    # Utilizamos la palabra reservada return
    # para devolver el valor.
    return a + b

# Llamamos a nuestra función.
resultado = sumar(2, 3)
print(resultado)
print()

# Y si aun no tenemos la lógica de las función podemos utilizar
# la palabra reservada 'pass' para que no de error.
print("UTILIZANDO LA PALABRA RESERVADA pass PARA EVITAR ERRORES")
# Definimos nuestra función.
def nueva_funcion():
    # Con esta palabra podemos ejecutar
    # el código sin que nos de error
    pass
print()

# Desafió de Platzi, crear funciones que realicen
# las operaciones matemáticas básicas.

# Creamos la primera función para suma.
def suma(a, b):
    return a + b

# Creamos la segunda función para resta.
def resta(a, b):
    return a - b

# Creamos la tercera función para multiplicación.
def multiplicar(a, b):
    return a * b

# Creamos la cuarta función para dividir.
def division(a, b):
    if b == 0:
        return "No se puede dividir entre ", b
    else:
        return a / b
# En la división utilizamos
# una condición donde evaluamos
# si el segundo argumento que se le
# pasa a la función cuando se llama
# es igual a cero ( 0 ).