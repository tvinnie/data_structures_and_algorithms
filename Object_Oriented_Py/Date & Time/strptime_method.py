from datetime import datetime
print(datetime.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# OUTPUT
# 2019-11-04 14:53:00

"""In the example, we've specified two required arguments. The first is a date and time as a string: "2019/11/04 14:53:00", while the second is a format that facilitates parsing to a datetime object. Be careful, because if the format you specify doesn't match the date and time in the string, it'll raise a ValueError.

Note: In the time module, you can find a function called strptime, which parses a string representing a time to a struct_time object. Its use is analogous to the strptime method in the datetime class:"""


import time
print(time.strptime("2019/11/04 14:53:00", "%Y/%m/%d %H:%M:%S"))

# Output
# time.struct_time(tm_year=2019, tm_mon=11, tm_mday=4, tm_hour=14, tm_min=53, tm_sec=0, tm_wday=0, tm_yday=308, tm_isdst=-1)