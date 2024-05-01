from funciones import suma as oper_1, multiplicacion as oper_2     #Para cambiar el nombre de las funciones

var_1 = int(input("Ingresar tu primer valor: "))
var_2 = int(input("Ingresar tu segundo valor: "))

sum = oper_1(var_1, var_2)
print("El resultado de sus dos valores es: {}".format(sum))

mul = oper_2(var_1, var_2)
print("El resultado de sus dos valores es: {}".format(mul))