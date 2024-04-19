"""Conversión de datos"""

"""De string a tipo de dato int (entero)"""


var_1 = "8000"
var_2 = 35000
var_3 = 400.0

suma_1 = var_2 + var_3
print("El valor de suma_1 es: {}".format(suma_1))

# Esta suma no es posible por ser un valor string y otro ser un valor entero
# suma_2 = var_1 + var_2
# print("El valor de suma_2 es: {}".format(suma_2))

suma_3 = int(var_1) + var_2
print("El valor de suma_3 es: {}".format(suma_3))

"""Suma de dos variables: int + float"""

suma_4 = var_2 + var_3
print("El valor de suma_4 es: {}".format(suma_4))

var_4 = int(suma_4)
print(var_4)

var_5 = "700"
var_6 = 40000
var_7 = 40.68

"""Suma de las tres variables como strintg"""
suma_5 = var_5 + str(var_6) + str(var_7)
print("El valor de suma_5 es: {}".format(suma_5))
