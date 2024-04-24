"""Usando las propiedades de cadenas o string"""

"""
Requisitos:
-Ingresar tu nombre y apellido por consola (cada valor tiene que estar en una variable distinta)
-Concatenar ambos valores en una sola variable
-Obtener y mostrar el tamaño de tu nombre completo
-Imprimir el resultado final todo en mayuscula
-Indicar mediente condicionales si el tamaño del nombre es mayor o no al apellido (ingresar solo para este caso el apellido paterno)
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
nombre_completo = "{} {}".format(nombre, apellido)
print(nombre_completo)
print("El tamaño del nombre es: ",len(nombre_completo))
print("El resultado en mayúscula es: {}".format(nombre_completo.upper()))
if len(nombre) > len(apellido):
    print("El tamaño del nombre es mayor que el del apellido")
else:
    print("El tamaño del nombre no es mayor que el del apellido")
