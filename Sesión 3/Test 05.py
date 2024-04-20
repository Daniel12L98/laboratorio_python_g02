"""Uso del flujo condional: if"""

edad = int(input("Ingrese su edad: "))

if 0 < edad < 18:
    print("Usted es menor de edad")
# Cuendo hay mas condicionales se usa elif
elif 18 <= edad < 65:
    print("Usted es una persona adulta")
elif 100 >= edad > 65:
    print("Usted es una persona adulta de la tercer edad")
# Cuando ya no se va a agregar mas condicionales se usa el else
else:
    print("Usted ha ingresado una edad incorrecta")
    