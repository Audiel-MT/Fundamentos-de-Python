# Creamos nuestras operaciones matemáticas.

# Suma.
def sumar(a, b):
    return a + b

# Resta.
def restar(a, b):
    return a - b 

# Multiplicación.
def multiplicar(a, b):
    return a * b

# Division.
def dividir(a, b):
    if b == 0:
        return "No se puede dividir entre ", b
    else:
        return a / b

# Cada función retornara el resultado
# de la operación matemática ya que tienen la
# palabra reservada 'return'. 