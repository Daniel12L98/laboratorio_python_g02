"""POO en Python"""
"""Polimorfismo"""

class Perro():
    def sonido(self):
        print("Guauu")

class Gato():
    def sonido(self):
        print("Miauu")

class Vaca():
    def sonido(self):
        print("Muuuu")


gato = Gato()
perro = Perro()
vaca = Vaca()

lista_animales = [perro, gato, vaca]

def canto(animales):
    for animal in animales: # Al final la lista que va a recorrer
        animal.sonido()

canto (lista_animales)  #Llamar la función que vamos a usar y luego que es lo que va a usar