"""Listas en Python"""

"""Requisitos
- Crear dos listas vacías inicialmente
_ Agregar luego los datos de nombre, edad y profesión para ambos (usando append)
- Sumar ambas listas y mostrar el resultado en consola
- Mostrar de manera inversa la suma de ambas listas
- Actualizar la nueva lista eliminando las edades de ambas personas con remove
"""

lista_1 = []
lista_2 = []

lista_1.append("Daniel")
lista_1.append(25)
lista_1.append("Ingeniero")
lista_2.append("Juan")
lista_2.append(23)
lista_2.append("Doctor")

suma_listas = lista_1 + lista_2
print(suma_listas)

suma_listas.reverse()
print(suma_listas)

suma_listas.remove(23)
suma_listas.remove(25)
print(suma_listas)