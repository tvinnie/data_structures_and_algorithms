"""
You probably won't be surprised to learn that the strftime function is available in the time module. It differs slightly from the strftime methods in the classes provided by the datetime module because, in addition to the format argument, it can also take (optionally) a tuple or struct_time object.

If you don't pass a tuple or struct_time object, the formatting will be done using the current local time. Take a look at the example in the editor.

"""
import time
timestamp = 1572879180
st = time.gmtime(timestamp)

print(time.strftime("%Y/%m/%d %H:%M:%S", st))
print(time.strftime("%Y/%m/%d %H:%M:%S"))

"""
2019/11/04 14:53:00
2024/06/28 10:15:14
"""