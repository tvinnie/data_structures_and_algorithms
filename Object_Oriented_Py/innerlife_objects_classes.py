# __dict__

class Classy:
    varia = 1
    def __init__(self):
        self.var = 2

    def method(self):
        pass

    def __hidden(self):
        pass

obj = Classy()
print(obj.__dict__)

# Output : {'var': 2}

# ------------------------------------------------------------------------------------------------------------------------------------------


# __name__ :: The property contains the name of the class

class Classy:
    pass
print(Classy.__name__)
obj = Classy()
print(type(obj).__name__)

# Output: Classy Classy

# ------------------------------------------------------------------------------------------------------------------------------------------

# __module__ :: it stores the name of the module which contains the definition of the class.

class Classy:
    pass
print(Classy.__module__)
obj = Classy()
print(obj.__module__)
    
# Output: __main__ __main__
# ------------------------------------------------------------------------------------------------------------------------------------------
# __bases__ :: is a tuple. The tuple contains classes (not class names) which are direct superclasses for the class.

class SuperOne:
    pass

class SuperTwo:
    pass

class Sub(SuperOne, SuperTwo):
    pass

def printBases(cls):
    print('( ', end='')

    for x in cls.__bases__:
        print(x.__name__, end=' ')
    print(')')

printBases(SuperOne)
printBases(SuperTwo)
printBases(Sub)
