"""
A text file contains some text (nothing unusual) but we need to know how often (or how rare) each letter appears in the text. Such an analysis may be useful in cryptography, so we want to be able to do that in reference to the Latin alphabet.

Your task is to write a program which:

asks the user for the input file's name;
reads the file (if possible) and counts all the Latin letters (lower- and upper-case letters are treated as equal)
prints a simple histogram in alphabetical order (only non-zero counts should be presented)
Create a test file for the code, and check if your histogram contains valid results.

"""
from os import strerror

# Initialize 26 counters for each Latin letter.
# Note: we've used a comprehension to do that.
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
file_name = input("Enter the name of the file to analyze: ")
try:
    file = open(file_name, "rt")
    for line in file:
        for char in line:
            # If it is a letter...
            if char.isalpha():
                # ... we'll treat it as lower-case and update the appropriate counter.
                counters[char.lower()] += 1
    file.close()
    # Let's output the counters.
    for char in counters.keys():
        c = counters[char]
        if c > 0:
            print(char, '->', c)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))


# TEST CASES
# Sample file (samplefile.txt) with aBc . 

# NOTE: OUTPUT

"""
a -> 1
b -> 1
c -> 1

"""
    