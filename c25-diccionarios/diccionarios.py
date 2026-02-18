# Colecciones de datos diccionario.
"""
Los diccionarios en Python son una colección
poderosa y ordenada desde Python 3.7 que organiza
datos en pares clave-valor. Aquí verás cómo crearlos,
acceder a la información con corchetes y get,
modificarlos con asignación y update, eliminarlos
con pop y popitem, recorrerlos con for e items,
y trabajar con diccionarios anidados
"""

# Los diccionarios son ordenados.
# Son mutables (si se pueden modificar) y pueden tener diferentes datos.
# Se puede acceder por su llave (key), ya que tienen llave y valor.
# Y no puede tener claves duplicadas.

# Sintaxis básica para crear un diccionario clave-valor.
print("SINTAXIS BÁSICA PARA CREAR UN DICCIONARIO")
auto = {
    # llave   valor
    #  key    value
    "marca": "Renault",
    "modelo": "Clio",
    "año": 2025
}
print(auto)
print(type(auto))
print()

# Como podemos acceder a los valores del diccionario.
print("DE ESTA MANERA PODEMOS ACCEDER A LOS VALORES DEL DICCIONARIO")
# Con corchete podemos acceder a los valores del diccionario.
print(auto["marca"])
print(auto["año"])
print()

# También podemos acceder con el método get(llave).
print("ACCEDEMOS A LOS VALORES CON EL MÉTODO get(llave)") 
print(auto.get("marca"))
print(auto.get("modelo"))
print(auto.get("año"))
print()


# También podemos obtener solo las llaves de nuestro diccionario.
print("CON EL MÉTODO keys() PODEMOS OBTENER SOLO LAS LLAVES DE NUESTRO DICCIONARIO") 
# utilizamos el método keys().
print(auto.keys())
print()

# Y también podemos obtener solo los valores con el método values().
print("CON EL MÉTODO values() PODEMOS OBTENER SOLO LOS VALORES DEL DICCIONARIO")
# Utilizamos el método values().
print(auto.values())
print()

# También podemos modificar un valor en nuestro diccionario.
print("PODEMOS MODIFICAR LOS VALORES DE NUESTRO DICCIONARIO DE DOS FORMAS")
print("Modificación con sintaxis básica")
# Utilizando una sintaxis básica.
print("Diccionario original ", auto)
auto["año"] = 2015
print("Diccionario modificado ", auto)
print()

print("Modificación con el método update(llave - valor)")
print("Diccionario original ", auto)
# Debemos pasar un diccionario donde este la clave - valor a remplazar.
auto.update({"año": 2012})
# De igual manera con este método podemos agregar nuevas clave - valor. 
print("Diccionario modificado ", auto)
print()

# Formas de agregar nuevas llaves y valores.
print("FORMA DE AGREGAR NUEVAS LLAVES Y VALORES")
print("Sintaxis básica para agregar nuevos datos")
auto["puertas"] = 4
print(auto)
print()
# Utilizando el método update() para agregar datos llave - valor.
print("Utilizando el método update(llave - valor) para agregar datos")
auto.update({"color": "Gris"})
print(auto)
print()

# Formas de de eliminar datos de nuestro diccionarios.
print("FORMAS DE ELIMINAR DATOS DE NUESTRO DICCIONARIO")
# Utilizamos el método pop(llave).
print("Utilizando el método pop(llave) para eliminar un valor")
auto.pop("puertas")
print(auto)
print()

# Y para eliminar el ultimo elemento de nuestro
# diccionario podemos utilizar el método popitem().
print("Con popitem() podemos eliminar el ultimo elemento de nuestro diccionario")
auto.popitem()
print(auto)
print()

# También podemos recorre el diccionario con el ciclo for.
print("TAMBIÉN PODEMOS RECORRE NUESTRO DICCIONARIO CON EL CICLO for")
# Vamos a recorre las llaves (key).
print("Vamos a recorre las llaves (key)")
for k in auto:
    print(k)
print()

# Vamos a recorre los valores (values).
print("Vamos a recorre los valores (values)")
for v in auto.values():
    print(v)
print()

# De esta manera podemos recorre las llaves (key) y los values (values).
print("Con el método item() podemos obtener llaves y valores")
for k, v in auto.items():
    print(k, v)
print()

# Veremos diccionarios anidados.
print("AHORA VEREMOS DICCIONARIOS ANIDADOS COMO CREARLOS")
# Creamos nuestro diccionario.
familia = {
    "hijo1": {
        "nombre": "Samuel",
        "edad": 8
    },
    "hijo2": {
        "nombre": "Ana",
        "edad": 7
    },
    "hijo3": {
        "nombre": "Marcelo",
        "edad": 6
    }
}
print(familia)

print("De esta manera podemos mostrar los datos de nuestro diccionario")
# Esta seria la sintaxis para acceder a los valores
# de nuestro diccionario anidados.
print(familia["hijo1"]["nombre"])

