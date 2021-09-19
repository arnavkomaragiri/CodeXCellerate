def isPalindrome(x):
  if x < 0:
    return False
  if x % 10 == 0:
    return x == 0
  str_x = str(x)
  str_pal = str_x[::-1]
        
  for i in range(len(str_x)):
    for j in range(len(str_pal)):
      if str_x[i] != str_pal[j] and i == j:
        return False
  return True