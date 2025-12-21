# ¿Qué es una variable en Python y cómo se asigna?
"""
Una variable es una “cajita” en memoria donde guardamos un valor
para usarlo después. Con el signo igual definimos
el nombre y asignamos el valor: el símbolo “=” es
el operador de asignación que mueve el valor
de la derecha a la variable de la izquierda.
"""

# x: Es el nombre de la variable.
# =: Con el signo igual podemos almacenar un valor en la variable.
# Y por ultimo colocamos el valor que sera asignado a la variable.
x = "Esta es una variable"
# Ahora imprimiremos el valor de la variable "x" por consola.
print(x)

# Python nos permite sobrescribir las variables.
x = 5.78
# Imprimimos el valor de "x"
print(x)

"""
Podemos declarar dos variables con el mismo nombre
pero si una esta en mayúscula y la otra en minúscula
no serán lo mismo apuntaran a distintos lugares en memoria.
"""
v = "Esta es nuestra variable en minúscula"
X = "Esta es nuestra variable en mayúscula"
print(v)
print(x)

# Nombres de variables validos.
mivariable = "Esta es una variable valida toda esta en minúscula"
mi_variable = "Esta es una variable valida lleva un guion bajo ( _ )"
_mi_variable = "Esta variable inicia con guion bajo y es valido (SE UTILIZA CON VARIABLES QUE SON PRIVADAS)"
miVariable = "Esta es una variable validad por que tiene una mayúscula"
MIVARIABLE = "Esta es una variable valida por que esta toda en mayúscula (SE UTILIZAN PARA CONSTANTE)"
mivariable2 = "Esta es una variable valida por que tiene un numero al final"

# Nombres de variables no validos.
2mivariable = "Iniciar con un numero no se puede declarar una variable"
mi-variable = "Tampoco se puede utilizar guio medio ( - )"
mi variable = "No se puede utilizar espacios"

# Convenciones para escribir nombres de variables largos.
camelCase = "Comienza con minúscula y la primera letra de la segunda palabra se pone en mayúscula"
PascalCase = "Comienza con la primera letra en mayúscula y cuando inicia la segunda palabra la primera letra se pone en mayúscula"
snake_case = "Esta se separa cada palabra con un guion bajo ( _ ) y todas las palabras son en minúsculas"