# check the existence of an attiribute using the hasattr() 

class ExampleClass:
    attr = 1


print(hasattr(ExampleClass, 'attr'))
print(hasattr(ExampleClass, 'prop'))

"""
Output

True
False
"""