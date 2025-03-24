Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> lst = ['madam', 'Python', 'malayalam', 12321]

def is_palindrome(s):
  """Checks if a string or number is a palindrome."""
  s_str = str(s)  # Convert to string to handle both strings and numbers
  return s_str == s_str[::-1]

for item in lst:
  if is_palindrome(item):
    print(item)
