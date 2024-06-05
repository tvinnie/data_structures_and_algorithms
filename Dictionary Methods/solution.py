dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for key in dictionary.keys():
    print(key, "->", dictionary[key])

# Output 
""" horse -> cheval
dog -> chien
cat -> chat """


dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for english, french in dictionary.items():
    print(english, "->", french)

# Output 
""" horse -> cheval
dog -> chien
cat -> chat """

# -------------------------------------------------------------------------------------------

# Modifying and adding values
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary['cat'] = 'minou'
print(dictionary)

# The output is: {'cat': 'minou', 'dog': 'chien', 'horse': 'cheval'}

# ------------------------------------------------------------------------------------------- 

# Sorting using keys()
for key in sorted(dictionary.keys()):
    print(key)

# Sorting using values()
# Note: It does return values
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
for french in dictionary.values():
    print(french)

# -------------------------------------------------------------------------------------------

# Adding a new Key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary['swan'] = 'cygne'
print(dictionary)
 
# The example outputs: {'cat': 'chat', 'dog': 'chien', 'horse': 'cheval', 'swan': 'cygne'} 


# adding using update() method 
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.update({"duck": "canard"})
print(dictionary)


# -------------------------------------------------------------------------------------------
# Removing a Key
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
del dictionary['dog']
print(dictionary)

# The example outputs: {'cat': 'chat', 'horse': 'cheval'} 


# To remove the last item in a dictionary, you can use the popitem() method:
dictionary = {"cat": "chat", "dog": "chien", "horse": "cheval"}
dictionary.popitem()
print(dictionary) # outputs: {'cat': 'chat', 'dog': 'chien'}
 


# -------------------------------------------------------------------------------------------
# creating a tuple using the tuple method
# You can also create a tuple using a Python built-in function called tuple(). This is particularly useful when you want to convert a certain iterable (e.g., a list, range, string, etc.) to a tuple:

my_tuple = tuple((1, 2, "string"))
print(my_tuple)

my_list = [2, 4, 6]
print(my_list)    # outputs: [2, 4, 6]
print(type(my_list))    # outputs: <class 'list'>
tup = tuple(my_list)
print(tup)    # outputs: (2, 4, 6)
print(type(tup))    # outputs: <class 'tuple'>

# -------------------------------------------------------------------------------------------

# when you want to convert an iterable to a list, you can use a Python built-in function called list():
tup = 1, 2, 3,
my_list = list(tup)
print(type(my_list)) # outputs: <class 'list'>



# -------------------------------------------------------------------------------------------




# -------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------



# -------------------------------------------------------------------------------------------