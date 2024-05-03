"""Uso de libreria de fecha y tiempo"""

from datetime import datetime, date

"""Obtener la decha actual"""

fecha = date.today()
print("La fecha a manejar es la siguiente: {}".format(fecha))

tiempo = datetime.now()
print(tiempo)

anio = tiempo.year
mes = tiempo.month
dia = tiempo.day

print("El año actual:", anio)
print(mes)
print(dia)

"""Uso del datetime para extraer la hora, el minuto y el segundo"""

hora = tiempo.hour
minuto = tiempo.minute
segundo = tiempo.second

print("La hora exacta: {} {} {}".format(hora, minuto, segundo))
