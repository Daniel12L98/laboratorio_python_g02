class Alumnos:
    def __init__(self, nombre, edad, nota):
        self.nombre = nombre
        self.edad = edad
        self.nota = nota
    def datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Nota: {}".format(self.nota))
    def notas(self):
        if 11 <= self.nota <= 20:
            print("El alumno aprobó con {}".format(self.nota))
        elif self.nota >= 20:
            print("La nota no es válida")
        else:
            print("El alumno desaprobó con {}".format((self.nota)))

alumno_1 = Alumnos("Pedro", 14, 4)
alumno_2 = Alumnos("Patricia", 15, 19)
alumno_3 = Alumnos("Marco", 14, 9)

print("Los datos del primer alumno son los siguientes")
alumno_1.datos()
alumno_1.notas()
print(" ")
print("Los datos del segundo alumno son los siguiente")
alumno_2.datos()
alumno_2.notas()
print(" ")
print("Los datos del tercer alumno son los siguiente")
alumno_3.datos()
alumno_3.notas()