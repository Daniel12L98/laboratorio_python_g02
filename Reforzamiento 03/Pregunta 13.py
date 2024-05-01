class Persona():
    def __init__(self, nombre, edad):
        self.nombre = "Juan"
        self.edad = 24


class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def impuesto(self):
        impuesto = 0
        if self.sueldo > 4000:
            print("Debe pagar impuesto")
            impuesto = self.sueldo * 0.10
        else:
            print("No debe pagar impuesto")
        return impuesto


empleado = Empleado("Juan", 25, 5000)
impuesto = empleado.impuesto()

print("El sueldo del {} es: {} soles".format(empleado.nombre, empleado.sueldo))
print("{} debe pagar de impuesto: {} soles".format(empleado.nombre, impuesto))