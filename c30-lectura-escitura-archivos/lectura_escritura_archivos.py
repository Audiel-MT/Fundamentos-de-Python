# Lectura y escritura de archivos de texto.
"""
Manipular archivos de texto con Python es clave
para guardar y recuperar información de forma segura.
Aquí verás, paso a paso, cómo usar la función integrada open,
los modos de apertura r, w, a y x, el bloque try/except
para errores y el contexto with que automatiza el cierre del archivo.
Además, se resuelve el detalle de los acentos con el parámetro
de codificación y el salto de línea con \n.
"""

# Esta seria la sintaxis básica para poder leer un archivo.
print("SINTAXIS BÁSICA PARA PODER LEER UN ARCHIVO")
# Utilizamos la función 'open()' y se le deben de pasar dos argumentos.
# 1 - el nombre del archivo.
# 2 - y modo con el cual queremos manipularlo el archivo.
# Lista de modos para manipular un archivo.
# r = lectura.
# w = write.
# a = agregar texto.
# x = crea un nuevo archivo.

# Inicializamos nuestra variable con el archivo y el modo.
f = open("archivo1.txt", "r")
# Imprimimos la variable y utilizamos la función 'readline()'
# para mostrar solo una linea.
print(f.readline())
# Cerramos el archivo para que no consuma memoria.
f.close()
print()

# utilizaremos try y except para capturar errores cuando el archivo no existe.
print("UTILIZAREMOS try except CUANDO EL ARCHIVO NO EXISTE")
try:
    f = open("nuevoArchivo.txt", "r")
    print(f.readline())
    f.close()
except FileNotFoundError:
    print("No se ha encontrado el archivo")
print()

# También podemos utilizar la palabra 'with', con ella podemos
# gestionar de manera segura y garantizar que se abra y cierre
# el archivo.
print("PALABRA RESERVADA with PARA ABRIR Y CERRA EL ARCHIVO DE UNA MANERA MAS FÁCIL")
try:
    # utilizamos 'with' para que se encargue de abrir y cerra el archivo
    # con la palabra reservada utilizamos menos código.
    with open("archivo1.txt", "r") as f:
        print(f.readline())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
print()

# Veremos como mostrar los acentos de las palabras con con
# el formato de texto 'utf-8' que es el estándar mas extendido
# en la web.
print("COMO PODEMOS MOSTRAR LOS ACENTOS CON EL ESTÁNDAR utf-8")
try:
    # Se agregara un nuevo argumento para mostrar los acentos.
    # Agregando el argumento 'utf-8' ya que es un estándar y lo
    # hace eficiente y compatible con multiples idiomas.
    with open("archivo1.txt", "r", encoding="utf-8") as f:
        # Con la función 'read()' podemos leer todo nuestro archivo.
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
print()

# Ahora veremos como escribir en un archivo.
print("VEREMOS LA FORMA DE ESCRIBIR EN UN ARCHIVO")
try: 
    # Utilizamos un nuevo archivo y un argumento
    # nuevo 'w' para escribir en el archivo
    # si utilizamos el archivo1 lo que hará es sobrescribir
    # el texto.
    with open("archivo2.txt", "w") as f:
        f.write("Este es el archivo2, de esta manera podemos escribir")
    with open("archivo2.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
print()

# Utilizaremos el argumento 'w' para ver como se sobrescribe el texto
# en nuestro archivo2.txt.
print("UTILIZAREMOS EL ARGUMENTO 'w' DE LA FUNCIÓN open() PARA SOBRESCRIBIR")
try:
    with open("archivo2.txt", "w") as f:
    # Aquí podemos ver como sobrescribe el texto de nuestro archivo2.txt
        f.write("Este texto esta sobrescrito en el archivo2.txt, el texto original es (Este es el archivo2, de esta manera podemos escribir)")
    with open("archivo2.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
print()

# Si necesitamos agregar texto a nuestros archivo utilizaremos el argumento 'a'.
print("SI NECESITAMOS AGREGAR TEXTO Y QUE NO SOBRESCRIBA UTILIZAREMOS EL ARGUMENTO 'a' EN NUESTRA FUNCIÓN open()")
# Agregaremos nuevo texto a nuestro archivo1.txt.
try:
    # Con el argumento 'a' podemos agregar mas texto y no lo sobrescribe
    # solo que pone el nuevo texto en el mismo renglón y lo pone unido a la ultima palabra
    # del texto que estaba.
    with open("archivo1.txt", "a") as f:
        f.write("Esta es un nuevo texto que no lo sobrescribe en nuestro archivo1.txt")
    with open("archivo1.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
print()

# Si queremos evitar que el nuevo texto que queremos añadir a un archivo
# este en el mismo renglón y unido con la ultima palabra de ese texto
# podemos utilizar un salto de linea '\n'.
print("CON PLECA INVERTIDA Y N PODEMOS AGREGAR TEXTO EN EL SIGUIENTE RENGLÓN")
try:
    # Debemos de validar que cuando vamos a escribir texto nuevo
    #  también debemos colocar el argumento 'utf-8' 
    # para no tener problema con los acentos. 
    with open("archivo1.txt", "a", encoding="utf-8") as f:
        # Colocamos la instrucción para hacer el salto de linea.
        f.write("\n")
        f.write("Este es un nuevo texto en el nuevo renglón")
    with open("archivo1.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    print("No se ha encontrado el archivo")
print()

# Ahora veremos como crear un archivo cuando este no se encuentre.
print("CREAREMOS UN ARCHIVO CON LA FUNCIÓN open() Y EL ARGUMENTO 'x'")
try:
    # Tratamos de abrir nuestro archivo y leerlo.
    with open("archivo3.txt", "r", encoding="utf-8") as f:
        print(f.read())
except FileNotFoundError:
    # Utilizamos la siguiente sintaxis para crear un nuevo archivo.
    open("archivo3.txt", "x")
    print("No se ha encontrado el archivo")