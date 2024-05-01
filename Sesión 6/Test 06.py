"""Gestión de excepciones"""
"""
Crear una función aplicando excepciones donde no se pueda
realizar una suma de diferentes tipos de datos
"""

def operaciones(a, b):
    try:
        resultado = a/b
    except TypeError:
        print("No se puede sumar un STR con un dato INT")
    except ZeroDivisionError:
        print("No se puede dividir entre cero!")
        resultado = 0  # Al resultado ya se le está asignando este valor de 0
        print("Resultado: {}".format(resultado))
    else:
        print(resultado)
# operaciones(40, "¡¡Hello Python!!")
# operaciones(100, 500)
operaciones(100, 0)