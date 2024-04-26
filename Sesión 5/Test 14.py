"""Programación orientada a objetos en Python
Clase y métodos"""

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

carro_1 = Carro("Azul", 100)

print("La valocidad inicial de mi carro 1 es: {}".format(carro_1.velocidad))

carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
carro_1.acelerar()
print("La nueva velocidad que tiene el carro 1 es: {}".format(carro_1.velocidad))

carro_1.frena()
carro_1.frena()
carro_1.frena()
print("La velocidad actual de mi carro 1 luego de frenar una vez es: {}".format(carro_1.velocidad))

