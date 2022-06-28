#Use of different timezones and examples

from datetime import datetime
import pytz


bogota_timezone = pytz.timezone("America/Bogota")
bogota_date = datetime.now(bogota_timezone)
print("Bogotá: ", bogota_date.strftime("%d/%m/%Y, %H:%M:%S"))

mexico_city_timezone = pytz.timezone("America/Mexico_City")
mexico_city_date = datetime.now(mexico_city_timezone)
print("Ciudad de México: ", mexico_city_date.strftime("%d/%m/%Y, %H:%M:%S"))

caracas_timezone = pytz.timezone("America/Caracas")
caracas_date = datetime.now(caracas_timezone)
print("Caracas: ", caracas_date.strftime("%d/%m/%Y, %H:%M:%S"))
