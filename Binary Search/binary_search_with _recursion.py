"""
#INSTRUCTIONS:

Define the base case.
Check whether the search value equals the value in the middle.
Call the binary_search_recursive() function recursively on the left half of the list.
Call the binary_search_recursive() function recursively on the right half of the list.

"""
## SOLUTION

def binary_search_recursive(ordered_list, search_value):
  # Define the base case
  if len(ordered_list) == 0:
    return False
  else:
    middle = len(ordered_list)//2
    # Check whether the search value equals the value in the middle
    if search_value == ordered_list[middle]:
        return True
    elif search_value < ordered_list[middle]:
        # Call recursively with the left half of the list
        return binary_search_recursive(ordered_list[:middle], search_value)
    else:
        # Call recursively with the right half of the list
        return binary_search_recursive(ordered_list[:middle], search_value)
  
print(binary_search_recursive([1,5,8,9,15,20,70,72], 5))