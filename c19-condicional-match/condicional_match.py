# Condicional match.

"""
La sentencia match de Python 3.10 simplifica el control de flujo
con una sintaxis clara y legible. Si vienes de otros lenguajes,
se siente similar a un switch, pero con el estilo Python.
Aquí verás cómo sustituir cadenas de if, elif, else por casos bien
definidos con case y cómo usar el comodín _ para capturar lo no contemplado.
"""

# Con esta sentencia lo podemos utilizar como un if - elif - else.

dia = 10
# Con esta sentencia el código se ve mas limpio.
match dia: # Valida si la variable es igual con una caso.
    case 1:
        print("Hoy es Lunes") # Si la variable es 1 mostrara esto.
    case 2:
        print("Hoy es martes") # Si la variable es 2 mostrara esto.
    case 3:
        print("Hoy es miércoles") # Si la variable es 3 mostrara esto.
    # Cuando nuestra variable no tenga un dato correcto
    # lo podemos tomar de la siguiente manera como si fuera else
    # se utiliza un guion bajo (_)
    case _:
        print("No coincide con ningún dato de los anteriores")
        print()


print("* EJERCIÓ PROPUESTO *")
# Variable a comparar en la sentencia match.
mes = "febro"

# Estructura match para validar nuestra variable.
match mes: 
    case "enero": # En cada 'case' colocamos el nombre de un mes.
        print("El mes de tu variable es ", mes)
        print("numero del mes 1")
    case "febrero":
        print("El mes de tu variable es ", mes)
        print("numero del mes 2")
    case "marzo":
        print("El mes de tu variable es ", mes)
        print("numero del mes 3")
    case "abril":
        print("El mes de tu variable es ", mes)
        print("numero del mes 4")
    case "mayo":
        print("El mes de tu variable es ", mes)
        print("numero del mes 5")
    case "junio":
        print("El mes de tu variable es ", mes)
        print("numero del mes 6")
    case "julio":
        print("El mes de tu variable es ", mes)
        print("numero del mes 7")
    case "agosto":
        print("El mes de tu variable es ", mes)
        print("numero del mes 8")
    case "septiembre":
        print("El mes de tu variable es ", mes)
        print("numero del mes 9")
    case "octubre":
        print("El mes de tu variable es ", mes)
        print("numero del mes 10")
    case "noviembre":
        print("El mes de tu variable es ", mes)
        print("numero del mes 11")
    case "diciembre":
        print("El mes de tu variable es ", mes)
        print("numero del mes 12")
    case _: # Y si no hay ningún mes en la variable, imprimirá lo del guion bajo.
        print("El dato que ingresaste no coincide con ningún mes")
        print("Dato almacenado en la variable ", mes)