# ¿Cómo funciona la asignación múltiple en Python?
"""
Asignar varios valores a varias variables en una sola línea
es directo y legible. Se hace por posición, lo que mejora
la claridad del código y evita errores al repetir líneas.
"""

"""
Posicionamos las tres variable en la misma linea
y de igual manera se colocamos los valores en la misma
siempre separados por comas.
"""
x, y, z = "Manzana", "Naranja", "Banana"
print(x,y,z)

# De esta manera podemos asignar el mismo valor a 3 variables diferentes.
a = b = c = "Mandarina"
print(a,b,c)

# También podemos utilizar el signo ( + ) para concatenar texto con una variable.
print("Mi fruta favorita es " + y)
# También lo podemos utilizar para concatenar espacios en blanco entre nuestras variables.
print(a + " " + c)

# Con datos de tipo numero tenemos que tener cuidado por que el signo mas ( + ) tomara otra indicaciones.
d = 5
e = 10
# Si tratamos de concatenar lo que ara sera la operación matemática. 
print(d + e)
