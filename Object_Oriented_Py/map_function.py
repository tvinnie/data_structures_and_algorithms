# The map(fun, list) function creates a copy of a list argument, and applies the fun function to all of its elements, returning a generator that provides the new list content element by element. 

short_list = ['mython', 'python', 'fell', 'on', 'the', 'floor']
new_list = list(map(lambda s: s.title(), short_list))
print(new_list)

# OUTPUT: ['Mython', 'Python', 'Fell', 'On', 'The', 'Floor']