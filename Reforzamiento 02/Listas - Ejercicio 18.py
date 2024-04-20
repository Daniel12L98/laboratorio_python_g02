lista = []
for i in range(1, 30, 2):
    lista.append(i)
print("La lista es: {}".format(lista))
lista.append(1.5)
lista.append(1.5)
lista.append(1.5)
print("La nueva lista con flotantes repetidos es: {}".format(lista))
lista.insert(2, "cadena")
print("La nueva lista con 'cadena' en la posición 3 es: {}".format(lista))
del lista[7]
print("La nueva lista con el valor impar eliminado es: {}".format(lista))
