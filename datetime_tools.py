#Different methods to obtain datetimes from our pc

import datetime

#UTC
my_time = datetime.datetime.now()
print(my_time)

my_day = datetime.date.today()
print(my_day)

print(f'year: {my_day.year}')
print(f'Month: {my_day.month}')
print(f'Day: {my_day.day}')


#date formats
""" 
%Y: year
%m: month
%d: day
%H: hour
%M: minute
%S: second
"""

#Examples
from datetime import datetime

my_datetime = datetime.now()
print(my_datetime)

#strftime= string format time
my_str = my_datetime.strftime('%d/%m/%Y')
print((f'Formato LATAM: {my_str}'))

my_str = my_datetime.strftime('%m/%d/%Y')
print((f'Formato USA: {my_str}'))

my_str = my_datetime.strftime('Estamos en el año %Y')
print((f'Formato Random: {my_str}'))