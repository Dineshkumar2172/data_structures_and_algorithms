# QuickSort is a sorting algorithm based on the Divide and Conquer that picks an element as a 
# pivot and partitions the given array around the picked pivot by placing the pivot in its correct 
# position in the sorted array.


# Example:
# For the list [33, 10, 59, 27, 41, 16, 19], Quick Sort works as follows:

# Choose Pivot: Choose 33 as the pivot.
# Partition: Split the list into:
#       1. less_than_pivot = [10, 27, 16, 19]
#       2. equal_to_pivot = [33]
#       3. greater_than_pivot = [59, 41]
# Recursive Sorting: Recursively sort [10, 27, 16, 19] and [59, 41].
# Combine: Combine the results to get the sorted list [10, 16, 19, 27, 33, 41, 59].


# Function to perform Quick Sort
def quick_sort(numbers_list):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(numbers_list) <= 1:
        return numbers_list
    
    # Choose a pivot element (usually the first element of the list)
    pivot = numbers_list[0]
    
    # Separate the list into three parts:
    less_than_pivot = [number for number in numbers_list[1:] if number < pivot] # 1. Numbers less than the pivot
    equal_to_pivot = [number for number in numbers_list if number ==  pivot]    # 2. Numbers equal to the pivot
    greater_than_pivot = [number for number in numbers_list if number > pivot]  # 3. Numbers greater than the pivot
    
    # Recursively sort the numbers less than and greater than the pivot
    return quick_sort(less_than_pivot) + equal_to_pivot + quick_sort(greater_than_pivot)
    
    
# Example usage
numbers = [33, 10, 59, 27, 41, 16, 19]
print("Original list:", numbers)
sorted_numbers = quick_sort(numbers)
print("Sorted list:", sorted_numbers)
