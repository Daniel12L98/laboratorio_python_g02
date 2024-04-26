"""Programación funcional en Python"""

"""Requisitos
- Solicitar al usuario 4 números por consola
- Crear una función que devuelve cual es el número mayor de los 4 ingresados por el usuario
- Finalmente elevar al cubo el resultado y mostrarlo por consola
"""
a = int(input("Ingrese número 1: "))
b = int(input("Ingrese número 2: "))
c = int(input("Ingrese número 3: "))
d = int(input("Ingrese número 4: "))
def numero_mayor(a, b, c, d):
    return max(a, b, c, d)

cubo = numero_mayor(a, b, c, d) ** 3
print("El numero mayor es: {}".format(numero_mayor(a, b, c, d)))
print("El valor al cubo es: {}".format(cubo))
