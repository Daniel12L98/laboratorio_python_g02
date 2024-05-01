def suma_de_digitos(numero):
    suma = 0
    while numero:
        suma += numero % 10
        numero //= 10
        return suma

def ingresar_numero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("El número introducido no es positivo")
        except ValueError:
            print("Introduce un valor válido")

numero_1 = ingresar_numero_positivo("Ingrese el primer número positivo: ")
numero_2 = ingresar_numero_positivo("Ingrese el segundo número positivo: ")
suma_de_digitos_1 = suma_de_digitos(numero_1)
suma_de_digitos_2 = suma_de_digitos(numero_2)
print(suma_de_digitos_1)
print(suma_de_digitos_2)
