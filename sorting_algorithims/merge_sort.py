def merge_sort(my_list):
    if len(my_list) > 1: 
        mid = len(my_list)//2
        left_half = my_list[:mid]
        right_half = my_list[mid:]
        
        merge_sort(left_half)
        merge_sort(right_half)
 
        i = j = k = 0
 
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
        		# Correct mistake when assigning left half
                my_list[k] = left_half[i]                
                i += 1
            else:
                # Correct mistake when assigning right half
                my_list[k] = right_half[j]
                j += 1
            k += 1
            
        while i < len(left_half):
            my_list[k] = left_half[i]
            # Correct mistake when updating pointer for left half
            i += 1
            k += 1
 
        while j < len(right_half):
            my_list[k] = right_half[j]
            # Correct mistake when updating pointer for right half
            j += 1
            k += 1

my_list = [35,22,90,4,50,20,30,40,1]
merge_sort(my_list)
print(my_list)

#SOLUTION ::: [1, 4, 20, 22, 30, 35, 40, 50, 90]