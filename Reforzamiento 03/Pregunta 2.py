def cuadrados (a, b):
    for num in range(a, b + 1):
        print("El cuadrado de {} es: {}".format(num, num ** 2))

def numero(a, b):
    try:
        cuadrados(min(a, b), max(a, b))
    except ValueError:
        print("Los números ingresados no son válidos")


a = int(input("Ingrese en primer número: "))
b = int(input("Ingrese el segundo número: "))

numero(a, b)