"""Uso de flujo condicional: if"""

var_1 = int(input("Ingrese su primer dato numérico"))
var_2 = int(input("Ingrese su segundo dato numérico"))

if var_1 > var_2:
    print("El valor de var_1 es mayor que el segundo valor ingresado")
elif var_1 == var_2:
    print("Los valores ingresados son iguales")
else:
    print("El valor de var_1 no es mayor que la de var_2")