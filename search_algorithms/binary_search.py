# BINARY SEARCH WITH RECURSIVE APPROACH
def binary_search(search_array, start_index, last_index, search_val):
    # check base case
    if last_index >= start_index:

        mid_index = ( last_index + start_index) // 2
        
        # If element is present at the middle itself
        if search_array[mid_index] == search_val:
            return mid_index
        
        # If element is smaller than mid, then it can only be present in left subarray
        elif search_array[mid_index] > search_val:
            return binary_search(search_array, start_index, mid_index-1, search_val)
        
        # Else the element can only be present in right subarray
        else:
            return binary_search(search_array, mid_index+1, last_index, search_val)
    
    else:
        # Element is not present in the array
        return -1
    

# BINARY SEARCH WITH ITERATIVE APPROACH
def binary_search_iterative(search_value, search_array):
    start_index, last_index = 0, len(search_array)-1

    while(last_index >= start_index):
        middle_index = (start_index + last_index) // 2
        if search_array[middle_index] == search_value:
            return middle_index
        
        elif search_array[middle_index] > search_value:
            last_index = middle_index-1

        elif search_array[middle_index] < search_val:
            start_index = middle_index+1

    return -1
    


search_array = [ 2, 3, 4, 10, 40 ]
search_val = 4
 
# Function call
# result = binary_search(search_array, 0, len(search_array)-1, search_val)
iter_result = binary_search_iterative(search_val, search_array)
 
if iter_result != -1:
    print("Element is present at index", str(iter_result))
else:
    print("Element is not present in array")
