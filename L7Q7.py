Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> my_tuple = (1, 2, 3, 4, 5)
>>> 
>>> temp_list = list(my_tuple)
>>> 
>>> temp_list.remove(3)
>>> 
>>> modified_tuple = tuple(temp_list)
>>> 
>>> print("Modified tuple after deletion:", modified_tuple)
Modified tuple after deletion: (1, 2, 4, 5)
>>> 
