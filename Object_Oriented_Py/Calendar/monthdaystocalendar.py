"""
The Calendar class has several other useful methods that you can learn more about in the documentation (https://docs.python.org/3/library/calendar.html).

One of them is the monthdays2calendar method, which takes the year and month, and then returns a list of weeks in a specific month. Each week is a tuple consisting of day numbers and weekday numbers. Look at the code in the editor.

"""
import calendar  

c = calendar.Calendar()

for data in c.monthdays2calendar(2020, 12):
    print(data)

