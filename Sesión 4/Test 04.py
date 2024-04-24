"""Usando las propiedades de cadenas o string"""


"""Replace"""
cadena = "Conexión a base de datos con Python"

cadena_2 = cadena.replace(cadena[0:6], "pppppp")
print("Cadena con reemplazo, tiene el siguiente valor actualizado: {}".format(cadena_2))

"Eliminación de espacios en blanco de mi cadena (despues)"
cadena_3 = "Conexión a base de datos con python"
cadena_4 = cadena_3.rstrip()
print(cadena_3)
print("Mi cadena actualizada sin espacios en blanco es el siguiente: {}".format(cadena_4))
