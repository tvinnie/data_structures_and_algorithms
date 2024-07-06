import calendar  

c = calendar.Calendar(calendar.SUNDAY)

for weekday in c.iterweekdays():
    print(weekday, end=" ")
    
# OUTPUT: 6 0 1 2 3 4 5 