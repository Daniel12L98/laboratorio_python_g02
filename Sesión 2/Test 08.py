"""Crear 4 variables: nombre, edad, pais de residencia y distrito"""
"""
Requisitos:
-Nombre: string, edad: int, pais de residencia: string, distrito:string
-Concatenar estos datos e indicar una horación como la siguiente
José tiene X años, es del distrito de "distrito" y viene de "pais de residencia"
-Obtener el módulo de su edad al usarlo con el número 5
"""
nombre = "Daniel"
edad = 25
pais_de_residencia = "Perú"
distrito = "Surco"
print(nombre + " " + "tiene" + " " + str(edad) + " " + "años" + " " + "es del distrito de" + " " + distrito + " " + "y viene de" + " " + pais_de_residencia)
print(edad % 5)
