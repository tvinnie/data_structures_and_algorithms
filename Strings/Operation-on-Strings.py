"""
min()

# Now that you understand that strings are sequences, we can show you some less obvious sequence capabilities. We'll present them using strings, but don't forget that lists can adopt the same tricks, too.

# Let's start with a function named min().

# The function finds the minimum element of the sequence passed as an argument. There is one condition – the sequence (string, list, it doesn't matter) cannot be empty, or else you'll get a ValueError exception.

"""
# Demonstrating min() - Example 1:
print(min("aAbByYzZ"))


# Demonstrating min() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + min(t) + ']')

t = [0, 1, 2]
print(min(t))

# Output 

"""
A
[ ]
0 

"""

# -------------------------------------------------------------------------------
"""
max()

# Similarly, a function named max() finds the maximum element of the sequence.

"""

# Demonstrating max() - Example 1:
print(max("aAbByYzZ"))


# Demonstrating max() - Examples 2 & 3:
t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

t = [0, 1, 2]
print(max(t))

# Output
"""
z
[y]
2

"""
# -------------------------------------------------------------------------------
"""
The index() method

# The index() method (it's a method, not a function) searches the sequence from the beginning, in order to find the first element of the value specified in its argument.

# Note: the element searched for must occur in the sequence – its absence will cause a ValueError exception.

# The method returns the index of the first occurrence of the argument (which means that the lowest possible result is 0, while the highest is the length of the argument decremented by 1).

"""
# Demonstrating the index() method:
print("aAbByYzZaA".index("b"))
print("aAbByYzZaA".index("Z"))
print("aAbByYzZaA".index("A"))

# Output
"""
2
7
1
"""
# -------------------------------------------------------------------------------
"""
The list() function

# The list() function takes its argument (a string) and creates a new list containing all the string's characters, one per list element.

# Note: it's not strictly a string function - list() is able to create a new list from many other entities (e.g., from tuples and dictionaries).

# Take a look at the code example in the editor.
"""

# Demonstrating the list() function:
print(list("abcabc"))

# Output
#  ['a', 'b', 'c', 'a', 'b', 'c']

# -------------------------------------------------------------------------------
"""
The count() method

# The count() method counts all occurrences of the element inside the sequence. The absence of such elements doesn't cause any problems.
"""
# Demonstrating the count() method:
print("abcabc".count("b"))
print('abcabc'.count("d"))

# Output
"""
2
0
"""
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------
# -------------------------------------------------------------------------------