Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> students = [(1, "John", 18), (2, "Alice", 17), (3, "Bob", 19), (4, "Eve", 18)]
>>> roll_numbers = []
>>> names = []
>>> ages = []
>>> 
>>> for student in students:
	roll_numbers.append(student[0])
	names.append(student[1])
	ages.append(student[2])

	
>>> print("Roll numbers:", roll_numbers)
Roll numbers: [1, 2, 3, 4]
>>> print("Names:", names)
Names: ['John', 'Alice', 'Bob', 'Eve']
>>> print("Ages:", ages)
Ages: [18, 17, 19, 18]
>>> 
>>> 
>>> 
