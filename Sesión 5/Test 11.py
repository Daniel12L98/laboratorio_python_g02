"""Requisitos
- Un usuario ingresará 2 numeros por consola
- En una función obtener si el segundo numero ingresado es multiplo del primo o viceversa
- Retornar quien fue multiplo de quien
"""

a = int(input("Ingresar el primer número: "))
b = int(input("Ingresar el segundo número: "))

def multiplo (a, b):
    if a % b == 0:
        return print(f"{a} es multiplo de {b}")
    if b % a == 0:
        return print(f"{b} es multiplo de {a}")
    else:
        return print("Los números no son multiplos")
print(multiplo(a, b))
