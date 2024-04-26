"""Usando las propiedades de cadenas o string"""

"""lstrip: Desaparece el espacio en blanco anterior a la cadena"""

cadena = "                  Conexión a Base de Datos con Python"

cadena_2 = cadena.lstrip()
print(cadena)
print("Mi cadena actualizada sin espacios en blanco es: {}".format(cadena_2))
