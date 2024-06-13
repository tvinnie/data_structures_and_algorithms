# Ceasers Decrypting Text

text = input('Enter word to decrypt: ')
cyp = ''
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    code = ord(char) - 1
    if code < ord('A'):
        code = ord('Z')
    cyp += chr(code)
print(cyp)