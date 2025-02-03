Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random

# Step 1: Create a list of 5 random odd integers
odd_numbers = [random.randrange(1,100,2) for _ in range(5)]
print("List of 5 random odd numbers:", odd_numbers)

# Step 2: Create a list of 4 random even integers
even_numbers = [random.randrange(2, 100, 2) for _ in range(4)]
print("List of 4 random even numbers:", even_numbers)

# Step 3: Replace the third element of the odd list with the even list
odd_numbers[2] = even_numbers
print("List after replacing the third element with even numbers:", odd_numbers)

# Step 4: Flatten the list
flattened_list = []
for item in odd_numbers:
    if isinstance(item, list):
        flattened_list.extend(item)
    else:
        flattened_list.append(item)

# Step 5: Print the final flattened list
print("Flattened list:", flattened_list)