Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> from datetime import date
>>> date1 = (12, 5, 2023)
>>> date2 = (20, 8, 2024)
>>> 
>>> date1_obj = date(date1[2], date1[1], date1[0])
>>> date2_obj = date(date2[2], date2[1], date2[0])
>>> 
>>> difference = date2_obj - date1_obj
>>> 
>>> print(f"Number of days between the two dates: {difference.days}")
Number of days between the two dates: 466
>>> 
