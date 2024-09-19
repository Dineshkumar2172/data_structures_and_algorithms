# This sorting technique repeatedly finds the minimum element and sort it in order. Bubble Sort does not 
# occupy any extra memory space. During the execution of this algorithm, two subarrays are maintained, the 
# subarray which is already sorted, and the remaining subarray which is unsorted. During the execution of 
# Selection Sort for every iteration, the minimum element of the unsorted subarray is arranged in the sorted 
# subarray. Selection Sort is a more efficient algorithm than bubble sort. Sort has a Time-Complexity of O(n2) 
# in the average, worst, and in the best cases.

# Example:
# For the list [29, 10, 14, 37, 14], Selection Sort works as follows:

# Step 1: Find the smallest number (10) and swap it with 29. List becomes [10, 29, 14, 37, 14].
# Step 2: Find the next smallest number (14) and swap it with 29. List becomes [10, 14, 29, 37, 14].
# Step 3: Find the next smallest (14) and swap it with 29. List becomes [10, 14, 14, 37, 29].
# Step 4: Finally, 29 and 37 are swapped. List becomes [10, 14, 14, 29, 37].

# Function to perform Selection Sort
def selection_sort(number_list):
    # Loop through the list to select each number
    for current_position in range(len(number_list)):
        # Assume the current number is the smallest in the unsorted part
        smallest_position = current_position

        # Loop through the remaining unsorted numbers to find the smallest
        for next_position in range(current_position+1, len(number_list)):
            if number_list[next_position] < number_list[smallest_position]:
                smallest_position = next_position # Update the position of the smallest number

        # Swap the current number with the smallest number found
        number_list[current_position], number_list[smallest_position] = number_list[smallest_position], number_list[current_position]

# Example usage
numbers = [29, 10, 14, 37, 14]
print("Original list:", numbers)
selection_sort(numbers)  # Sort the list
print("Sorted list:", numbers)
