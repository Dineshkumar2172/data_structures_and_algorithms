# This sorting algorithm maintains a sub-array that is always sorted. Values from the unsorted part 
# of the array are placed at the correct position in the sorted part. It is more efficient in practice 
# than other algorithms such as selection sort or bubble sort. Insertion Sort has a Time-Complexity 
# of O(n2) in the average and worst case, and O(n) in the best case.

# Example:
# If the input array is [9, 5, 1, 4, 3], the steps are:

# Step 1: Start with 5 (the second element). Move 9 to the right, and place 5 at the start.
# Step 2: Next, take 1 and move both 9 and 5 to the right, placing 1 at the start.
# Step 3: Take 4, move 9 to the right, and place 4 between 1 and 5.
# Step 4: Finally, take 3, move 9 and 4 to the right, and place 3 between 1 and 4.
# At the end, the array will be [1, 3, 4, 5, 9].

# Function to perform Insertion Sort
def insertion_sort(number_list):
    # Loop through the list starting from the second number
    for current_position in range(1, len(number_list)):
        # The number we are trying to place correctly
        current_number = number_list[current_position]

        # Position of the last number in the sorted part of the list
        previous_position = current_position - 1 

        # Move numbers in the sorted part that are bigger than 'current_number' one position to the right
        while previous_position >= 0 and number_list[previous_position] > current_number:
            number_list[previous_position + 1] = number_list[previous_position] # Shift number to the right
            previous_position -= 1  # Move to the previous number
            
        # Place the 'current_number' in its correct position
        number_list[previous_position + 1] = current_number


# Example usage
numbers = [9, 5, 1, 4, 3]
print("Original list:", numbers)
insertion_sort(numbers)  # Sort the list
print("Sorted list:", numbers)
