"""
The strftime method takes only one argument in the form of a string specifying a format that can consist of directives.

A directive is a string consisting of the character % (percent) and a lowercase or uppercase letter. For example, the directive %Y means the year with the century as a decimal number. Let's see it in an example. Run the code in the editor.

"""

from datetime import date

d = date(2020, 1, 4)
print(d.strftime('%Y/%m/%d'))
    
# OUTPUT
# 2020/01/04

# ------------------------------------------------------------------------------------------------

from datetime import time
from datetime import datetime

t = time(14, 53)
print(t.strftime("%H:%M:%S"))

dt = datetime(2020, 11, 4, 14, 53)
print(dt.strftime("%y/%B/%d %H:%M:%S"))

# OUTPUT:
"""
14:53:00
20/November/04 14:53:00
"""