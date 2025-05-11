def process_list(my_list):
    my_list = list(my_list)
    result = sorted([my_list[0], my_list[-1]])
    return result


# Ask the user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Split the input into a list of strings, convert each to int, then make a set
number_set = set(int(num) for num in user_input.split())

# Print the resulting set
print("The set is:", number_set)

processed_data = process_list(number_set)

print("Processed list (first and last elements sorted):", processed_data)