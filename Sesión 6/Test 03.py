"""
    Programación orientada a objetos en Python
    participación
Requerimientos:
- Crear clase alumno
- Debe tener un atributo de nacionalidad con valor "Peruano"
- Crear un método que indicará el promedio del alumno
- Crear un método que indicará si el alumno está aprobado o no de acuerdo a su promedio (>=11)
- Tendrá 3 notas, la nota inicial será de 0 para todos
- Obtener el nombre y distrito de residencia
"""

class Alumno():
    def __init__(self):
        self.nombre = "Juan"
        self.distrito_de_residencia = "Surco"
        self.nacionalidad = "Peruano"
        self.notas =[0, 9, 16]
    def promedio(self):
        return sum(self.notas)/len(self.notas)
    def aprobado(self):
        if self.promedio() >= 11:
            print("El alumno está aprobado")
        else:
            print("El alumno está desaprobado")


alumno_1 = Alumno()

print("El nombre del alumno es: {}".format(alumno_1.nombre))
print("El distrito de residencia del alumno es: {}".format(alumno_1.distrito_de_residencia))
print("El promedio del alumno es: {}".format(alumno_1.promedio()))
print("{}".format(alumno_1.aprobado()))