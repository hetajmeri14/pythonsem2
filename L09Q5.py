Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> faculty_names = ["John Smith", "Elizabeth Brown", "David Lee", "Jennifer Wilson", "Christopher Garcia", "Mary Rodriguez"]

filtered_names = [name for name in faculty_names if len(name) > 8]

print(filtered_names)
