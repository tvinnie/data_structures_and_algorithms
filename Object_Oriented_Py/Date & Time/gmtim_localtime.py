"""
time.struct_time:
    tm_year   # Specifies the year.
    tm_mon    # Specifies the month (value from 1 to 12)
    tm_mday   # Specifies the day of the month (value from 1 to 31)
    tm_hour   # Specifies the hour (value from 0 to 23)
    tm_min    # Specifies the minute (value from 0 to 59)
    tm_sec    # Specifies the second (value from 0 to 61 )
    tm_wday    # Specifies the weekday (value from 0 to 6)
    tm_yday   # Specifies the year day (value from 1 to 366)
    tm_isdst  # Specifies whether daylight saving time applies (1 – yes, 0 – no, -1 – it isn't known)
    tm_zone   # Specifies the timezone name (value in an abbreviated form)
    tm_gmtoff # Specifies the offset east of UTC (value in seconds)


"""
# The struct_time class also allows access to values using indexes. Index 0 returns the value in tm_year, while 8 returns the value in tm_isdst.
# The exceptions are tm_zone and tm_gmoff, which cannot be accessed using indexes

import time

timestamp = 1572879180
print(time.gmtime(timestamp))
print(time.localtime(timestamp))

# OUTPUT:
"""
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=0)
"""