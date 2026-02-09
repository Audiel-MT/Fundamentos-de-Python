# Colecciones de datos Tuplas.
"""
Las tuplas en Python son una base sólida para escribir
código claro y seguro. Aquí aprenderás, paso a paso, 
cómo crear, acceder y operar con tuplas: colecciones ordenadas
e inmutables que permiten elementos duplicados, admiten tipos mixtos
y se pueden desempaquetar, concatenar, multiplicar e iterar.
Además, verás el truco para “modificarlas” convirtiéndolas
en lista y de vuelta a tupla.
"""
# Las tuplas son ordenada.
# Son inmutables (no se pueden modificar sus valores).
# Se puede acceder por su indice.
# Y pueden tener datos duplicados.

# Para crear una tupla se utiliza los paréntesis ().
tecnologias = ("Python", "Java", "Go")

# Imprimimos toda la tupla.
print("Tupla: ", tecnologias)
print()

print("MOSTRAMOS UN VALOR DE LA TUPLA POR SU INDICE")
# En las tuplas podemos acceder por su indice a cada valor.
print("Indice 1 es igual a ", tecnologias[1])
print()

# Creamos una nueva tupla con datos duplicados.
framework = ("Django", "Node.js", "vue", "Svelte", "Django")
print("IMPRIMIMOS LA TUPLA framework CON UN DATOS DUPLICADO")
print(framework)
print()

# También podemos utilizar la función
# len() para saber cuantos datos tienen.  
print("UTILIZANDO LA FUNCIÓN len() PARA SABER CUANTOS DATOS TIENE NUESTRAS TUPLAS")
print("Tupla de tecnologia tiene la cantidad de ",len(tecnologias), " valores")
print("Tupla de framework tiene la cantidad de ",len(framework), " valores")
print()

# Debemos tener algo muy en cuanta si queremos hacer una tupla con solo un dato.
print("TUPLA CON SOLO UN DATO")
# Creamos nuestra tupla.
tupla_uno = ("uno")
# Imprimimos el tipo de dato con type().
print("Tipo de dato de la tupla uno: ", type(tupla_uno))
# Nos da que es de tipo (str) que es un texto.

# Para poder crear una tupla de solo un elemento
# le debemos de agregar una coma (,) al final de nuestro valor.
tupla_dos = ("dos",)
print("Tipo de dato de la tupla dos: ", type(tupla_dos))
print()

# En las tuplas también podemos tener diferentes tipo de datos.
print("LAS TUPLAS TAMBIÉN PUEDEN TENER DIFERENTES TIPOS DE DATOS")
tupla = ("Perro", 8, False)
# Imprimimos la tupla y el tipo de datos que es.
print("Tupla con diferentes tipos de datos: ", tupla)
print("Tipo de dato: ", type(tupla))
print()

# También podemos desempaquetar una tupla.
print("DESEMPAQUETAREMOS UNA TUPLA")
# Podemos desempaquetar las siguientes estructuras de datos.
# - Lista
# - Tupla
# - Conjuntos.
desempaquetar = (12, "gato", True)
print("Tupla a desempaqueta ", desempaquetar)
# creamos tres variables.
x, y, z = desempaquetar
print("DATOS DESEMPAQUETADOS")
print(x)
print(y)
print(z)
print()

# Para unir dos tuplas lo podemos hacer de la siguiente forma.
print("UNIR DOS TUPLAS")
# Creamos las tuplas.
tuplaUno = (1, 2, 3)
tuplaDos = (3, 5, 6)
print("Tupla uno ", tuplaUno)
print("Tupla dos ", tuplaDos)
# Lo podemos hacer con el signo de suma (+)
# para concatenar las dos tuplas.
tuplaTres = tuplaUno + tuplaDos
print("Tuplas concatenadas: ", tuplaTres)
print()

# Podemos duplicar los datos de una tupla.
print("TAMBIÉN PODEMOS DUPLICAR LOS DATOS DE UNA TUPLA CON EL OPERADOR (*)")
print(tuplaUno * 2)
# Imprimirá dos veces los valores, pero no podremos acceder a
# los valores nuevos por su indice, solo se puede acceder a los
# valores por defecto de la tupla.
print()

# Al igual que las litas podemos iterar las tuplas.
print("TAMBIÉN PODEMOS RECORRE UNA tupla CON for")
for i in tuplaTres:
    print(i)
print()
# Recordemos que las tuplas son inmutables 
# (no se pueden modificar cuando ya esta inicializadas).

# Para modificar una tupla, la podemos convertir en una
# lista y después trasformarla en tupla de nuevo.
print("PARA MODIFICAR UN VALOR DE UNA tupla PODEMOS HACER UN CASTING A lista")
# creamos nuestra tupla.
tupla_modificar = (2, "hola", 7.2, True)
print("Imprimimos la tupla: ",tupla_modificar)
# Realizamos el casting de la tupla a lista.
lista_comodin = list(tupla_modificar)
print("Imprimimos la lista: ",lista_comodin)
# Hacemos el cambio en nuestra lista.
lista_comodin.append("Python")
# realizamos el casting a una tupla.
tupla_modificar = tuple(lista_comodin)
# Imprimimos el resultado.
print("Tupla ya modificada: ", tupla_modificar)