Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def fun():
  print("This is function fun()")

def disp():
  print("Displaying some information from disp()")

def msg():
  print("A message from msg()")

functions = [fun, disp, msg]

for func in functions:
  func()
