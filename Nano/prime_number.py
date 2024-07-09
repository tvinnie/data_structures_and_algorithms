## iterate through the check_prime list

for num in check_prime:

## check if the number is 2

    if num == 2:
        print("{} IS a prime number".format(num))
        continue

## search for factors, iterating through numbers ranging from 2 to the number itself

for i in range(2, num):

## number is not prime if modulo is 0

    if (num % i) == 0:
        print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
        break

## otherwise keep checking until we've searched all possible factors, and then declare it prime

    if i == num -1:    
        print("{} IS a prime number".format(num))


# TEST CASES:

# check_prime = [26, 39, 51, 53, 57, 79, 85]