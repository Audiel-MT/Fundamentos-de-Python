# Manejo de comillas, múltiples líneas y búsqueda en strings de Python.
"""
Domina las operaciones esenciales con cadenas en Python:
manejo de comillas, múltiples líneas, conteo de caracteres,
búsqueda de palabras, transformación a mayúsculas/minúsculas
y limpieza de espacios. Con ejemplos claros y resultados esperados,
entenderás cómo funcionan los métodos más
usados de los strings sin errores comunes.
"""

# Como podemos utilizar las comillas dobles dentro de un texto que lo necesitamos.
print('Hola con comillas "dobles"')
# Podemos utilizar las comillas simple para utilizar las comillas dobles dentro.

# Y para utilizar las comillas simple por dentro se haría lo contrario.
print("Hola con comillas 'simple'")
print("******************************")

# Como podemos utilizar multiples lineas.
# Utilizando las comillas dobles como comentario
# podemos tener un texto con multiples lineas y respetara
# los saltos de linea.
print("TEXTO EN MULTIPLE LINEAS") 
multiples = """Este es un texto
dentro de comillas triple
y vemos que respeta
los saltos de linea que se le dan"""
print(multiples)
print("******************************")

# Método para saber cuantos caracteres contiene un texto.
print('MÉTODO "len()" PARA SABER CUANTOS CARACTERES TIENE UN TEXTO')
palabra = "Murciégalo"
print(palabra)
print(len(palabra))
print("******************************")

# Método para si una palabra existe en un texto.
texto = "Este curso es de fundamentos de Python"
print('PALABRA RESERVADA (Keyword) "in" PARA SABER SI UNA PALABRA SE ENCUENTRA EN UN TEXTO')
print(texto)
# De esta manera podemos utilizar la palabra reservada in.
estaIncluida = "Python" in texto
print(estaIncluida) # No dará un dato de tipo Boolean True.
# Debemos tener en cuanta que la palabra que buscamos debe estar escrita de la misma forma.
print("******************************")

# Y para validar que una palabra no esta incluida en el texto podemos utilizar el "not in".
print('PARA VALIDAR QUE UNA PALABRA NO ESTA INCLUIDA EN NUESTRO TEXTO PODEMOS UTILIZAR "not in"')
# De esta manera podemos utilizar las palabras reservadas "not in".
noEstaIncluida = "Javascritp" not in texto
print(texto)
# Nos retornara un valor de tipo Boolean 'True'.
print(noEstaIncluida)
print("******************************")

# Manipulación de texto mayúsculas o minúsculas.
# Método para convertir un texto a MAYÚSCULA.
print('CONVIRTIENDO EL TEXTO A MAYÚSCULA CON EL MÉTODO "upper()"')
mayuscula = texto.upper() # Convertirá todo el texto en mayúscula.
print(mayuscula)

# Método para convertir un texto a minúscula.
print('CONVIRTIENDO EL TEXTO A MINÚSCULA CON EL MÉTODO "lower()"')
minuscula = texto.lower() # Convertirá todo el texto en minúscula.
print(minuscula)
print("******************************")

# Método para quitar los espacios antes y después de un texto.
print('PODEMOS QUITAR LOS ESPACIOS CON EL MÉTODO "strip()"')
espacioTexto ="     este es un texto con espacios al inicio y al final      "
# Imprimimos el texto original.
print(espacioTexto)
# Utilizamos el método "strip()" para quitar los espacios.
sinEspacios = espacioTexto.strip()
print(sinEspacios)
