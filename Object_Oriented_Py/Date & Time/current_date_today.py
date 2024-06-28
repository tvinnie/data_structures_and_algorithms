from datetime import date

current_day = date.today()

print("Today:", today)
print("Year:", today.year)
print("Month:", today.month)
print("Day:", today.day)

# OUTPUT:
"""
Today: 2024-06-28
Year: 2024
Month: 6
Day: 28

"""

from datetime import datetime

print("today:", datetime.today())
print("now:", datetime.now())
print("utcnow:", datetime.utcnow())

"""
today: 2024-06-28 10:01:41.839890
now: 2024-06-28 10:01:41.840245
utcnow: 2024-06-28 10:01:41.840486

"""