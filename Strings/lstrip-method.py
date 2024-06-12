# NOTE: lstrip() method

# The parameterless version of the lstrip() method returns a newly created string formed from the original one by removing all leading whitespaces.

# Demonstrating the lstrip() method:
print("[" + " tau ".lstrip() + "]")

# Output: [tau ]


# The one-parameter version of the lstrip() method does the same as its parameterless version, but removes all characters enlisted in its argument (a string), not just whitespaces:
print("www.cisco.com".lstrip("w."))

# Output:  cisco.com
