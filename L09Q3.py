Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random

# Generate 10 different random numbers between -15 and 15
random_numbers = random.sample(range(-15, 16), 10)

# Create a new list containing the squares of the numbers
squared_numbers = [num ** 2 for num in random_numbers]

# Print the lists
print("Random numbers:", random_numbers)
print("Squared numbers:", squared_numbers)
