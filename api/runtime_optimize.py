def isPalindrome(x):
  if x < 0:
    return False
  if x % 10 == 0:
    return x == 0
  str_x = str(x)
  str_pal = str_x[::-1]
        
  for i in range(len(str_x)):
    if str_x[i] != str_pal[i]:
      return False
  return True

# Optimize the memory usage of the above code
def isPalindrome(x):
  if x < 0:
    return False
  if x % 10 == 0:
    return x == 0
  str_x = str(x)
  str_pal = str_x[::-1]
        
  for i in range(len(str_x)):
    if str_x[i] != str_pal[i]:
      return False
  return True
