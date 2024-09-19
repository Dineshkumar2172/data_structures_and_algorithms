# RECURSIVE APPROACH
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


search_array = [ 2, 3, 4, 10, 40 ]
search_val = 10
 
# Function call
result = binary_search(search_array, 0, len(search_array)-1, search_val)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")