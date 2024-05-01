def contador(oracion):
    palabras = oracion.split()
    return len(palabras)
while True:
    oracion = input("Ingrese una oración con 3 palabras máximo: ")
    if len(oracion.split()) >= 3:
        break
    else:
        print("La oración debe tener 3 palabras como mínimo")
cantidad_palabras = contador(oracion)
print("La oración tiene", cantidad_palabras, "palabras")