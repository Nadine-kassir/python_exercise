def is_in_list(my_list, number):
    if number in my_list:
        return True
    else:
        return False



# Ask the user to enter numbers separated by spaces
user_input = input("Enter numbers separated by spaces: ")

# Split the input into a list of strings, convert each to int, then make a set
number_set = set(int(num) for num in user_input.split())

num=int(input("entre numbre to search: "))
result=is_in_list(number_set,num)
print(result)
