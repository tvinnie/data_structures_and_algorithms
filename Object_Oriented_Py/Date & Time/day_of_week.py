"""
One of the more helpful methods that makes working with dates easier is the method called weekday. It returns the day of the week as an integer, where 0 is Monday and 6 is Sunday. Run the code in the editor.

"""
from datetime import date

the_day = date(1994,12,3)
print(the_day.weekday())


# NOTE: The date class has a similar method called isoweekday, which also returns the day of the week as an integer, but 1 is Monday, and 7 is Sunday.

from datetime import date

d = date(2019, 11, 4)
print(d.isoweekday())

#The integer returned by the isodayweek method follows the ISO 85601 specification

