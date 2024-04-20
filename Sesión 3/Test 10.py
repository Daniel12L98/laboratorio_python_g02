"""Uso del fluo condicional: if"""

estado = 1

"""Aplicando la forma ternaria"""

"""
*OTRA FORMA DE DECIR EL PROGRAMA DE ABAJO*
if estado == 1:
    print("1. Su estado final ha terminado")
else:
    print("2. Su estado es no terminado")
"""

final = "1. Su estado final es terminado" if estado == 1 else "2. Su estado es no terminado"
print(final)
