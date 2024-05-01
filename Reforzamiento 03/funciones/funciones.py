def nombre():
    nombre = input("Ingresar nombre:")
    apellido = input("Ingresar apellido:")
    return nombre, apellido

def tipo_seguro():
    seguro = input("Ingrese el tipo de seguro que tiene:")
    return seguro

def mayor_edad():
    edad = int(input("Ingrese su edad:"))
    return edad >= 18