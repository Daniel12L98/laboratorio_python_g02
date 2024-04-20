"""Uso del flujo condional: if"""
"""if ternario"""

"""
Requisitos:
- Ingresar por teclado el sueldo de un empleado
- Si el sueldo es mayor a 3000, imprimir "Su sueldo no tiene bonificación"
- Caso contrario: "Su sueldo tiene bonificación este año"
"""

sueldo = input("Su sueldo es: ")

if sueldo > str(3000):
    print("Su sueldo no tiene bonificación")
else:
    print("Su sueldo tiene bonificación este año")

final = "Su sueldo no tiene bonificación" if sueldo > str(3000) else "Su sueldo tiene bonificación este año"
print(final)
