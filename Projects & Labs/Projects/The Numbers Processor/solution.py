line = input('Enter a list of numbers - separate using space: ')
strings = line.split()
total = 0

try:
    for value in strings:
        total += float(value)
    print('The Total is: ', total)
except:
    print(value, " is not a number")