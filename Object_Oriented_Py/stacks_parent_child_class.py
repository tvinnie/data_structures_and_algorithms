# Initiating a child class

class AddingStack(Stack): # Child class init
    def __init__(self):
        Stack.__init__(self) # Explicitly invoke a superclass's constructor
        self.__sum = 0

        """
        you have to point to the object (the class's instance) which has to be initialized by the constructor – this is why you have to specify the argument and use the self variable here; note: invoking any method (including constructors) from outside the class never requires you to put the self argument at the argument's list – invoking a method from within the class demands explicit usage of the self argument, and it has to be put first on the list.

        """

# Full Code - Parent and Child Class

class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val


class AddingStack(Stack):
    def __init__(self):
        Stack.__init__(self)
        self.__sum = 0

    def get_sum(self):
        return self.__sum

    def push(self, val):
        self.__sum += val
        Stack.push(self, val)

    def pop(self):
        val = Stack.pop(self)
        self.__sum -= val
        return val


stack_object = AddingStack()

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())

# Output
"""
10
4
3
2
1
0

"""    