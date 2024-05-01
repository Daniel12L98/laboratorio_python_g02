import funciones

nombre, apellido = funciones.nombre()
seguro = funciones.tipo_seguro()
edad = funciones.mayor_edad()

print("El nombre es:", nombre)
print("El apellido es:", apellido)
print("El tipo de seguro es:", seguro)
if edad:
    print("Es mayor de edad")
else:
    print("Es menor de edad")