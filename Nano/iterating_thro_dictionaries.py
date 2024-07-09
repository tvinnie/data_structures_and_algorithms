#  Iterating Through Dictionaries with For Loops

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }
# iterating through keys alone
for key in cast:
    print(key)

    
# Iterating through keys and values
for key, value in cast.items():
    print('Actor:{}  Role: {}'.format(key,value))

# OUTPUT: 
"""
Actor: Jerry Seinfeld    Role: Jerry Seinfeld
Actor: Julia Louis-Dreyfus    Role: Elaine Benes
Actor: Jason Alexander    Role: George Costanza
Actor: Michael Richards    Role: Cosmo Kramer
"""

# NOTE: items is an awesome method that returns tuples of key, value pairs, which you can use to iterate over dictionaries in for loops.