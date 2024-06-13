txt = input('Enter text to enrypt: ');
cyp = ''
shift = 0

while shift == 0:
    try:
        shift = int(input('Enter enrypt shift value(btwn 1 & 25): '));
        if shift not in range(1,26):
            raise ValueError
    except ValueError:
        shift = 0
    if shift == 0:
        print('Incorrect Shift Value!')
        

for char in txt:
    if char.isalpha():
        code = ord(char) + shift
        if char.isupper():
            first = ord('A')
        else:
            first = ord('a')
        code -= first
        code %= 26 
        cyp += chr(first + code)
    else:
        cyp += char
print(cyp)


# TEST DATA

# Sample Input:
"""
abcxyzABCxyz 123
2

"""
# Expected Output
"""
cdezabCDEzab 123

"""
# ------------------------------------------

# Sample Input:
"""
The die is cast
25

"""
# Expected Output
"""
Sgd chd hr bzrs

"""