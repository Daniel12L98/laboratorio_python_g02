"""Gestión de excepciones"""

"""Estructuras y uso"""
"""
try:
    bloque de código 1
except 'excepción_1'
    bloque de código 2
else:
    bloque de código 3
"""

def division(a, b):
    try:
        resultado = a/b
    except ZeroDivisionError:
        print("No se puede dividir entre cero!")
    else:
        print(resultado)

division(40, 0) # La función con los valores
division(190, 100)