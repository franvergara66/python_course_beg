def boolean_find_candidates(array, arr_size, sum):       
    quick_sort(array, 0, arr_size-1) 
    left = 0
    right = arr_size-1      
    # traverse the array for the two elements 
    while left<right: 
        if (array[left] + array[right] == sum): 
            return True
        elif (array[left] + array[right] < sum):
            array[left] + array[right]
            left += 1
        else: 
            array[left] + array[right]
            right -= 1
    return False

# Utility function for partitioning the array(used in quick sort) 
def partition(sort_list, low, high):
    i = (low -1)
    pivot = sort_list[high]
    for j in range(low, high):
        if sort_list[j] <= pivot:
            i += 1
            sort_list[i], sort_list[j] = sort_list[j], sort_list[i]
    sort_list[i+1],sort_list[high] = sort_list[high], sort_list[i+1]
    return (i+1)
            
def quick_sort(sort_list, low, high):
    if low < high:
        pi = partition(sort_list, low, high)
        quick_sort(sort_list, low, pi-1)
        quick_sort(sort_list, pi+1, high)

  

# Driver program to test the functions 
A = [2,5,3,1,-9] 
n = 5

print(True if boolean_find_candidates(A, len(A), n) else False)