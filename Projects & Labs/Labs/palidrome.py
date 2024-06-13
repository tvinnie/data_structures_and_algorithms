

word = input('Enter word/sentence: ')

word = word.replace(' ', '')

if len(word) > 1 and word.upper() == word[::-1].upper():
    print('It is a palidrome!')
else:
    print('It is not a palidrome!')
    

# Sample input:
# Ten animals I slam in a net

# Sample output:
# It's a palindrome