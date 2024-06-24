def outer(par):
    loc = par

    def inner():
        return loc
    return inner


var = 1
fun = outer(var)
print(fun())
    
Output: 1

"""
Look carefully:

 * the inner() function returns the value of the variable accessible inside its scope, as inner() can use any of the entities at the disposal of outer()
 * the outer() function returns the inner() function itself; more precisely, it returns a copy of the inner() function, the one which was frozen at the moment of outer()'s invocation; the frozen function contains its full environment, including the state of all local variables, which also means that the value of loc is successfully retained, although outer() ceased to exist a long time ago

 NOTE: The function returned during the outer() invocation is a closure.
 NOTE: A closure has to be invoked in exactly the same way in which it has been declared.
"""