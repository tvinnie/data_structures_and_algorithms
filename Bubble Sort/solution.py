mlist = [8,10,6,2,4] # the list of number to sort
swapped = True

while swapped:
    swapped = False # no swaps
    for i in range(len(mlist) - 1): 
        if mlist[i] > mlist[i + 1]: # doing the comparisons
            swapped = True # a swap has occurred 
            mlist[i],mlist[i+1] = mlist[i+1],mlist[i]
            
print(mlist)