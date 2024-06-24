# Sample 1
list_1 = []

for ex in range(6):
    list_1.append(10 ** ex)

# Sample 2

list_2 = [10 ** ex for ex in range(6)]


# Output
print(list_1) # [1, 10, 100, 1000, 10000, 100000]
print(list_2) # [1, 10, 100, 1000, 10000, 100000]


# EXAMPLE 2: LISTS

the_list = [1 if x % 2 == 0 else 0 for x in range(10)]

print(the_list)

# Output: [1, 0, 1, 0, 1, 0, 1, 0, 1, 0]