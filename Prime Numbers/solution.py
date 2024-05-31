def is_prime(num):
    for i in range(2, int(1 + num ** 0.5)):
        if num % i == 0:
            return False
    return True

# Test Case

for i in range(1, 20):
    if is_prime(i + 1):
        print(i + 1, end=" ")
print()

# Expected Output
# 2 3 5 7 11 13 17 19
