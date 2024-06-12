# NOTE: join() method

# The join() method is rather complicated, so let us guide you through it step by step:

"""
 * as its name suggests, the method performs a join – it expects one argument as a list; it must be assured that all the list's elements are strings – the method will raise a TypeError exception otherwise;
 * all the list's elements will be joined into one string but...
 * ...the string from which the method has been invoked is used as a separator, put among the strings;
 * the newly created string is returned as a result.
 
 """
# Demonstrating the join() method:
print(",".join(["omicron", "pi", "rho"]))

# OUTPUT
# omicron,pi,rho