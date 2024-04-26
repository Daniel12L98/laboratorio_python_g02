"""Usando las propiedades de cadenas o string"""

"""Métodos de string"""

cadena = "Python para la predicción de fraudes bancarios o de prestamos"

# cadena_sin_espacios = cadena.split(sep="a")
cadena_sin_espacios = cadena.split()

print("Cadena separada por espacios en blanco dentro del string: {}".format(cadena_sin_espacios))

for palabra in cadena_sin_espacios:
    print(palabra)
