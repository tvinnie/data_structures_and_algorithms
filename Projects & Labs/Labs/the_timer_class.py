
"""
Read them carefully as the class you're about write will be used to launch rockets carrying international missions to Mars. It's a great responsibility. We're counting on you!

Your class will be called Timer. Its constructor accepts three arguments representing hours (a value from the range [0..23] – we will be using military time), minutes (from the range [0..59]) and seconds (from the range [0..59]).

Zero is the default value for all of the above parameters. There is no need to perform any validation checks.

The class itself should provide the following facilities:

objects of the class should be "printable", i.e. they should be able to implicitly convert themselves into strings of the following form: "hh:mm:ss", with leading zeros added when any of the values is less than 10;
the class should be equipped with parameterless methods called next_second() and previous_second(), incrementing the time stored inside the objects by +1/-1 second respectively.
Use the following hints:

all object properties should be private;
consider writing a separate function (not method!) to format the time string.

"""

# Expected Output"

"""
23:59:59
00:00:00
23:59:59

"""

def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s
    return s
    
    
class Timer:
    def __init__( self, hours=0, minutes=0, seconds=0 ):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return  two_digits(self.__hours) + ':' + two_digits(self.__minutes) + ':' + two_digits(self.__seconds)
            

    def next_second(self):
        self.__seconds += 1
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self):
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23

timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)
    