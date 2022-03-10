def reverse(s):
  str = ""
  for i in s:
    str = i + str
  return str
  
stringVal = "1234abcd"
print(reverse(stringVal))
