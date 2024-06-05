# function to print fibonacci numbers 


""" 
They are a sequence of integer numbers built using a very simple rule:
    the first element of the sequence is equal to one (Fib1 = 1)
    the second is also equal to one (Fib2 = 1)
    every subsequent number is the the_sum of the two preceding numbers:(Fibi = Fibi-1 + Fibi-2)
    
Here are some of the first Fibonacci numbers:
    fib_1 = 1 fib_2 = 1 fib_3 = 1 + 1 = 2 fib_4 = 1 + 2 = 3 fib_5 = 2 + 3 = 5 fib_6 = 3 + 5 = 8 fib_7 = 5 + 8 = 13 
"""

def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1

    elem_1 = elem_2 = 1
    the_sum = 0
    for i in range(3, n + 1):
        the_sum = elem_1 + elem_2
        elem_1, elem_2 = elem_2, the_sum
    return the_sum


for n in range(1, 16):  # testing
    print(n, "->", fib(n))


# Fibonacci using Recursion Part 1
def fib(n):
    if n < 1:
        return None
    if n < 3:
        return 1
    return fib(n - 1) + fib(n - 2)

# test function using recursion Part 1
for n in range(1, 16):  # testing
    print(n, "->", fib(n))

# NOTE: You can use recursive functions in Python to write clean, elegant code, and divide it into smaller, organized chunks. On the other hand, you need to be very careful as it might be easy to make a mistake and create a function which never terminates. You also need to remember that recursive calls consume a lot of memory, and therefore may sometimes be inefficient


