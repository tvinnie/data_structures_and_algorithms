def print_function(args, fun):
    for x in args:
        print('f(', x,')=', fun(x), sep='')


def poly(x):
    return 2 * x**2 - 4 * x + 2 #lambda function in a function


print_function([x for x in range(-2, 3)], poly) 

# OR

print_function([x for x in range(-2, 3)], lambda x: 2 * x**2 - 4 * x + 2) #lambda inside the print function
    
"""
f(-2)=18
f(-1)=8
f(0)=2
f(1)=0
f(2)=2

"""


# lambda with map() function

list_1 = [x for x in range(5)]
list_2 = list(map(lambda x: 2 ** x, list_1))
print(list_2)

for x in map(lambda x: x * x, list_2):
    print(x, end=' ')
print()

# Output: 1 4 16 64 256 