# Bucle for.
"""
Domina el bucle for en Python para recorrer secuencias
de forma clara y eficiente. Aquí verás cómo iterar cadenas
y listas, usar break, continue y else, trabajar con range y
crear bucles anidados. Además, aprenderás a usar pass cuando
aún no tienes definida la lógica interna.
"""

print("UTILIZAMOS EL BUCLE for PARA RECORRE LA PALABRA python")
# Variable que vamos a recorre.
palabra = "python"

# Creamos el bucle for.
# de la variable (palabra) le pasa un caracter a la variable letra.
for letra in palabra: 
    print(letra) # No mostrara letra por letra de la variable.
print()


print("UTILIZAMOS EL BUCLE for PARA RECORRE UNA lista")
# Creamos una variable de tipo lista.
frutas = ["Manzana", "Naranja", "Kiwi"]

# Ahora vamos a recorre la lista llamada frutas
for fruta in frutas:
    print(fruta)
print()

"""
Igual que el bucle while también podemos
utilizar las palabras reservadas 
-break
-continue
-pass
"""

print("UTILIZAMOS EL BUCLE for CON LA PALABRA RESERVADA break")
# Creamos el bucle for, siempre utilizando la lista de frutas.
for fruta in frutas:
    # Creamos la condición donde se ejecutara el break.
    if fruta == "Naranja":
        print("Ingreso a la condición y termina el bucle for")
        break
    print(fruta)
print()

print("UTILIZAMOS EL BUCLE for CON LA PALABRA RESERVADA continue")
# Creamos el bucle for con la lista a recorre de frutas.
for fruta in frutas:
    # Creamos la misma condición solo que ahora utilizaremos la palabra continue.
    if fruta == "Naranja":
        print("Ingresa a la condición y se salta ")
        continue
    print(fruta)
print()

print("TAMBIÉN PODEMOS UTILIZAR LA SENTENCIA else EN EL BUCLE for")
# Podemos utilizar else como el en ciclo while.
for fruta in frutas:
    if fruta == "Naranja":
        print("En este ciclo utilizamos la sentencia 'else' al finalizar el recorrido")
        continue
    print(fruta)
# Esta sentencia se imprimirá al finalizar el ciclo for.
else:
    print("El ciclo 'for' a finalizado")
print()

# También podemos utilizar numero con la función 'range()'.
print("UTILIZAREMOS LA FUNCIÓN range() PARA UTILIZAR NUMERO EN NUESTRO BUCLE for")
# Creamos nuestro bucle for, con la función range().
for i in range(10):
    # Imprimimos los valores por consola.
    print(i)
    # La función 'range' no incluye el valor hasta donde le asignemos.
print()

# Podemos utilizar la función range pasándole de donde queremos qu inicie
# y hasta donde queremos que termine sin incluir ese numero.
print("FUNCIÓN range() PASÁNDOLE EL NUMERO DE INICIO Y EL NUMERO FINAL SIN INCLUIRLO")
# Creamos nuestro bucle.
for i in range(2, 12):
    print(i) # Mostrara los números del 2 hasta el 11.
print()

# De igual manera podemos utilizar range() 
# para mostrar valores en específicos de un rango.
print("UTILIZAREMOS LA FUNCIÓN range() PARA MOSTRAR VALORES DE 3 EN 3")
# Creamos el ciclo for.
# Le damos un inicio en 0.
# que llegue hasta el 10.
# con un paso de 3 en el rango de 0 al 10.
for i in range(0, 10, 3): 
    print(i)
print()

# Creamos otra lista para utilizarla con la lista de frutas
adjetivos = ["Rica", "Saludable"]
# y utilizaremos un bucle anidado.
print("UTILIZAREMOS LOS BUCLE for ANIDADOS")
# Utilizaremos un bucle dentro del otro
# para poder utilizar las dos listas.
for adjetivo in adjetivos:
    for fruta in frutas:
        print(fruta, adjetivo)
        # Se ejecutara dos veces los adjetivo con cada fruta
        # en total seria 2 * 3 = 6.
print()

# Reto.
print("RETO DE PLATZI")
# Listas que vamos a utilizar.
f = ["Manzana", "Naranja", "Kiwi"]
a = ["Rica", "Saludable"]
# Manzana rica.
# Manzana saludable.
# Naranja rica.
# Naranja saludable.
# Kiwi rica.
# Kiwi saludable.
for fr in f:#Iteramos la lista de las frutas
    for ad in a:#Iteramos la lista de los adjetivos.
        print(fr, ad) # Mostramos la fruta (fr) y el adjetivo (ad)
else:#Mostramos un mensaje que a finalizado la iteración de la lista.
    print("A finalizado la iteración del bucle principal")
print()

# Para evitar errores en nuestro código
# también podemos utilizar la palabra reservada pass.
print("UTILIZAMOS LA PALABRA RESERVADA pass PARA EVITAR ERRORES")
for i in range(0, 100):
    pass
# Utilizando esta palabra nuestro código se ejecuta sin ningún error.