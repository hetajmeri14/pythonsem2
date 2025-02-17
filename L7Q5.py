Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> tuples_list = [("apple", 2), (), ("banana", 3), (), ("orange", 5), ()]
>>> cleaned_list = [tup for tup in tuples_list if tup]
>>> 
>>> print("List after removing empty tuples:")
List after removing empty tuples:
>>> print(cleaned_list)
[('apple', 2), ('banana', 3), ('orange', 5)]
>>> 
