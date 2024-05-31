mlist = []
swapped = True
num = int(input("How many elements do you want to sort: "))

for i in range(num):
    val = float(input("Enter a list element: "))
    mlist.append(val)

while swapped:
    swapped = False
    for i in range(len(mlist) - 1):
        if mlist[i] > mlist[i + 1]:
            swapped = True
            mlist[i], mlist[i + 1] = mlist[i + 1], mlist[i]

print("\nSorted:")
print(mlist)

