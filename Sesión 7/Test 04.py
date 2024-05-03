"""Uso de librerias de fecha y tiempo"""

"""
    Conversión de fechas
"""

from datetime import datetime

"""timestamp"""

time_now = datetime.strptime("2024/12/15 20:30:00", "%Y/%m/%d %H:%M:%S").timestamp()
print("La conversión de nuestro valor time_now es: {}".format(time_now))
