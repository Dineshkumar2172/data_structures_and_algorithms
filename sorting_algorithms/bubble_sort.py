
# Bubble Sort is a simple sorting algorithm. This sorting algorithm repeatedly compares two adjacent 
# elements and swaps them if they are in the wrong order. It is also known as the sinking sort. It has a 
# time complexity of O(n2) in the average and worst cases scenarios and O(n) in the best-case scenario. 
# Bubble sort can be visualized as a queue where people arrange themselves by swapping with each other so 
# that they all can stand in ascending order of their heights. Or in other words, we compare two adjacent 
# elements and see if their order is wrong, if the order is wrong we swap them. (i.e arr[i] > arr[j] for 1 <= i < j <= s; 
# where s is the size of the array, if array is to be in ascending order, and vice-versa).

# Example:
# If the array is [64, 34, 25, 12, 22, 11, 90], the algorithm works as follows:

# Pass 1: The largest element, 90, is moved to the last position.
# Pass 2: The second largest element, 64, moves to its correct position, and so on.
# Eventually, after all passes, the array will be sorted in ascending order.

# Function to implement Bubble Sort
def bubble_sort(unsorted_array):
     # Outer loop: Traverse the array n-1 times
    for index in range(len(unsorted_array)):
        # Inner loop: Perform the comparisons and swap adjacent elements
        # As the largest element will "bubble up" to the end of the list after each outer loop,
        # we reduce the range of the inner loop by i because the last i elements are already sorted.
        for inner_index in range(len(unsorted_array) - index - 1):
            if unsorted_array[inner_index] > unsorted_array[inner_index+1]:
                temp_value = unsorted_array[inner_index+1]
                unsorted_array[inner_index+1] = unsorted_array[inner_index]
                unsorted_array[inner_index] = temp_value


arr = [64, 34, 25, 12, 22, 11, 90]
print("Original array:", arr)
bubble_sort(arr)
print("Sorted array:", arr)
