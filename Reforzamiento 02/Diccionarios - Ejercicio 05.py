var_1 = {"nombre": "Pedro", "edad": 23, "salario": 3500}
var_1["dni"] = 13648592
# print("El valor del salario es:", var_1["salario"])
del var_1["edad"]
# print("El nuevo diccionario es: {}".format(var_1))
var_2 = list(var_1)
print("La nueva lista es: {}".format(var_2))
print("El tipo de dato de la lista es:", type(var_2))
