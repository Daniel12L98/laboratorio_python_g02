"""Pedir dos números positivos mediante terminal al usuario. Mostrar como salida el número cuya sumatoria de dígitos es
el mayor y los números cuya sumatoria de dígitos es menor que 10. Utilizar una o más funciones, según sea conveniente.
"""
def suma_digitos(numero):
    return sum(int(digito) for digito in str(numero))
def ingresa_numero_positivo(mensaje):
    while True:
        try:
            numero = int(input(mensaje))
            if numero > 0:
                return numero
            else:
                print("El número ingresado no es positivo")
        except ValueError:
            print("Ingrese un número válido")


# Solicitar el primer número positivo
#numero1 = ingresa_numero_positivo("Introduce el primer número positivo: ")

# Solicitar el segundo número positivo
#numero2 = ingresa_numero_positivo("Introduce el segundo número positivo: ")

