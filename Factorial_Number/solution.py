# Finding the Product of fuctorial numbers

def factorial_function(n):
    if n < 0:
        return None
    elif n < 2:
        return 1
        
    
    product  = 1
    for i in range(1, n+1):
        product *= i
    return product
    
# test case
for n in range(1,6):
    print(n,factorial_function(n))