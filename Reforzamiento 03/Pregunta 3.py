def suma_digitos(a):
    suma = 0
    while a > 0:
        suma += a % 10
        a //= 10
    print("La suma de los dígitos del número ingresado es:", suma)

a = int(input("Ingrese un número: "))
suma_digitos(a)