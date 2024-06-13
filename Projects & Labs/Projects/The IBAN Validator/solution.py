iban = input('Enter an iban number: ')
iban = iban.replace(' ', '')

if not iban.isalnum():
    print('You have entered invalid characters, try again!')
elif len(iban) < 15:
    print('You have entered less characters, try again!')
elif len(iban) > 31:
    print('You have entered excess characters, try, again!')
else:
    iban = (iban[4:] + iban[0:4]).upper()
    iban2 = ''
    for char in iban:
        if char.isdigit():
            iban2 += char
        else:
            iban2 += str(10 + ord(char) - ord('A')) 
    iban = int(iban2)
    if iban % 97 == 1:
        print('The iban number is valid!')
    else:
        print('The iban number is invalid')



# TEST CASES:
"""Albania: AL47 2121 1009 0000 0002 3569 87411 
Luxembourg: LU 28 001 94006447500003
Cyprus: CY 17 002 00128 00000012005276002
Norway: NO 93 8601 1117947
Kuwait: KW81CBKU0000000000001234560101"""