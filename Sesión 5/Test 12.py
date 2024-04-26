"""Programación orientada a objetos en Python"""

class Carro:
    """Atributos"""
    ruedas = 4

    """Constructor: Valores que van a tener por defecto mi clase que se le instancia en una variable"""

    def __init__(self, color, aceleracion):
        self.color = color
        self.aceleracion = aceleracion
        self.velocidad = 0

        """Mérodos: Son las funciones de la clase"""
    def acelerar(self):
        self.velocidad = self.velocidad + self.aceleracion

    def frena(self):
        velocidad = self.velocidad - self.aceleracion
        if velocidad < 0:
            velocidad = 0
        self.velocidad = velocidad

"""Instanciamos nuestra clase"""
carro_1 = Carro("Negro", 50)
print("El color del primer carro es: {}".format(carro_1.color))
print("La aceleración en el primer carro es: {}".format(carro_1.aceleracion))
print("La cantidad de ruedas del primer carro es: {}".format(carro_1.ruedas))

carro_2 = Carro("Azul", 90)
print("El color del segundo carro es: {}".format(carro_2.color))
print("La aceleración en el segundo carro es: {}".format(carro_2.aceleracion))
print("La cantidad de ruedas del segundo carro es: {}".format(carro_2.ruedas))
