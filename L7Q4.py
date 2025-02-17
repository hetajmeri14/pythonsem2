Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> food_items = [("Burger", 5), ("Pizza", 8), ("Pasta", 6), ("Salad", 4), ("Sushi", 12)]
>>> sorted_food_items = sorted(food_items, key=lambda x: x[1], reverse=True)
>>> print("Food items sorted by price (descending order):")
Food items sorted by price (descending order):
>>> for item in sorted_food_items:
	print(item)

	
('Sushi', 12)
('Pizza', 8)
('Pasta', 6)
('Burger', 5)
('Salad', 4)
>>> 
