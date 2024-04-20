"""
Requisitos:

- Dentro de una empresa se va a solicitar pedir nombre y apellido del empleado.
- Distrito de residencia
- Sueldo y el cálculo del bono final del año, que será el triple de el sueldo mensual menos el 10% del sueldo
- Todos estos datos van a estar asignados en una lista
- Por asignación múltiple de variables, asignar los valores de esta lista a 3 nuevas variables
- Mostrar por la terminal el mensaje de "'Nombre' 'apellido' recibirá 'bono' soles de fin de año.
"""

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")
distrito_de_residencia = input("Ingrese su distrito de residencia: ")
sueldo = input("Ingrese su sueldo: ")

bono = int(sueldo) * 3 - int(sueldo) * 0.1

lista = [nombre, apellido, distrito_de_residencia, sueldo]
nombre, apellido, distrito_de_residencia, sueldo = lista

print("{} {} recibirá {} soles de fin de año".format(nombre, apellido, bono))

