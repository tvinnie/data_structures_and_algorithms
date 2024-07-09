# ZIP

letters = ['a', 'b', 'c']
nums = [1, 2, 3]

for letter, num in zip(letters, nums):
    print("{}: {}".format(letter, num))

# UNZIP

some_list = [('a', 1), ('b', 2), ('c', 3)]
letters, nums = zip(*some_list)


# ENUMERATE

letters = ['a', 'b', 'c', 'd', 'e']
for i, letter in enumerate(letters):
    print(i, letter)

# OUTPUT
"""
0 a
1 b
2 c
3 d
4 e

"""

"""
Quiz: Zip Coordinates
Use zip to write a for loop that creates a string specifying the label and coordinates of each point and appends it to the list points.

Each string should be formatted as label: x, y, z. For example, the string for the first coordinate should be F: 23, 677, 4.
"""
x_coord = [23, 53, 2, -12, 95, 103, 14, -5]
y_coord = [677, 233, 405, 433, 905, 376, 432, 445]
z_coord = [4, 16, -6, -42, 3, -6, 23, -1]
labels = ["F", "J", "A", "Q", "Y", "B", "W", "X"]
points = []
# write your for loop here
for vals in zip(labels,x_coord,y_coord,z_coord):
    points.append("{}: {} {} {}".format(*vals))

for point in points:
    print(point)

# OUTPUT:
"""
F: 23 677 4
J: 53 233 16
A: 2 405 -6
Q: -12 433 -42
Y: 95 905 3
B: 103 376 -6
W: 14 432 23
X: -5 445 -1
"""