"""Manejo de errores"""
"""
Requisitos
- Crear una función aplicando excepciones donde el bloque del except va a considerar a los errors de división entre 0 
y el tipo de error.
- Los valores tienen que ser ingresados por consola.
"""

def division(a, b):
    try:
        resultado = a/b
    except (ZeroDivisionError, TypeError):
        print("No se pueden dividir estos valores")
    else:
        print(resultado)

a = int(input("valor 1: "))
b = int(input("valor 2: "))
division(a, b)
