Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import random
fifty = [random.randrange(1,30,1) for _ in range(50)]
print("list of random 50 numbers:", fifty)