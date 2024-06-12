# The find() method
# ONE PARAMETER VARIANT

# The find() method is similar to index(), which you already know – it looks for a substring and returns the index of the first occurrence of this substring, but:

# it's safer – it doesn't generate an error for an argument containing a non-existent substring (it returns -1 then)
# it works with strings only – don't try to apply it to any other sequence.
# Look at the code in the editor. This is how you can use it.

# Demonstrating the find() method:
print("Eta".find("ta"))
print("Eta".find("mma"))

# Output
"""
1
-1
"""

# TWO PARAMETER VARIANT
# If you want to perform the find, not from the string's beginning, but from any position, you can use a two-parameter variant of the find() method. Look at the example:
print('kappa'.find('a', 2))

"""
The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).

Among the two a letters, only the second will be found 
"""

# THREE PARAMETER VARIANT
# There is also a three-parameter mutation of the find() method
# the third argument points to the first index which won't be taken into consideration during the search (it's actually the upper limit of the search).

print('kappa'.find('a', 1, 4))
print('kappa'.find('a', 2, 4))

# Output 
# 1 -1

# The second argument specifies the index at which the search will be started (it doesn't have to fit inside the string).
# NOTE: (a cannot be found within the given search boundaries in the second print().

# ----------------------------------------------

# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------
# ----------------------------------------------