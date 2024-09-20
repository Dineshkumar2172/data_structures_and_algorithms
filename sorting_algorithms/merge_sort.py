# Merge sort is a sorting algorithm that follows the divide-and-conquer approach. It works by 
# recursively dividing the input array into smaller subarrays and sorting those subarrays then 
# merging them back together to obtain the sorted array. In simple terms, we can say that the process
# of merge sort is to divide the array into two halves, sort each half, and then merge the sorted 
# halves back together. This process is repeated until the entire array is sorted.

# Example:
# For the list [38, 27, 43, 3, 9, 82, 10], Merge Sort works as follows:
# Divide: Split the list into [38, 27, 43] and [3, 9, 82, 10].
# Further Divide: Keep splitting until you have single-element lists. [38], [27], [43], [3], [9], [82], [10].
# Merge Step 1: Merge back the single-element lists into sorted pairs: [27, 38], [3, 43], [9, 10], [82].
# Merge Step 2: Continue merging: [3, 27, 38, 43] and [3, 9, 10, 82].
# Final Merge: Merge the two halves into [3, 9, 10, 27, 38, 43, 82].

# Function to perform Merge Sort
def merge_sort(numbers_list):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(numbers_list) <= 1:
        return numbers_list
    
    # Find the middle of the list to split it into two halves
    middle_position = len(numbers_list) // 2
    left_half = numbers_list[:middle_position]  # Left half of the list
    right_half = numbers_list[middle_position:] # Right half of the list
    
    # Recursively sort both halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Merge the two sorted halves
    return merge(left_sorted, right_sorted)


# Function to merge two sorted lists into one sorted list
def merge(left_list, right_list):
    sorted_list = []                # List to store the merged result
    left_index, right_index = 0, 0  # Pointer for the left and right list
    
    # Merge the two lists by comparing the elements one by one
    while left_index < len(left_list) and right_index < len(right_list):
        if left_list[left_index] < right_list[right_index]:
            sorted_list.append(left_list[left_index])
            left_index += 1
        else:
            sorted_list.append(right_list[right_index])
            right_index += 1
    
    # If there are any remaining elements in either list, add them to the sorted list
    sorted_list.extend(left_list[left_index:])
    sorted_list.extend(right_list[right_index:])
    
    return sorted_list
    
# Example usage
numbers = [38, 27, 43, 3, 9, 82, 10]
print("Original list:", numbers)
sorted_numbers = merge_sort(numbers)
print("Sorted list:", sorted_numbers)
