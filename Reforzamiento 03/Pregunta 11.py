class Persona:
    def __init__(self, nombre, edad, sueldo):
        self.nombre = nombre
        self.edad = edad
        self.sueldo = sueldo
    def mostrar_datos(self):
        print("Nombre: {}".format(self.nombre))
        print("Edad: {}".format(self.edad))
        print("Sueldo: {} soles".format(self.sueldo))
    def mayor_edad(self):
        if self.edad >= 18:
            print("Esta persona es mayor de edad")
        else:
            print("Esta persona es menor de edad")
    def bonificación(self):
        return self.sueldo * 0.20

persona_1 = Persona("Juan", 20, 3000)
persona_2 = Persona("Elena", 30, 5000)

print("Los datos de la primera persona son los siguientes")
persona_1.mostrar_datos()
persona_1.mayor_edad()
print("La bonificación de la primera persona es:", persona_1.bonificación())
print(" ")
print("Los datos de la segunda persona son los siguientes")
persona_2.mostrar_datos()
persona_2.mayor_edad()
print("La bonificación de la segunda persona es:", persona_2.bonificación())
