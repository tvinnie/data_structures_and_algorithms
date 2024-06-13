# NOTE: sorting methods

# sorted()
# sort()

# -----------------------------------------------------------------------

# SORTED()

"""The function takes one argument (a list) and returns a new list, filled with the sorted argument's elements. (Note: this description is a bit simplified compared to the actual implementation – we'll discuss it later.)

The original list remains untouched."""
# Demonstrating the sorted() function:
first_greek = ['omega', 'alpha', 'pi', 'gamma']
first_greek_2 = sorted(first_greek)

print(first_greek)
print(first_greek_2)

print()

# Output: 
"""
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']

"""

# -------------------------------------------------------------------------------

# SORT()
"""
The second method affects the list itself – no new list is created.
Ordering is performed in situ by the method named sort().

"""

# Demonstrating the sort() method:
second_greek = ['omega', 'alpha', 'pi', 'gamma']
print(second_greek)

second_greek.sort()
print(second_greek)

# Output: 
"""
['omega', 'alpha', 'pi', 'gamma']
['alpha', 'gamma', 'omega', 'pi']

"""