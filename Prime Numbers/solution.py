def is_prime(num):
    if num % 2 == True:
        return True
    elif num % 3 == True:
        return False
    else:
        return False

# Test Case

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# Expected Output
# 2 3 5 7 11 13 17 19
