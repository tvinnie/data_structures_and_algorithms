# NOTE: Anagrams

"""
An anagram is a new word formed by rearranging the letters of a word, using all the original letters exactly once. For example, the phrases "rail safety" and "fairy tales" are anagrams, while "I am" and "You are" are not.

Your task is to write a program which:

asks the user for two separate texts;
checks whether, the entered texts are anagrams and prints the result.

"""
word1 = input('Enter first word: ')
word2 = input('Enter second word: ')

word1 = ''.join(sorted(list(word1.upper().replace(' ',''))))
word2 = ''.join(sorted(list(word1.upper().replace(' ',''))))

if len(word1) > 1 and word1 == word2:
    print('It is an anagram!')
else:
    print('It is not an anagram!')


# TEST CASES

# word1 : listen
# word2: silent