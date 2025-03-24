Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> list1 = list(range(1, 7))  # [1, 2, 3, 4, 5, 6]
list2 = list(range(6, 0, -1)) # [6, 5, 4, 3, 2, 1]

result = list(map(lambda x, y: x + y, list1, list2))

print(result)
SyntaxError: multiple statements found while compiling a single statement
>>> 
