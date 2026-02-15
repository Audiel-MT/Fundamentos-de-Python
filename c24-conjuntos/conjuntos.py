# Colecciones de datos conjuntos.
"""
Domina los conjuntos en Python con ejemplos claros y prácticos.
Aprende qué es un set, cómo evitar duplicados de forma automática
y cuáles son los métodos clave para agregar, buscar, eliminar
y combinar elementos. Además, entiende por qué el orden no está
garantizado y cómo aprovechar operaciones como
unión, intersección y diferencia.
"""

# Los conjuntos no son ordenados.
# Son mutables (si se pueden editar) y pueden tener diferentes tipos de datos.
# No se puede acceder por su indice (se accede por su valor).
# Y no puede tener valores duplicados.

# Sintaxis básica para crear un conjunto son los corchetes ( {} ).
frutas = {"Manzana", "Naranja", "Mandarina", "Naranja"}
print(frutas)
print(type(frutas))
print()

# Lo conjuntos no pueden mostrar valores duplicados.
print("LOS CONJUNTOS (set) NO PUEDEN TENER VALORES REPETIDOS")
# Solo muestra el valor 'naranja' una vez. 
print(frutas)
print()

# Utilizaremos la función len() para ver cuantos valores tiene.
print("UTILIZAMOS LA FUNCIÓN len() PARA VER CUANTOS VALORES TIENE")
print("Conjunto de frutas tiene la cantidad de: ", len(frutas))
# Nos dará el valor de 3, ya que como un valor se repite.
print()


# Creamos un nuevo conjunto.
conjunto = {"Python", 3.1416, True}
# Los conjuntos pueden tenes diferentes datos.
print("LOS CONJUNTOS PUEDEN TENER DIFERENTES TIPOS DE DATOS") 
print("Conjunto con diferentes datos: ", conjunto)
print("Tipo de dato: ",type(conjunto))
print()

# De esta manera podemos recorre nuestro conjunto.
print("TAMBIÉN PODEMOS RECORRE UN conjunto CON UN for")
# Los valores nunca tendrán el mismo orden.
for i in conjunto:
    print(i)
print()

# También podemos validar si un elemento 
# esta en nuestro conjunto
# o también podemos preguntar si no esta.
print("VALIDANDO SI EL VALOR 'Naranja' ESTA EN NUESTRO CONJUNTO fruta")
print("Naranja" in frutas)
# Validamos un datos que no este en nuestro conjunto.
print("VALIDAMOS QUE NUESTRO DATO 'Pera' NO SE ENCUENTRA EN NUESTRO CONJUNTO fruta")
print("Pera" not in frutas)
print()

# También podemos desempaquetar los conjuntos.
print("DESEPAQUETAREMOS UN CONJUNTO")
print("conjunto que desenpaquetaremos: ", conjunto)
# creamos tres variables.
x, y, z = conjunto
print("DATOS DESEMPAQUETADOS")
print(x)
print(y)
print(z)
print()

# Métodos para agregar valores nuevos a un conjunto.
print("MÉTODOS PARA AGREGAR VALORES A UN CONJUNTO")
print("Método para agregar un valor en un conjunto add(valor)")
print("Conjunto original ", frutas)
# Hacemos referencia a nuestro conjunto
# y agregamos un elemento que no este repetido.
frutas.add("Pera")
print("Conjunto modificado ", frutas)
print()

# Con el método update(nuevo conjunto) podemos agregar mas de 1 elemento.
print("Método para agregar varios valores en un conjunto update(valor1, valor2)")
print("Conjunto original ", frutas)
# Hacemos referencia a nuestro
# conjunto frutas y utilizamos 
# el nuevo método update() pasándole
# una nueva Lista, tupla o conjunto.
lista = ["Fresa"]
tupla = ("Pera",)
# Agregamos la lista la tupla y el conjunto 
frutas.update(lista, tupla, conjunto)
print("Conjunto modificado ", frutas)
print()

# Veremos métodos para remover valores en los conjuntos.
print("MÉTODOS PARA ELIMINAR VALORES DE UN CONJUNTO")
# Método que podemos utilizar es remove(valor).
print("Método que podemos utilizar para eliminar un valor remove(valor)")
print("Conjunto original ", frutas)
# Utilizamos el método remove(valor)
# y le pasamos el valor a eliminar de
# nuestro conjunto.
frutas.remove("Fresa")
print("Eliminamos el valor de Fresa")
# Si no colocamos un valor que exista entre
# paréntesis nos dará un error.
print("Conjunto modificado ", frutas)
print()

# Otro método que también podemos 
# utilizar para eliminar valores es discard(valor) 
print("Método que podemos utilizar para eliminar valores discard(valor)")
print("Conjunto original ", frutas)
# Utilizamos el método discard(valor)
# con el valor que deseamos eliminar
# solo se puede eliminar un valor.
frutas.discard("Python")
# Con este método no tenemos inconveniente
# que si el valor no existe nos dará un error
# este método va ignorar la instrucción.
frutas.discard("Pizza")
print("Eliminamos el valor de 'Python' y tratamos de eliminar un valor que no existe 'Pizza'")
print("Conjunto modificado ", frutas)
print()

# Otro método que podemos utilizar es el pop().
print("Método que podemos utilizar para eliminar un elemento aleatorio pop()")
# Con este método al no tener indice en nuestro
# conjunto elimina un valor aleatorio.
print("Conjunto original ", frutas)
# Utilizamos el método pop().
frutas.pop()
print("Conjunto modificado ", frutas)
print()

# También esta el método clear() este
# elimina todo los valores de nuestro conjunto.
print("Método para eliminar todo los valores de un conjunto clear()")
print("Conjunto original ", frutas)
# Conjunto utilizando el método clear().
frutas.clear()
print("Conjunto modificado ", frutas)
print()

# utilizaremos métodos entre conjunto 
# que en matemática son muy usados.
print("MÉTODOS MUY UTILIZADOS ENTRE CONJUNTOS EN MATEMÁTICA")
# Creamos unos conjuntos.
a = {"a", "b", "c"}
b = {"c", "d", "e"}

# Utilizamos el primer método union(conjunto).
print("Método union() para unir dos conjuntos")
print("Conjunto a ", a)
print("Conjunto b ", b)
# Con el método union(conjunto) podemos
# unir dos conjuntos. 
c = a.union(b)
print("Conjunto utilizando el método union()", c)
print()

print("Método intersection() para ver que datos si se repiten en ambos conjuntos")
print("Conjunto a ", a)
print("Conjunto b ", b)
# Este método intersection() nos dará
# el único valor que se repite en ambos conjuntos.
i = a.intersection(b)
print("Conjunto utilizando el método intersection()", i)
print()

print("Método diferencia() para validar son diferentes de los conjuntos que comparemos")
print("Conjunto a ", a)
print("Conjunto b ", b)
# Con este método obtendremos los 
# valores que no son iguales en ambos conjuntos.
d = a.difference(b)
print("Conjunto utilizando el método difference()", d)
print()