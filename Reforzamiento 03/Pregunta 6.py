class Operaciones:
    def __init__(self):
        self.resultado = None
        pass

    def valor(self):
        while True:
            try:
                self.numero = int(input("Ingrese su valor: "))
                return self.numero
            except ValueError:
                print("El valor ingresado no es válido")

    def elevado_cubo(self):
        if self.resultado is None:
            self.valor()
        self.resultado = self.numero ** 3
        return self.resultado

    def elevado_cuadrado(self):
        if self.resultado is None:
            self.valor()
        self.resultado = self.numero ** 2
        return self.resultado

operaciones_1 = Operaciones()

resultado_1 = operaciones_1.elevado_cubo()
resultado_2 = operaciones_1.elevado_cuadrado()
print("El número al cubo es:", resultado_1)
print("El número al cuadrado es:", resultado_2)