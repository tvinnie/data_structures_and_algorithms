# NOTE: replace() method

# The two-parameter replace() method returns a copy of the original string in which all occurrences of the first argument have been replaced by the second argument.

# Demonstrating the replace() method:
print("www.netacad.com".replace("netacad.com", "pythoninstitute.org"))
print("This is it!".replace("is", "are"))
print("Apple juice".replace("juice", ""))

# OUTPUT

"""
www.pythoninstitute.org
Thare are it!
Apple

"""

# The three-parameter replace() variant uses the third argument (a number) to limit the number of replacements.

print("This is it!".replace("is", "are", 1))
print("This is it!".replace("is", "are", 2))

# Output

"""
Thare is it!
Thare are it!
"""