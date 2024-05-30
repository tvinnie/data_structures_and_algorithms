# Prompt user input
c0 = int(input('Enter a value: '))
#  initialize count to 0
cnt = 0

# start loop to check whether number is not 1
while c0 != 1:
    # check divisibility by 2
    if c0 % 2 == 0:
        c0 = c0 / 2
        cnt = cnt + 1 # increase count by 1
    elif c0 % 2 == 1:
        c0 = 3 * c0 + 1
        cnt= cnt + 1
    print(c0) # print the values obtained in c0
print('steps = ', str(cnt)) # print the number of iterations of the function





# Test Data:

# Sample input: 15                                Expected output: 46,46,70,35,106,53,160,80,40,20,10,5,16,8,4,2,1    steps = 17

# Sample input: 16                                Expected output: 8,4,2,1    steps = 4

# Sample input: 1023                              Expected output: 3070,1535,4606,2303,6910,3455,10366,5183,.....,4,2  steps = 62