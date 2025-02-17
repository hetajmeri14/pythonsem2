Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> names_list = [("John", "Doe"), "Alice", ("Bob", "Smith"), "Eve", ("Charlie", "Brown")]
>>> boys_count = 0
>>> girls_count = 0
>>> 
>>> for ele in names_list:
	if isinstance(ele, tuple):
		boys_count +=1

		
>>> else
SyntaxError: invalid syntax
>>> girls_count += 1
>>> 
>>> print("number of boys:",boys_count)
number of boys: 3
>>> print("number of girls:", girls_count)
number of girls: 1
>>> 
>>> 
