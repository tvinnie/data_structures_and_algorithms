#Ceasers Cyper Encoding

text = input('Enter word to enrypt: ')
cyp = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) + 1
    if code > ord('Z'):
        code = ord('A')
    cyp += chr(code)
print(cyp)