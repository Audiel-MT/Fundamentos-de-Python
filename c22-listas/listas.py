# Colección de datos listas.
"""
Aprende a dominar las listas en Python con ejemplos
simples y prácticos. Entenderás qué son, cómo funcionan
los índices, cómo modificar elementos y qué métodos usar
para agregar, eliminar, ordenar y unir colecciones.
Con estas bases, escribirás código más claro y efectivo.
"""
# Las lista son una colección de datos ordenados
# que se pueden modifica y permiten datos duplicados.

# Sintaxis para crear una lista es con corchetes ( [] ).
frutas = ["Manzana", "Naranja", "Mandarina", "Mango"]
# Imprimimos nuestra lista.
print("VALORES QUE TIENE NUESTRA LISTA")
print(frutas)
# Imprimimos el tipo de dato que es nuestra lista con 'type()'.
print(type(frutas))
print()

print("PODEMOS IMPRIMIR UN VALOR EN ESPECIFICO COLOCANDO SU INDICE")
# Los indices comienzan en 0.
print("Imprimimos el indice 1 que es igual a Naranja")
print(frutas[1])
print()

print("LAS LISTA SE PUEDEN MODIFICAR")
# Podemos agregar, eliminar y modificar los valores
# de la lista con diferentes tipos de datos.
print("Sobrescribimos el valor de ", frutas[1], "por el valor de Mango")
print("Lista original: ", frutas)
# Ingresamos el nuevo valor por el indice que necesitamos.
frutas[1] = "Mango"
# Imprimimos la lista ya modificada.
print("Lista modificada: ", frutas)
print()

print("lAS LISTAS PUEDEN TENER ELEMENTOS DUPLICADOS")
# Las listas nos permiten tener elementos duplicados.
print("Agregaremos el valor de Mango de nuevo")
# Este dato se lo agregamos donde declaramos la lista (fruta) y sus valores.
print("Lista con datos duplicados: ",frutas)
print()

print("TAMBIÉN PODEMOS AGREGAR OTROS TIPOS DE VALORES EN LAS LISTAS")
# Ademas podemos agregar otros tipos de datos (int, float, boo) en la misma lista.
# Creamos una lista con valores diferentes.
lista = ["Mango", 5, True]
# mostramos la lista.
print("Lista con diferentes tipos de datos: ", lista)
# Validamos que tipo de dato es (lista).
print(type(lista))
print()

print("TAMBIÉN PODEMOS VALIDAR CUANTOS DATOS TIENE UNA LISTA CON LA FUNCIÓN len")
# Con la función len() podemos saber la cantidad de datos que tiene nuestra lista.
print("La cantidad de elemento que tiene la lista frutas es de: ",len(frutas))
print("La cantidad de elemento que tiene la lista es de: ",len(lista))
print()

print("EN LAS LISTA TAMBIÉN PODEMOS UTILIZAR EL slicing")
# Esto nos permite tal y como lo hacíamos en los textos
# recórtalos de igual manera lo podemos hacer con las listas.
print("Lista de frutas: ",frutas[0:2]) 
# Recordemos que no se imprimirá el valor
# que se encuentra en el indice 2.
print("IMPRIMIMOS LA SEGUNDA lista")
print("lista con diferentes datos: ", lista[1:3])
print()

print("TAMBIÉN PODEMOS VALIDAR SI DENTRO DE UNA LISTA EXISTE DETERMINADO VALOR CON in")
# Con la palabra reservada (in) podemos validar si un
# elemento existe dentro de una lista.
if "Mango" in frutas:
    print("El Mango esta dentro de la lista fruta")
    print()

# Creamos una nueva lista.
vehiculos = ["Auto", "Moto", "Avion"]

print("MÉTODOS AGREGAR DATO EN UNA LISTA")
# Veremos métodos que nos facilitaran agregar valores a una lista.
# append (Este nos ayuda a agregar un nuevo dato)
print("Método para agregar un valor en una lista append(valor)")
print("Lista original ", vehiculos)
vehiculos.append("Barco")
# Imprimimos la lista de vehículos.
print("Lista modificada con el método append ",vehiculos)

# insert con este método podemos agregar un valor
# pero con este le podemos decir en que indice lo
# podemos colocar.
print("Método para agregar un valor por medio de un indice insert(indice, valor)")
# Insertaremos en la segunda posición el valor de Bicicleta
# en la lista vehículos.
print("Lista original ", vehiculos)
vehiculos.insert(1, "Bicicleta")
# Imprimimos la lista vehículos.
print("Lista utilizando el método insert ", vehiculos)
print()

print("MÉTODOS PARA REMOVER VALORES EN UNA LISTA")
# Veremos métodos que nos facilitaran eliminar valores de una lista.
print("Método para eliminar un valor por su valor remove(valor)")
print("Lista original ", vehiculos)
# Eliminaremos el valor (Auto) que se encuentra en el indice 0.
vehiculos.remove("Auto")
# Mostramos la lista modificada.
print("Lista modifica con el método remove ", vehiculos)

# de igual manera podemos eliminar valores con el método pop()
print("Método para eliminar un valor por su indice pop(indice)")
# Eliminaremos el valor de Moto que se encuentra en el indice 1.
print("Lista original ", vehiculos)
# Lista modificada con el método pop()
vehiculos.pop(1)
print("Lista modificada con el método pop ", vehiculos)
print()

print("MÉTODO PARA ORDENAR")
# Con este podemos ordenar números, texto por orden alfabético.  
print("Lista original ", vehiculos)
print("Utilizando el método sort() para ordenar la lista")
vehiculos.sort()
print("Lista modificada con el método sort ", vehiculos)

# También tenemos el método reverse() con el 
# podemos ordenar de manera contraria nuestra lista.
print("Lista original ", vehiculos)
print("Utilizamos el método reverse() para ordenar de manera inversa una lista")
vehiculos.reverse()
print("Lista modifica con el método reverse ", vehiculos)
print()

print("MÉTODO PARA UNIR LISTA")
# Con este método podemos unir dos listas.
# Creamos dos listas nuevas.
coleccion1 = [1, 2, 3]
coleccion2 = [4, 5, 6]

print("Colección 1 ", coleccion1)
print("Colección 2 ", coleccion2)

# Lo podemos hacer con el operador aritmético de suma (+)
# para concatenar las dos lista creando una tercera lista.
coleccion3 = coleccion1 + coleccion2
# Imprimimos la nueva lista.
print("Utilizamos el operador aritmético suma (+) ", coleccion3)

print("Utilizamos el método extend()")
# Utilizamos el método para modificar la coleccion1.
coleccion1.extend(coleccion2)
# Imprimimos nuestra coleccion1.
print("Lista modificada con el método extend() ", coleccion1)