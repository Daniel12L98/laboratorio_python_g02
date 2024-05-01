import math
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def areas(self):
        try:
            area = math.pi * (self.radio ** 2)
        except TypeError:
            print("No se puede hallar el área")
        else:
            print("El área del circulo es:", area)


    def perimetros(self):
        try:
            perimetro = 2 * math.pi * self.radio

        except AttributeError:
            print("No se puede hallar el perímetro")
        else:
            print("El perímetro del circulo es: ", perimetro)


    def radios(self):
        print("Radio: {}".format(self.radio))

print("Los datos del primer radio son")
area_circulo_1 = Circulo(4)
area_circulo_1.radios()
area_circulo_1.areas()
area_circulo_1.perimetros()
print(" ")
print("Los datos del segundo radio son")
area_circulo_2 = Circulo(3)
area_circulo_2.radios()
area_circulo_2.areas()
area_circulo_2.perimetros()