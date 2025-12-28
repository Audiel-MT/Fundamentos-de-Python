# Slicing, replace y split para manipular strings.
"""
Aprende a dominar textos en Python con técnicas prácticas:
índices base cero, slicing con fin no incluido,
búsquedas seguras con normalización, y métodos esenciales
como replace y split. Con estas habilidades trabajarás textos
largos con precisión, evitando errores típicos al cortar,
reemplazar y comparar cadenas
"""

# Que es el indice.
"""
El indice es la posición donde se encuentra una letra
en un texto y también tener en cuanta que los espacios cuentan,
en este caso el indice comienza con el numero 0.
"""
#indice  0123456789
texto = "Este es un texto"

# Vamos a busca una letra del texto con su indice.
print("BUSCANDO UNA LETRA POR SU INDICE")
# Texto original.
print(texto)
# Buscamos la letra "E" por su indice que es 0.
print(texto[0])
print("**************************")

# Técnica slicing para recortar una parte del texto.
print('TÉCNICA "SLICING" PARA RECORTAR PARTE DEL TEXTO')
print(texto)
# Tomaremos la palabra "Este" de nuestro texto.
print(texto[0:4])
print("**************************")

"""
Cuando hagamos slicing debemos de tomar
un indice mas al final para completar la palabra.
"""
print('TRATAREMOS DE IMPRIMIR TODA LA FRASE UTILIZANDO "SLICING"')
# Trataremos de imprimir toda la frase.
print(texto[0:15]) # Como podemos ver la ultima letra no la imprime.
print("**************************")

# Para poder imprimir todo el texto podemos utilizar el "slicing" de la siguiente manera.
# No le agregamos el ultimo indice que tiene nuestro texto solo lo dejamos vacío.
print("IMPRIMIENDO TODO EL TEXTO CON EL INDICE VACÍO AL FINAL")
print(texto[0:])
print("**************************")

# También podemos imprimir texto al contrario sin poner un indice al inicio.
print("IMPRIMIENDO TEXTO SIN PONER INDICE AL INICIO")
print(texto[:10])
print("**************************")

# También podemos utilizar indices negativos.
print("UTILIZANDO INDICES NEGATIVOS PARA BUSCAR UNA PALABRA")
# utilizando los indice 8 que equivale a la letra "u".
# y utilizamos el indice -2 que equivale a la letra "t".
print(texto[8:-2])
print("**************************")

# Como podemos modificar el texto.
print('MÉTODO "replace()" PARA PODER CAMBIAR UNA PALABRA EN UN TEXTO')
# Texto que vamos a modificar.
curso = "Este es un curso de Javascript"
# Imprimimos el texto original.
print(curso)
# Imprimimos el texto modificado.
print(curso.replace("Javascript", "Python"))
"""
Este método remplazara la palabra
si se repite mas de una vez.
"""
print("**************************")

# Como podemos crear una lista por medio del método
# split cuando se repite un carácter en un texto. 
print('MÉTODO "split" PARA DIVIDIR UN TEXTO CUANDO SE REPITE UN CARÁCTER')
print(texto)
# Vamos utilizar la variable "texto" y lo vamos a dividir por sus espacios.
textoDividido = texto.split(" ")
# Imprimimos el nuevo dato.
print(textoDividido) # y lo que nos retorna es una lista.
print(type(textoDividido))
print("**************************")

# Normalización
print("NORMALIZACIÓN DE TEXTO")
texto2 = "Este texto tiene MAYÚSCULAS y minúsculas y necesito encontrar ciertas palabras"
print(texto2)
# Para validar si la palabra se encuentra dentro de nuestro texto.
# Utilizaremos el método "lower()" para convertir en minúscula todo el texto.
# Y la palabra reservada "in" para validar si esta dentro de nuestro texto la palabra.
print("mayúscula".lower() in texto2.lower())

