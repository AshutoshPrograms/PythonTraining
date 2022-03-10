def square_num(n):
  return n * 3
nums = [1, 2, 3, 4, 5, 6, 7]
result = map(square_num, nums)
print(list(result))
