def linear_search(search_val, input_list):
    for i in range(len(input_list)):
        if input_list[i] == search_val:
            return True # if value exists
    return False # if value doesn't exist

search_list = list(range(10))
search_value = 1
if linear_search(search_value, search_list):
    print(f"value {search_value} exists in the given list")
else:
    print(f"value {search_value} does not exist in the given list")
